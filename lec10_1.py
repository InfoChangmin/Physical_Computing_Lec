#능동부저 실습
from machine import Pin
import time

bell = Pin(15,Pin.OUT)

bell.on()
time.sleep(1)
bell.off()