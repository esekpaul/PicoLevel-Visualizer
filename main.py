from machine import Pin, ADC
import time

pini_led = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
leduri = [Pin(p, Pin.OUT) for p in pini_led]
pot = ADC(Pin(26))

def setup():
    for l in leduri: l.value(0)
    print("Sistem stabilizat pornit...")

def loop():
    
    suma = 0
    for _ in range(10):
        suma += pot.read_u16()
    medie = suma // 10
    
    
    numar_aprins = int((medie / 65535) * 10.5) 
    
    for i in range(len(leduri)):
        if i < numar_aprins:
            leduri[i].value(1)
        else:
            leduri[i].value(0)
            
    time.sleep(0.05)

setup()
while True:
    loop()
