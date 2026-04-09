import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)
up = 9
GPIO.setup(up, GPIO.IN)
down = 10
GPIO.setup(down, GPIO.IN)

num = 0
sleep_time = 0.2
while True:
    print(GPIO.input(up), GPIO.input(down))
    if GPIO.input(up):
        num = num + 1
        if num > 255:
            num = 0
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num = num - 1
        if num < 0:
            num = 255
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down) & GPIO.input(up):
        num = 255
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)