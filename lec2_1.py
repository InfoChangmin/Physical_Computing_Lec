from machine import Pin
import time

led = Pin('LED', Pin.OUT)
led.on() # LED 켜기
time.sleep(2)
led.off() # LED 끄기