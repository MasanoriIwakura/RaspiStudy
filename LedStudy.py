import wiringpi as pi
import time

# GPIO mode
GPIO_IN = 0
GPIO_OUT = 1

# status
ON = 1
OFF = 0

# GPIO setting
led_pin = 20
sw_pin = 12

pi.wiringPiSetupGpio()
pi.pinMode(led_pin, GPIO_OUT)
pi.pinMode(sw_pin, GPIO_IN)

# Lighting up:ON, Lighting off:OFF
led_status = OFF
pi.digitalWrite(led_pin, OFF)

try:
    while(True):
        if (pi.digitalRead(sw_pin) == ON):
            if (led_status == ON):
                pi.digitalWrite(led_pin, OFF)
                led_status = OFF
                print("LED OFF")
            else:
                pi.digitalWrite(led_pin, ON)
                led_status = ON
                print("LED ON")
        time.sleep(0.5)
        
except KeyboardInterrupt:
	pass
