from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep
import dht  # 온습도 센서 라이브러리

DEFAULT_I2C_ADDR = 0x27
sensor = dht.DHT11(Pin(2))  # 2번핀 사용!

# led 변수 만들기
led_red = Pin(3, Pin.OUT)


def setup():
    global lcd
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # SDA는 0번핀, SCL은 1번 핀
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)


def loop():
    while True:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Temperature: {temp}°C   Humidity: {hum}% ")
        sleep(1)

        # LCD 출력부
        lcd.move_to(0, 0)
        lcd.putstr("Temp: {}".format(temp))
        lcd.move_to(0, 1)
        lcd.putstr("Humi: {}".format(hum))
        sleep(1)

        if hum > 80:
            led_red.on()
        else:
            led_red.off()


# 동작 시작 부분
setup()
loop()

