from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(2))  # 2번핀 사용 / 디지털핀 / DHT11로 했을 때 온습도 출력에 오류가 있을 경우 DHT22로 진행

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f"Temperature: {temp}°C   Humidity: {hum}% ")
    sleep(1)
