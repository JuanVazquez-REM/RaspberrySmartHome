import RPi.GPIO as GPIO
import time

servoPIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0.1) 
try:
    
    p.ChangeDutyCycle(20)
    time.sleep(2)
    p.ChangeDutyCycle(1)
        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

