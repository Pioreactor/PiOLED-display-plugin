#!/bin/bash

set -x
set -e

export LC_ALL=C

sudo systemctl start pioreactor_startup_run@pioled_display.service
sudo systemctl enable pioreactor_startup_run@pioled_display.service
