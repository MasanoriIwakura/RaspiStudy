#######################################
#    Use the dht11 driver
#    http://osoyoo.com/driver/dht11.py
#######################################
import RPi.GPIO as GPIO
import time
import dht11

# GPIO pin
DHTPIN = 12
# GPIO number mode
GPIO.setmode(GPIO.BCM)
# DHT11 result code(no error)
DHT_NO_ERR = 0
# DHT11 setting
instance = dht11.DHT11(pin = DHTPIN)

try:
    print("-- START --")
    while True:
        result = instance.read()
        if result.error_code == DHT_NO_ERR:
            print("temperature: {0}C, humidity: {1}%".format(result.temperature, result.humidity))
        else:
            print("error")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("--- END ---")