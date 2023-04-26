import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
def on_connect(client, userdata, flags, rc):
    # tragt hier euer selbstgewaehltes TOPIC ein
    client.subscribe("Tich3_G1")
def on_message(client, userdata, msg):
    current_payload = str(msg.payload.decode("utf-8"))
    PIN = 7
    GPIO.setmode(GPIO.BOARD)  # Physische Nummerierung
    GPIO.setup(PIN, GPIO.OUT)  # Festlegen des GPIOs als Ausgang
    GPIO.output(PIN, GPIO.HIGH)  # Licht an -- Spannung
    time.sleep(5)
    GPIO.output(PIN, GPIO.LOW)
    GPIO.cleanup()
##################################################################################
# den nachfolgenden teils lasst ihr unveraendert
##################################################################################
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.209.33", 1883, 60)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
client.loop_forever()