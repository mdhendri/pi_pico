from machine import ADC, Pin, PWM
import time

# Initialize ADC (Analog to Digital Converter)
adc = ADC(Pin(26))  # GP26 is ADC0 on the Raspberry Pi Pico
value = 0
#Using external LED, build PWM object PWM LED
pwm_LED1=PWM(Pin(2))  # GPIO3 for PWM output to LED
pwm_LED1.freq(500)

while True:
    # Read the input on analog pin ADC0 (value between 0 and 65535)
    value = adc.read_u16()  # Read the 16-bit ADC value directly

    description = ""
    # We'll have a few thresholds, qualitatively determined
    if value < 655:
        description = "Dark"
    elif value < 13107:
        description = "Dim"
    elif value < 32768:
        description = "Light"
    elif value < 52429:
        description = "Bright"
    else:
        description = "Very bright"

    print(f"Analog reading: {value} - {description}")

    new_value = 65535 - value  # Invert the value for LED brightness
    print(new_value)
    pwm_LED1.duty_u16(new_value)
    time.sleep(0.1)  # delay for 500 milliseconds