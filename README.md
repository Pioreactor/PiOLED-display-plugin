## PiOLED display plugin for the Pioreactor

Display growth rate, normalized OD, and temperature for each Pioreactor using the [Adafruit PiOLED display](https://www.adafruit.com/product/3527)


### Hardware required

 - [Adafruit PiOLED display](https://www.adafruit.com/product/3527)
 - [0.1" 2x20-pin Strip Right Angle Female Header](https://www.adafruit.com/product/2823)


### Software installation

Install from the UI, or run:
```
pio plugins install pioled-display-plugin
```

You may get a "hardware not installed" error. That's okay, we'll do that next.

### Hardware installation

With the Pioreactor turned off (you can pull the plug), install the 2x20 right-angle header onto the the 2x20 header on the Pioreactor HAT. Attach the PiOLED display onto the right-hand side of the new header, with the orientation as shown in the image below:

<img width="462" alt="Screenshot 2023-06-21 at 2 40 14 PM" alt="PiOLD attached to the right-angle headers." src="https://github.com/Pioreactor/PiOLED-display-plugin/assets/884032/3b3096d0-4cfa-4a74-8ff1-36cff2fb4d99">

Power back on the Pioreactor.
