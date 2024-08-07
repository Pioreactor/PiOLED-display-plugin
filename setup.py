# -*- coding: utf-8 -*-
from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

setup(
    name="pioled-display-plugin",
    version="0.4.0",
    license_files=("LICENSE.txt",),
    description="Use an OLED display with your Pioreactor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="hello@pioreactor.com",
    author="Pioreactor",
    url="https://github.com/Pioreactor/PiOLED-display-plugin",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["adafruit-circuitpython-ssd1306==2.12.16", "Pillow==10.1.0"],
    entry_points={"pioreactor.plugins": "pioled_display_plugin = pioled_display_plugin"},
)
