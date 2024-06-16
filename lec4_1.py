# LCD 활용 예제
from machine import I2C, Pin, time_pulse_us
from i2c_lcd import I2cLcd
import time

DEFAULT_I2C_ADDR = 0x27

def setup():
    global lcd
    i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000) # SDA는 0번핀, SCL은 1번 핀
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def loop():
    while True:
        lcd.move_to(0,0) # 첫번째 줄
        lcd.putstr("Changmin Hong") # 작성할 내용
        lcd.move_to(0,1) # 두번째 줄
        lcd.putstr('Ulsan Girl\'s') # 작성할 내용
        lcd.move_to(15, 0)  # 특정 공간을 지정
        lcd.putstr('1')  # 작성할 내용
        time.sleep(1)
        lcd.clear()

# 동작 시작 부분
setup()
loop()