# PIR + DHT11 + LCD
from machine import I2C, Pin
from i2c_lcd import I2cLcd
from time import sleep
import dht

sensor = dht.DHT11(Pin(2))  # 2번핀 사용 / 디지털핀 / DHT11로 했을 때 온습도 출력에 오류가 있을 경우 DHT22로 진행
DEFAULT_I2C_ADDR = 0x27
pir = Pin(16, Pin.IN, Pin.PULL_UP)

def setup():
    global lcd
    i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def loop():
    while True:
        #온, 습도 센서 데이터 수집부
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Temperature: {temp}°C   Humidity: {hum}% ")

        # LCD 출력부
        lcd.move_to(0,0)
        lcd.putstr(f" T: {temp}    H: {hum}")
        lcd.move_to(0,1)
        lcd.putstr("-waiting motion-")
        sleep(1)
        lcd.clear()

        # PIR 센서 감지부
        print(pir.value())
        if pir.value() == 0:
           lcd.move_to(0,1)
           lcd.putstr("Detected")
           print("Motion Detected")
        else:
           print("waiting motion")
        sleep(1)

# 동작 시작 부분
setup()
loop()