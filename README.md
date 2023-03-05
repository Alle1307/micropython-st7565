ST7565 LCD driver for micropython
=================================

Description
-----------
This is micropython driver for LCDs based on **ST7565** controller.
Only serial mode sopported.

Wiring example for ESP8266-based or RP-Pico modules
----------------------------------------

|LCD | ESP8266|RP-Pico |
|----|--------|--------|
|A0  | GPIO 0 | GPIO20 |
|RST | GPIO 16| GPIO21 |
|CS  | GPIO 15| GPIO22 |
|DATA| GPIO 13| GPIO19 |
|SCK | GPIO 14| GPIO18 |

Usage example
-------------
```python
import machine
from st7565 import ST7565
#Using wiring for RP-Pico
RST = Pin(21, Pin.OUT)
A0 = Pin(20, Pin.OUT)
CS = Pin(22, Pin.OUT)
spibus = SPI(1, baudrate=1000000, polarity=1, phase=1)

display = ST7565(spibus, A0, CS, RST)
display.fill(1)
display.show()
```
