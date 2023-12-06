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

  if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)

  if result.temperature > 33:
    red.on()
    yellow.off()
    green.off()
    blue.off()
    white.off()
  elif 25 < result.temperature < 33:
    red.off()
    yellow.on()
    green.off()
    blue.off()
    white.off()
  elif 15 < result.temperature < 25:
    red.off()
    yellow.off()
    green.on()
    blue.off()
    white.off()
  elif 0 < result.temperature < 15:
    red.off()
    yellow.off()
    green.off()
    blue.on()
    white.off()
  elif result.temperature < 0:
    red.off()
    yellow.off()
    green.off()
    blue.off()
    white.on()
    
