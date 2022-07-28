from machine import Pin
from utime import sleep
from utime import sleep_ms
from machine import Timer

                                                                           


import rgb 
import mfrc522
import network, time, urequests
from machine import Pin, ADC, PWM 
from utelegram import Bot
from machine import Timer

TOKEN = '5528059287:AAGnyHBiL-PNghcVSzLjwIkhWos3loICq_s'

bot = Bot(TOKEN) # Token Bott

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
 
def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

def map(x):
        #return int((x - 0) * (8000-1800) / (180 - 0) +1800) # v1.19 -- duty_u16(m) -- 0 y 65536
        return int((x - 0) * (125- 25) / (180 - 0) + 25) 


if conectaWifi ("erikacruz","emilio12"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    print("ok")
    
    @bot.add_message_handler("Hola")
    def help(update):
        update.reply(''' ¡Bienvenidos a SERFID! \U0001F600
                     \n Menu Principal \U0001F606 
                     \n Elije una opción:
                     
                Estado ROJO:1
                Estado VERDE: 2
                
                LUZ Encendida \U0001F31E:ON
                LUZ Apagada \U0001F31A:OFF
               
                     \n No olvides que estoy para ayudarte \U0001F609 ''')
      
    
    @bot.add_message_handler("1")
    def help(update):
        sensorDHT.measure()
        tem = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply("EriKa Cruz, " + str(tem) + "°c! \U0001F975")
                      
    @bot.add_message_handler("2")
    def help(update):
        sensorDHT.measure()
        tem = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply("Raul Martinez, " + str(hum) + "%! \U0001F4A6")
          
    @bot.add_message_handler("ON")
    def help(update):
        rojo.on(0)
        update.reply("Encendido \U0001F917")
        
    @bot.add_message_handler("OFF")
    def help(update):
        verde.on(1)
        update.reply("Apagado \U0001F634")
               

    bot.start_loop()
    
    
else:
       print ("Conectividad invalida")
       miRed.active (False)
 
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