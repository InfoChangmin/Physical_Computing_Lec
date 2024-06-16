#LCD + DHT11
# LCD 활용 예제
from machine import I2C, Pin, time_pulse_us
from i2c_lcd import I2cLcd
import time
import dht

DEFAULT_I2C_ADDR = 0x27
sensor = dht.DHT11(Pin(2))  # 2번핀 사용 / 디지털핀 / DHT11로 했을 때 온습도 출력에 오류가 있을 경우 DHT22로 진행

def setup():
    global lcd
    i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000) # SDA는 0번핀, SCL은 1번 핀
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def loop():
    while True:
        # DHT11 측정부
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Temperature: {temp}°C   Humidity: {hum}% ")
        time.sleep(1)

        # LCD 출력부
        lcd.move_to(0,0)
        lcd.putstr("Temp: {}".format(temp))
        lcd.move_to(0,1)
        lcd.putstr("Humi: {}".format(hum))
        time.sleep(1)

# 동작 시작 부분
setup()
loop()
