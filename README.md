# Raspberry Pi Sense Hat Python Demos

### Notes

Version 2.0 of the Sense Hat contains an additional TCS34725 color sensor. To silence warnings about the missing sensor on a Version 1.0 board:

```
import logging
from sense_hat import SenseHat

logging.getLogger().setLevel(logging.ERROR)
sense = SenseHat()

```

[astro-pi/python-sense-hat github issue #121](https://github.com/astro-pi/python-sense-hat/issues/121#issuecomment-1179164651)


12 data points + cpu temp = 13

```
temp 27.8846435546875
pressure 0
compass 159.25725325438287
orientation {'roll': 0.042578191996562834, 'pitch': 356.1932175448687, 'yaw': 159.25725325438287}
gyro {'roll': 0.06651560379907745, 'pitch': 356.18573806084066, 'yaw': 159.27696518032752}
accel {'roll': 0.0665920365507368, 'pitch': 356.18495045465204, 'yaw': 159.27696518032752}
```
