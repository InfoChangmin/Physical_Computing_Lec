#조도센서 활용
from machine import Pin, ADC
import time

# 조도, 토양수분감지센서, 방수형온도계
jodo = ADC(26)

while True:
    print(jodo.read_u16() / 1024 * 100) # 밝다=값이 작다, 어둡다=값이 크다
    time.sleep(1)