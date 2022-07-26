from machine import Pin
from utime import sleep
from utime import sleep_ms
from machine import Timer
import rgb 
import mfrc522 

rojo = Pin(2, Pin.OUT)
amarillo = Pin(5, Pin.OUT)
verde = Pin(15, Pin.OUT)

r = Pin(21, Pin.OUT)
g = Pin(16, Pin.OUT)
b = Pin(17, Pin.OUT)

def display(R, G, B):

  r.value(R)
  g.value(G)
  b.value(B)
  
rgbobj = rgb.rgb(21, 16, 17, False)
rgbobj.off()

rojo = Pin(2, Pin.OUT)
amarillo = Pin(5, Pin.OUT)
verde = Pin(15, Pin.OUT)

p2 = Pin(2, Pin.OUT)
p2.on()

#init(sck, mosi, miso, rst, cs)
rdr = mfrc522.MFRC522(18, 23, 19, 4, 22)

def readRfid():
     p2.value(not p2.value)
     cardValue = rdr.getCardValue()

     if cardValue != "":
        print(cardValue)

        if cardValue == "0xda26d83f":
            rojo.on()
            rgbobj.red()                     
        if cardValue == "0x1a2f902e":
            verde.on()
            rgbobj.green()
        if cardValue == "":
            rgbobj.off()
        else:
            pass
            
            
tim1 = Timer(1)
tim1.init(period=55000, mode=Timer.PERIODIC, callback=lambda t:
    readRfid() 
)
 
     
while True:
 
    rojo.on()
    amarillo.off()
    verde.off()
    display(0,255,0)
    sleep_ms(500)
    sleep(6.980)
    rojo.off()
    amarillo.on()
    verde.off()
    sleep(0.920)
    rojo.off()
    amarillo.off()
    verde.on()
    display(255,0,0)
    sleep_ms(500)
    sleep(6.980)
    rojo.off()
    amarillo.on()
    verde.off()
    sleep(0.920)
    rojo.on()
    amarillo.off()
    verde.off()
    display(0,255,0)
    sleep_ms(500)
    sleep(0.980)

    