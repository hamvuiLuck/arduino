import Stepper
from machine import Pin, ADC
import time

# for the ESP8266 
# In1 = Pin(2,Pin.OUT) # IN1-> GPIO2 
# In2 = Pin(0,Pin.OUT) # IN1-> GPIO0 
# In3 = Pin(4,Pin.OUT) # IN1-> GPIO4 
# In4 = Pin(5,Pin.OUT) # IN1-> GPIO5 

# for ESP32
In1 = Pin(32,Pin.OUT)

In2 = Pin(33,Pin.OUT)
In3 = Pin(25,Pin.OUT)
In4 = Pin(26,Pin.OUT)
infrarouge = ADC(Pin(34))
s1 = Stepper.create(In1,In2,In3,In4, delay=1)
while True:
    s1.step(500) # rotate the stepper motor clockwise
    time.sleep(1)
    s1.step(500,-1) # rotate the stepper motor anti-clockwise
    time.sleep(1)
