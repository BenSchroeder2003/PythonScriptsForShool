import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
i = 0
while i < 4:
    GPIO.output(13, GPIO.HIGH)
    sleep(0.3)
    print("I bims 1 skript + " + str(i))
    GPIO.output(13, GPIO.LOW)
    sleep(0.3)
    i = i + 1
