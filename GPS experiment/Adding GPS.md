# Adding GPS to Pico with 128x64 Graphics LCD display
In the main folder wehave connected the Graphics display to the Pico and it is now time to add a sensor and make the data visible.
I decided to add a GPS module and use this to synchronize the RTC in the Pico and show the location in the Maidenhead form as is used by HAM radio amateurs.
The GPS outputs serial data which can be read by the Pico's UART. The GPS module must be powerd also with 3,3V. The Rx of the Pico must be connected to the Tx of the GPS module.
Also I have decided to monitor the PPS signal. When this is not present the module is not receiving any signal it may take quite a long time before there is some signal and I have experienced some unexpected behaviour when this signal is not present.
## Schematics
![This is the schematics](/picture/GPS-Tracker.png)
## Software
A little [UART-test program](./UART-test.py) has been added in order to check the correct working of the communication between the GPS-module and the Pico. When this works correctly you should see the serial output as NMEA lines in your shell window.
When that works it is time to work with the received GPS signals. Download the [GPS-Tracker.py software](./GPS-Tracker.py) and run it.
