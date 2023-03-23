# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="piOLED_display_plugin",
    version="0.0.2",
    license_files = ('LICENSE.txt',),
    description="Use an OLED display with your Pioreactor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="hello@pioreactor.com",
    author="Cameron Davidson-Pilon",
    url="https://github.com/Pioreactor/PiOLED-display-plugin",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["adafruit-circuitpython-ssd1306"],
    entry_points={
        "pioreactor.plugins": "piOLED_display_plugin = piOLED_display_plugin"
    },
)