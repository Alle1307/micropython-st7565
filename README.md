
# Instruction how to make a 128x64 graphics LCD display with ST7565 driver work on a Raspberry Pi Pico using micropython

## **Table of Contents**
+ [Introduction](#introduction)
+ [Preparation](#preparation)
+ [Step 1 Wiring](#step-1-wiring)
+ [Step 2 Get the display software driver](#step-3-get-the-display-software-driver)
+ [Step 3 Run the test program](#step-4-run-the-test-program)
+ [Further experimenting](#further-experimenting)

## **Introduction**
It happened that I came across about 20 LCD displays that looked interesting for my Raspberry Pi Pico experiments. These displays were salvaged from disassembled electronics at my Hamradio club. In this experiment a Raspberry Pi Pico with MicroPython is used as a prove of concept. Although this display  appears to be obsolete there are similar displays on the market that can be used instead with some alterations like the wiring and the software driver.

This display was a LM6020c and is a simple black and white 128x64 dots graphics LCD display. The complete [datasheet](https://datasheetspdf.com/pdf-file/1397601/TOPWAY/LM6020CCW/1) [^1] is still available on internet. 

From the datasheet it is found that the LM6020 contains a ST7565 display driver and has a serial interface fitted with an 8 wire flexible flat cable (ffc) to be connected to a MCU. The display works on 3,3 Volts which is perfectly suited to the Pico. 

## **Preparation**
The whole experiment is mounted on a standard breadboard and in order to connect the display to the Pico an 8 pin 1mm ffc adapter board (FPC-8P 1.0mm) is required, these adapter boards can be ordered through the usual channels on internet. The board is fitted with an extra layer board underneath so it can bridge over the middle gap of the breadboard, otherwise the pins get shortcircuited. I have soldered a long header on one side of the Pico so the pins can also be used on the top.

In this experiment a Raspberry Pi Pico with MicroPython is used to run the software. The original software display driver file was actually written for an ESP32, but with some slight alterations in the wiring it worked directly on the RP Pico. 
![](/picture/LM6020%20testing.jpg)

It is assumed the RP Pico is connected to a host PC (desktop, laptop or Raspberry Pi with desktop OS) through USB with the Thonny IDE application installed on the host PC and initiated through the Thonny IDE. Other IDE’s should work but have not been tested.

In Thonny on the bottom line at the right there is a remark showing which environment it is using. It should read Micropython (Raspberry Pi Pico), if not click on this line and select the correct environment. This should should be visible in the shell window. If not please read the official Raspberry Pi - Getting started guide.

Setting up a working system is therefor rather easy and can be done in some simple steps.

## **Step 1 Wiring**
Connect the flat cable to the adapter board, which has the following layout and connect this board in turn to a RP Pico. Note that the numbering on this board is confusing and the correct numbering is on other side of the board!

|**LM6020C Pin Description**|**Raspberry PI Pico**|
| :-: | :-: |
|**PIN NO**|**PIN Name**|**I/O**|**Descriptions**|**PIN Name**|**PIN NO**|
|1|VSS|Supply|Negative power supply,0V|GND|23|
|2|VDD|Supply|Positive power supply|3V3(OUT)|36|
|3|SI|I/O|Serial data input|GP19/SPI0\_SCK|24|
|4|SCL|I/O|Serial clock input|GP18/SPI0\_TX|25|
|5|A0|Input|<p>Register Select</p><p>A0 = H, Transferring the Display Data</p><p>A0 = L, Transferring the Control Data</p>|GP20|26|
|6|/RES|Input|<p>Reset signal</p><p>/RES = L, Initialization is executed</p><p>/RES = H, Normal running</p>|GP21|27|
|7|/CS1|Input|<p>Chip Select</p><p>/CS1=L, enable access to the LCD module</p><p>/CS1=H, disable access to the LCD module</p>|GP22|29|
|8|BLA|Power|Backlight Positive Supply|3V3 via resistor|36|

![This is the schematics](/picture/Pico%20-%20LM6020%20Schematics.png)

## **Step 2 Get the display software driver**
Download the st7565.py driver, extract and save it.
Click on the open icon. It should give you an option ‘Where to open from’ with two choices ‘This Computer’ or ‘ Raspberry Pi Pico’. Use this computer and get the downloaded st7565.py software driver. Save a copy on the RP Pico.

Open a new file and copy the given demonstation program and paste it into Thonny,save this also on the RP Pico as demo.py. It is recommended to save a copy on your computer.
## **Step 3 Run the test program**
Copy the MicroPython [demonstration program](/display_test.py) to Thonny and save it on the RP Pico as Display\_test.py or whatever name you can think of and run it.
This demonstration program also demonstrates some framebuffer commands!

## **Further experimenting**
The available commands for drawing in the FrameBuffer are described in a separate file in this repository.

In addition I have added a GPS module to this configuration that will update the internal clock and determine the location in maidenhead locator as is used by Ham radio operators. Read [here](/GPS%20experiment/Adding%20GPS.md) for further details.


[^1]: <https://datasheetspdf.com/pdf-file/1397601/TOPWAY/LM6020CCW/1>
[^2]: https://github.com/nquest/micropython-st7565/blob/master/st7565.py
