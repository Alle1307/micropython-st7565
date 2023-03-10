# Adding GPS to Pico with 128x64 Graphics LCD display
In the main folder wehave connected the Graphics display to the Pico and it is now time to add a sensor and make the data visible.
I decided to add a GPS module and use this to synchronize the RTC in the Pico and show the location in the Maidenhead form as is used by HAM radio amateurs.
The GPS outputs serial data which can be read by the Pico's UART. The GPS module must be powerd also with 3,3V. The Rx of the Pico must be connected to the Tx of the GPS module.
