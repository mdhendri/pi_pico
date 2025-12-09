#MicroPython implementation of raspberry PI Pico board LED breathing lamp program example
import time
from machine import Pin,PWM
PWM_PulseWidth1=0
#Using external LED, build PWM object PWM LED
pwm_LED1=PWM(Pin(2))
pwm_LED2=PWM(Pin(3))
pwm_LED3=PWM(Pin(4))
#Set the PWM LED frequency
pwm_LED1.freq(500)
pwm_LED2.freq(500)
pwm_LED3.freq(500)
while True:
    while PWM_PulseWidth1<65535:
        PWM_PulseWidth1=PWM_PulseWidth1+50
        time.sleep_ms(1)   #Delay 1 ms 
        pwm_LED1.duty_u16(PWM_PulseWidth1)
        pwm_LED2.duty_u16(PWM_PulseWidth1)
        pwm_LED3.duty_u16(PWM_PulseWidth1)
    while PWM_PulseWidth1>0:
        PWM_PulseWidth1=PWM_PulseWidth1-50
        time.sleep_ms(1)
        pwm_LED1.duty_u16(PWM_PulseWidth1)
        pwm_LED2.duty_u16(PWM_PulseWidth1)
        pwm_LED3.duty_u16(PWM_PulseWidth1)