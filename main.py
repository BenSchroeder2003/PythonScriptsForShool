#!/user/bin/python3 # Shebang-Zeile, mit welchem Programm zu öffnen
import RPi.GPIO as GPIO
import time
PIN = 26
GPIO.setmode(GPIO.BOARD) # Physische Nummerierung
GPIO.setup(PIN, GPIO.OUT) # Festlegen des GPIOs als Ausgang
GPIO.output(PIN, GPIO.HIGH) # Licht an -- Spannung
time.sleep(5)
GPIO.output(PIN, GPIO.LOW)
GPIO.cleanup()
