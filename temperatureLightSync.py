from gpiozero import LED
import RPi.GPIO as GPIO
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

red = LED(17)
yellow = LED(27)
green = LED(22)
blue = LED(23)
white = LED(24)

instance = dht11.DHT11(pin = 4)
result = instance.read()

while True:
  result = instance.read()
  
