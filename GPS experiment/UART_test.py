from machine import Pin, UART, SPI
import utime, time

# Start UART Assuming 9600bps default
baud = 9600
gps_module = UART(0, baud, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1, timeout=250)

status = False
try:    
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
            print('buffer is empty')
            gps_module = UART(0, baud, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1, timeout=250)
    while True:
        print('proces can be executed')
        time.sleep(2)
       
except KeyboardInterrupt:
    print('terminated')
