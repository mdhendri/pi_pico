import network
import socket
import time
import random
from machine import Pin, PWM

# Create an LED object on pin 'LED'
led = Pin('LED', Pin.OUT)
led_blink = Pin(20)
led_pwm = PWM(led_blink)
duty_step = 129  # Step size for changing the duty cycle

#Set PWM frequency
frequency = 5000
led_pwm.freq (frequency)

# --- AP Configuration ---
ssid = 'NAME'
password = 'PASSWORD' # Must be 8+ chars

# HTML web page to be served
def web_page(state, random_value):
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pico Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Raspberry Pi Pico Web Server</h1>
            <h2>Led Control</h2>
            <form action="./lighton">
                <input type="submit" value="Light on" />
            </form>
            <br>
            <form action="./lightoff">
                <input type="submit" value="Light off" />
            </form>
            <p>LED state: {state}</p>
            <h2>Fetch New Value</h2>
            <form action="./value">
                <input type="submit" value="Fetch value" />
            </form>
            <p>Fetched value: {random_value}</p>
        </body>
        </html>
        """
    return str(html)

# Set up Access Point
ap = network.WLAN(network.AP_IF)
ap.active(False)
# Setting power mode
ap.config(pm = 0xA11142)


ap.config(essid=ssid, password=password) # Set SSID & Password

# Set the static IP address for the Access Point
# The tuple contains (IP_address, subnet_mask, gateway_IP, DNS_server)
# Replace with your desired static IP configuration
ap.active(True) # Activate the AP
ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))

# --- Basic Server Setup ---
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] # Get IP & port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5) # Listen for up to 5 connections

print('Access Point "{}" started, IP: {}'.format(ssid, ap.ifconfig()[0]))

# Initialize variables
state = "OFF"
random_value = 0

while True:
    try:
        # Accept new connections
        conn, addr = s.accept()
        print('Client connected:', addr)
        # Receive and parse the request
        request = conn.recv(1024)
        request = str(request)
        print('Request content = %s' % request)

        try:
            request = request.split()[1]
            print('Request:', request)
        except IndexError:
            pass

        # Process the request and update variables
        if request == '/lighton?':
            print("LED on")
            led.value(1)
            state = "ON"
        elif request == '/lightoff?':
            led.value(0)
            state = 'OFF'
        elif request == '/value?':
            random_value = random.randint(0, 20)

        response = web_page(state, random_value)

        # Send the HTTP response and close the connection
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
    except OSError as e:
        #catch and print errors
        print(e)