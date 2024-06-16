from machine import Pin

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_UP) # 내부 풀업 저항으로 연결

while True:
    if button.value() == 0: # 풀업저항이므로 0이면 눌림, 풀다운저항은 1이면 눌림 / 디지털핀의 값을 읽기 위해서는 .value()를 활용
        print('버튼이 눌렸습니다.')
        led.on()
    else:
        led.off()