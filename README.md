
# Instruction how to connect a LM6020c using micropython

**Table of Contents**

[Preparation](#__RefHeading___Toc1391_520338010)

[The LM6020c](#__RefHeading___Toc1393_520338010)

[ Step 1 Wiring](#__RefHeading___Toc1395_520338010)

[ Step 2 Set up the Integrated Development Environment (IDE)](#__RefHeading___Toc1397_520338010)

[ Step 3 Get the display software driver](#__RefHeading___Toc1280_4163719918)

[ Step 4 Run the test program](#__RefHeading___Toc1282_4163719918)

## **Preparation**
In this example a Raspberry Pi Pico with MicroPython is used, but with some slight alterations it should work on other MCU’s like an ESP32. The original display driver file was actually written for an ESP32.

It is assumed the RP Pico is connected to the PC through USB with the Thonny IDE application installed on the PC and initiated through the Thonny IDE. Other IDE’s may work but have not been tested.

## **The LM6020c**
The LM6020 is a simple black and white graphics LCD display with according to the specs a layout of 128x 64 dots. The complete [datasheet](https://datasheetspdf.com/pdf-file/1397601/TOPWAY/LM6020CCW/1) [^1].with more information can be found on the internetnet. It is fitted with a 8 wire flat cable (ffc). An 8 pin 1mm ffc adapter board is required to connect it to the MCU.

The LM6020 is fitted with a ST7565 display driver which has a serial interface that can be used through a SPI interface on the MCU.

Setting up a working system is therefor rather easy and can be done in some simple steps. All you need further is an 8 pin adapter board for 1mm ffc, they can be obtained through the usual channels on internet.
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
## **Step 2 Set up the Integrated Development Environment (IDE)**
It is recommended to use Thonny as your IDE connect this to your RP Pico.
On the bottom line at the right there is a remark showing which environment it is using. It should read Micropython (Raspberry Pi Pico), if not click on this line and select the correct environment.

## **Step 3 Get the display software driver**
Download the st7565.py driver, extract and save it.
Click on the open icon. It should give you an option ‘Where to open from’ with two choices ‘This Computer’ or ‘ Raspberry Pi Pico’. Use this computer and get the downloaded st7565.py software driver. Save a copy on the RP Pico.

Open a new file and copy the given demonstation program and paste it into Thonny,save this also on the RP Pico as demo.py. It is recommended to save a copy on your computer.
## **Step 4 Run the test program**
Copy the MicroPython demonstration program to Thonny and save it on the RP Pico as Display\_test.py or whatever name you can think of and run it.
This demonstration program also demonstrates some framebuffer commands!

The available commands for drawing in the FrameBuffer are described in Annex 2.
#

[^1]: <https://datasheetspdf.com/pdf-file/1397601/TOPWAY/LM6020CCW/1>
[^2]: https://github.com/nquest/micropython-st7565/blob/master/st7565.py
