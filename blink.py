import time
import RPi.GPIO as GPIO

pins = [4, 17, 22, 5, 20]

GPIO.setmode(GPIO.BCM)
while True:
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, True)
        time.sleep(0.03)
        GPIO.output(pin, False)
        time.sleep(0.03)
    pins.reverse()
