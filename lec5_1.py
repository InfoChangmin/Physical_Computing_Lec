from machine import I2C, Pin, time_pulse_us
from i2c_lcd import I2cLcd
import time

SOUND_SPEED=340
TRIG_PULSE_DURATION_US=10
trig_pin = Pin(15, Pin.OUT) # 15번핀 사용 / 초음파 발생부
echo_pin = Pin(14, Pin.IN)  # 14번핀 사용 / 초음파 수신부

def loop():
    while True:
        trig_pin.value(0)
        time.sleep_us(5)
        trig_pin.value(1)
        time.sleep_us(TRIG_PULSE_DURATION_US)
        trig_pin.value(0)

        ultrason_duration = time_pulse_us(echo_pin, 1, 30000)
        distance = SOUND_SPEED * ultrason_duration / 20000

        print(f"Distance : {distance} cm")
        time.sleep(1) # 1초 간격으로 측정진행

loop()