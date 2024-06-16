from machine import Pin
import time

PIR = Pin(16, Pin.IN, Pin.PULL_DOWN) # 16번핀 활용

def pir_handler(pin):
    time.sleep(0.1)
    if pin.value():
        print("움직임이 감지되었습니다.")

# 이벤트 형태로 PIR에 움직임이 감지될 때마다 반응
PIR.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)