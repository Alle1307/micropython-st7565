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

How to set it up
-------------
