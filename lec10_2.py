# 수동부저
from machine import Pin, PWM
from time import sleep

BuzzerObj = PWM(Pin(14))


def buzzer(buzzerPinObject, frequency, sound_duration, silence_duration):
    buzzerPinObject.duty_u16(int(65536 * 0.2))
    buzzerPinObject.freq(frequency)
    sleep(sound_duration)
    buzzerPinObject.duty_u16(int(65536 * 0))
    sleep(silence_duration)


buzzer(BuzzerObj, 329, 0.5, 0.1)  # MI
buzzer(BuzzerObj, 293, 0.2, 0.1)  # RE
buzzer(BuzzerObj, 329, 0.5, 0.1)  # MI
buzzer(BuzzerObj, 293, 0.2, 0.1)  # RE

# 버튼을 이용해서 주파수를 바꿔볼 수는 없을까?
'''
if button.value() == 0:
    freq_value = 329

elif button2.value() == 0:
    freq_value = 293
    '''
