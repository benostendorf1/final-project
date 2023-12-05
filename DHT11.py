#This code requires you to have previously downloaded a git repository
import RPi.GPIO as GPIO
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin = 4)
result = instance.read()

#this will result in a constant update in temperature
while True:
  result = instance.read()
  if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)

#I did not include an error statement because it would print the error result between each temperature check interval not sure how to fix
