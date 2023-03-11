from machine import Pin, UART, SPI, RTC
from driver.st7565 import ST7565
#import lib.to_maiden as maidenhead
import utime, time

#Oled I2C connection
#i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
#oled = SSD1306_I2C(128, 64, i2c)
#settings for SPI
sck = Pin(18)
mosi = Pin(19)
A0 = Pin(20, Pin.OUT)
RST = Pin(21, Pin.OUT)
CS = Pin(22, Pin.OUT)

PPS = Pin(26, Pin.IN)

fg = 1 #forground colour is black
bg = 0 #background colour is white

# initialiize the SPI interface and framebuffer for display
# select SPI0 with a clk speed 
spi = SPI(0, 1_000_000) 
display = ST7565(spi, A0, CS, RST)

# reset the RTC if required

year = 2023
month = 02
day = 16
dotw = 0
hour = 0
mins = 0
secs = 0
tz = 1  #setting of timezone
rtc = machine.RTC()
rtc.datetime((year, month, day, dotw, hour, mins, secs, 0))

# Initialize UART
baud =9600
gps_module = UART(0, baud, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1, timeout=250)
buff = bytearray(255)

#Reset GPS Coordinates
latitude = ""
longitude = ""
satellites = ""
gpsTime = ""
status = False

#set up screen
display.fill(bg)
display.text('GPS-Tracker', 20, 2, fg)
display.show()
nicedate =("{:02d}-{:02d}-{}".format(day, month, year))
# display.text(nicedate, 30, 15, fg)
nicetime = ("{:02d}:{:02d}:{:02d}".format(hour, mins, secs))
display.text('getting time', 20, 46, fg)
display.show()
display.text('getting time', 20, 46, bg)
time.sleep(1)

#function to convert raw Latitude and Longitude
#to actual Latitude and Longitude
def convertToDigree(RawDegrees):
    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) #degrees
    nexttwodigits = RawAsFloat - float(firstdigits*100) #minutes
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) # to 6 decimal places
    return str(Converted)
    
def setclock(parts):     #parse gpsTime = parts[1]
    hour = int(parts[1][0:2])
    if (hour >= (24-tz)) :
        hour = hour - (24-tz)
    else:
        hour += tz
    mins = int(parts[1][2:4])
    secs = int(parts[1][4:6])
    nicetime =("{:02d}:{:02d}:{:02d}".format(hour, mins, secs))
    print('The RTC time is set at: ' + nicetime)
    rtc.datetime((year, month, day, dotw, hour, mins, secs, 0))
   
def to_maiden(lat, lon, precision):
#    Returns a maidenhead string for latitude, longitude at specified level.
#
#    Parameters
#    ----------
#    lat : float,     latitude
#    lon : float,     longitude
#    precision : int, optional
#        level of precision (length of maidenhead grid string output)
#
#    Returns maiden : str ie Maidenhead grid string of specified precision
    A = ord("A")
    a = divmod(float(lon) + 180, 20)
    b = divmod(float(lat) + 90, 10)
    maiden = chr(A + int(a[0])) + chr(A + int(b[0]))
    lon = a[1] / 2.0
    lat = b[1]
    i = 1
    while (i < precision):
        i += 1
        a = divmod(lon, 1)
        b = divmod(lat, 1)
        if (not (i % 2)):
            maiden += str(int(a[0])) + str(int(b[0]))
            lon = 24 * a[1]
            lat = 24 * b[1]
        else:
            maiden += chr(A + int(a[0])) + chr(A + int(b[0]))
            lon = 10 * a[1]
            lat = 10 * b[1]
    if (len(maiden) >= 6):
        maiden = maiden[:4] + maiden[4:6].lower() + maiden[6:]
    return maiden
    
def local_position(parts):
    latitude = convertToDigree(parts[2])
    # parts[3] contain 'N' or 'S'
    if (parts[3] == 'S'):
        latitude = -latitude
    longitude = convertToDigree(parts[4])
    # parts[5] contain 'E' or 'W'
    if (parts[5] == 'W'):
        longitude = -longitude
    #display.text("Lat: "+latitude, 5, 15, fg)
    #display.text("Lng: "+longitude, 5, 25, fg)
    mhl = to_maiden(latitude, longitude, 3) # precision set to 3
    display.text(mhl, 40, 25, fg)

def showtime():
    t = rtc.datetime()
    nicetime =("Time:  {:02d}:{:02d}:{:02d}".format(t[4], t[5], t[6]))
    display.text('            ', 4, 46, fg)
    display.text(nicetime, 4, 46, fg)
    display.show()
    display.text(nicetime, 4, 46, bg)    #print("fix......" + gpsTime)
    
while (PPS == False): # If there is no PPS do not start the proces
    print('No signal')

print('Ready for reception')

while (status == False):
    #read_uart()
    gps_module.readline()
    buff = str(gps_module.readline())
    print(buff)
    if(buff != 'None'):
        parts = buff.split(",")
        if ((parts[0] == "b'$GPGGA") and (parts[6] == "1")):
            print('we have a fix')
            time.sleep(1)
            status = True                
    else:
        print('error reading GPS')
        gps_module = UART(0, baud, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1, timeout=250)
setclock(parts)
local_position(parts)
print('Proceeding with time update')
while True:
    try:
        showtime()  #show results
    except KeyboardInterrupt:
        print('terminated')
        display.fill(bg)
        display.text("Terminated" , 10, 30, fg)
        display.show()
        time.sleep(10)
        display.text("Terminated" , 10, 30, bg)
        display.show()
        break
    except:
        print('error')
        continue