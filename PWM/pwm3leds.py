from machine import Pin, PWM
import time

# Define the GPIO pins connected to the LEDs
LED_PIN_1 = 2
LED_PIN_2 = 3
LED_PIN_3 = 4

# Initialize PWM for each LED
# The frequency (e.g., 1000Hz) should be set for each PWM object
pwm_1 = PWM(Pin(LED_PIN_1))
pwm_2 = PWM(Pin(LED_PIN_2))
pwm_3 = PWM(Pin(LED_PIN_3))

# Set the frequency for each PWM channel (optional, but good practice)
pwm_1.freq(1000)
pwm_2.freq(1000)
pwm_3.freq(1000)

# Function to set the brightness of an LED (0-100%)
def set_brightness(pwm_object, brightness_percent):
    if not (0 <= brightness_percent <= 100):
        raise ValueError("Brightness percentage must be between 0 and 100.")
    # Map the percentage to a 16-bit duty cycle value (0-65535)
    duty_cycle = int(brightness_percent / 100 * 65535)
    pwm_object.duty_u16(duty_cycle)

# Example usage:
try:
    while True:
        
        for i in range(0, 101, 5):
            set_brightness(pwm_1, i)
            time.sleep(0.05)
       
        for i in range(100, -1, -5):
            set_brightness(pwm_1, i)
            time.sleep(0.05)
        time.sleep(0.5)

        for i in range(0, 101, 5):
            set_brightness(pwm_2, i)
            time.sleep(0.05)
       
        for i in range(100, -1, -5):
            set_brightness(pwm_2, i)
            time.sleep(0.05)
        time.sleep(0.5)

        for i in range(0, 101, 5):
            set_brightness(pwm_3, i)
            time.sleep(0.05)
       
        for i in range(100, -1, -5):
            set_brightness(pwm_3, i)
            time.sleep(0.05)
        time.sleep(0.5)
       


except KeyboardInterrupt:
    # Turn off all LEDs on exit
    set_brightness(pwm_1, 0)
    set_brightness(pwm_2, 0)
    set_brightness(pwm_3, 0)
    pwm_1.deinit()
    pwm_2.deinit()
    pwm_3.deinit()
    print("Program terminated and LEDs turned off.")