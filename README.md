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
