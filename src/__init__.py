# -*- coding: utf-8 -*-

import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import click

from msgspec.json import decode
from pioreactor.hardware import SCL, SDA
from pioreactor.whoami import get_unit_name, get_latest_experiment_name
from pioreactor import structs
from pioreactor.background_jobs.base import BackgroundJobContrib
from pioreactor import types as pt


class PiOLEDDisplay(BackgroundJobContrib):

    job_name = "piOLED_display"

    def __init__(self, unit: str, experiment: str):
        super().__init__(unit, experiment, plugin_name="PiOLED-display-plugin")

        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)

        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        self.disp.rotation = 2

        # Clear display.
        self.disp.fill(0)
        self.disp.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("1", (self.width, self.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)


        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = -2
        self.top = padding
        self.bottom = self.height - padding
        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0


        # Load default font.
        self.font = ImageFont.load_default()

        # intialize data
        self.growth_rate = None
        self.od = None
        self.temp = None

        self.update_display()
        self.start_passive_listeners()


    def update_od(self, msg: pt.MQTTMessage):
        if msg.payload:
            self.od = decode(msg.payload, type=structs.ODFiltered).od_filtered
        else:
            self.od = None
        self.update_display()

    def update_temp(self, msg: pt.MQTTMessage):
        if msg.payload:
            self.growth_rate = decode(msg.payload, type=structs.GrowthRate).growth_rate
        else:
            self.growth_rate = None
        self.update_display()

    def update_growth_rate(self, msg: pt.MQTTMessage):
        if msg.payload:
            self.temp = decode(msg.payload, type=structs.Temperature).temperature
        else:
            self.temp = None
        self.update_display()

    def start_passive_listeners(self):
        self.subscribe_and_callback(self.update_od, f"pioreactor/{self.unit}/{self.experiment}/growth_rate_calculating/od_filtered", allow_retained=False)
        self.subscribe_and_callback(self.update_growth_rate, f"pioreactor/{self.unit}/{self.experiment}/growth_rate_calculating/growth_rate", allow_retained=False)
        self.subscribe_and_callback(self.update_temp, f"pioreactor/{self.unit}/{self.experiment}/temperature_control/temperature", allow_retained=False)

    def update_display(self):
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        # Write four lines of text.
        self.draw.text((self.x, self.top + 0), self.unit, font=self.font, fill=255)
        if self.growth_rate:
            self.draw.text((self.x, self.top + 8),  f"  Growth rate: {self.growth_rate:.2f}/h", font=self.font, fill=255)
        if self.od:
            self.draw.text((self.x, self.top + 16), f"  OD:          {self.od:.2f} AU", font=self.font, fill=255)
        if self.temp:
            self.draw.text((self.x, self.top + 25), f"  Temp:        {self.temp:.0f} C", font=self.font, fill=255)

        # Display image.
        self.disp.image(self.image)
        self.disp.show()


@click.command(name="piOLED_display")
def click_pioled_display():
    lg = PiOLEDDisplay(
        unit=get_unit_name(), experiment=get_latest_experiment_name()
    )
    lg.block_until_disconnected()

