#######################################
#    Use the dht11 driver
#    http://osoyoo.com/driver/dht11.py
#######################################
import RPi.GPIO as GPIO
import time
import dht11
import milkcocoa.milkcocoa as milkcocoa

# GPIO pin
DHTPIN = 12
# GPIO number mode
GPIO.setmode(GPIO.BCM)
# DHT11 result code(no error)
DHT_NO_ERR = 0
# DHT11 setting
instance = dht11.DHT11(pin = DHTPIN)

# milkcocoa setting
# Note:
#   [blocking = True] is important.
#   Because, You can not push it continuously.
milkcocoaClient = milkcocoa.Milkcocoa.connectWithApiKey("app id", "api key", "secret", useSSL=False, blocking=True)
datastore = milkcocoaClient.datastore("temperature")
# push milkcocoa func
def on_push(e):
    print(e)
datastore.on("push", on_push)

try:
    print("-- START --")
    while True:
        result = instance.read()
        if result.error_code == DHT_NO_ERR:
            print("temperature: {0}C, humidity: {1}%".format(result.temperature, result.humidity))
            datastore.push({"temperature":"{0}".format(result.temperature)
                            , "humidity":"{0}".format(result.humidity)})
            time.sleep(10)
        else:
            print("error")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("--- END ---")
