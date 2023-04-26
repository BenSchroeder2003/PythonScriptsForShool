import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
LED=26
GREEN = '\033[92m' #GREEN
YELLOW = '\033[93m' #YELLOW
RED = '\033[91m' #RED
RESET = '\033[0m' #RESET COLOR
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
def on_connect(client, userdata, flags, rc):
    client.subscribe("Tich3_GP2")
def on_message(client, userdata, msg):
    current_payload = str(msg.payload.decode("utf-8"))
    if current_payload == "ON":
        print(GREEN + "ON" + RESET)
        GPIO.output(LED, GPIO.HIGH)
    else:
        if current_payload == "OFF":
            print(RED + "OFF" + RESET)
            GPIO.output(LED, GPIO.LOW)
        if not current_payload == "OFF":
            print("\n\nERROR")
            print(GREEN + "Fehlerhafte Nachricht empfangen: " + YELLOW + current_payload + RESET + "\n\n")
            for i in range(5):
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(0.09)
                GPIO.output(LED, GPIO.LOW)
                time.sleep(0.09)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.209.33", 1883, 60)
client.loop_forever()
clean()
# Made by JJ