import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
sensor = dht.DHT11

GPIO.setup(18, GPIO.IN)
while True:
    humidity,temperature = dht.read_retry(sensor, 18)
    print("Temperatura: ")
    print(temperature)

    print("Temperatura: ")
    print(humidity)
