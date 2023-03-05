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
# Examples for using LCD display with Raspberry Pi Pico
# For ESP use original SPI pins
from machine import Pin, SPI
from st7565 import ST7565
from time import sleep

#settings for SPI on Raspberry Pi Pico
sck = Pin(18)
mosi = Pin(19)
A0 = Pin(20, Pin.OUT)
RST = Pin(21, Pin.OUT)
CS = Pin(22, Pin.OUT)

fg = 1 #forground colour is black
bg = 0 #background colour is white

#initialiize the SPI interface and framebuffer
spi = SPI(0, 4_000_000) # select SPI0 with a clk speed 
display = ST7565(spi, A0, CS, RST)

#clear the framebuffer (display) and print opening text
display.fill(bg)
display.text('MicroPython!', 20, 20, fg)
display.hline(20, 29, 96, fg)

#and draw some shapes as examples

# Show outline of display adjust edge values to see if it is all useable
xmin = 4 #Left edge
ymin = 0 #Top edge
xmax = 124 # Right edge
ymax = 64 # Bottom edge
display.rect(xmin, ymin, xmax, ymax, fg) #shows active area
display.show() #write from framebuffer
sleep(2)

# Do some animation
ex = 12 # x = horizontal position
exmax = 120 # end of x position
ey = 10 # y = vertical postion
r = 5 # radius x&y radius are the same for a circle
display.ellipse(ex,ey,r,r,fg)
while ex != exmax:
    display.ellipse(ex,ey,r,r,bg)
    ex += 1
    display.ellipse(ex,ey,r,r,fg)
    display.show()
    sleep(0.1)
sleep(2)

# Finished, clear the screen
display.fill(bg)
display.text('Testing', 30 , 30, fg)
display.show()
sleep(2)
display.fill(fg) #use inversed colours
display.text('Testing', 30 , 30, bg) #use inversed colours
display.show()

display.hline(0, 15, 128, fg)
display.hline(0, 16, 128, fg)

# show a progress bar
ex = 1
mex = 128
display.rect(ex, 49, (mex - ex), 10, fg)
while ex != mex:
    ex = ex + 1
    display.vline(ex, 49, 10, fg)
    display.show()
    sleep(0.05)

# Finished, clear the screen
display.fill(bg)
display.show()

#Wrap it up
display.text('Hurray it works!', 4, 20, fg)
display.show()
sleep(1)
display.text('''That's all folks''', 4, 40, fg)
display.show()
sleep(5)

# Finished, clear the screen
display.fill(bg)
display.show()
print('Done')
```
