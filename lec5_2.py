# LCD + SR04
from machine import I2C, Pin, time_pulse_us
from i2c_lcd import I2cLcd
from utime import sleep
import time

DEFAULT_I2C_ADDR = 0x27
SOUND_SPEED=340
TRIG_PULSE_DURATION_US=10
trig_pin = Pin(15, Pin.OUT) # 15번핀 사용 / 초음파 발생부
echo_pin = Pin(14, Pin.IN)  # 14번핀 사용 / 초음파 수신부

def setup():
    global lcd
    i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000) # SDA는 0번핀, SCL은 1번 핀
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def loop():
    while True:
        trig_pin.value(0)
        time.sleep_us(5)
        trig_pin.value(1)
        time.sleep_us(TRIG_PULSE_DURATION_US)
        trig_pin.value(0)

        ultrason_duration = time_pulse_us(echo_pin, 1, 30000)
        distance = SOUND_SPEED * ultrason_duration / 20000

        print(f"Distance : {distance} cm") # Thonny 터미널에 출력

        lcd.move_to(0,0) # 첫번째 줄
        lcd.putstr("Changmin Hong") # 작성할 내용
        lcd.move_to(0,1) # 두번째 줄
        lcd.putstr('Dist:' + str(distance) + 'CM') # 측정한거리

        time.sleep(1)
        lcd.clear()

# 동작 시작 부분
setup()
loop()