import RPi.GPIO as GPIO
from Mongo import Mongodb

response = {'status': True, 'message': 'Accion realizada'}
class Dispositivo:

    def __init__(self,data): # data=nombre,estado,pin
        GPIO.setmode(GPIO.BCM)
        if(data['estado'] == 1):
            self.onDevice(data)
        elif(data['estado']== 0):
            self.offDevice(data)

    def onDevice(self,data):
        GPIO.setup(data['pin'], GPIO.OUT)
        GPIO.output(data['pin'],False)
        return response

    def offDevice(self,data):
        GPIO.setup(data['pin'], GPIO.OUT)
        GPIO.output(data['pin'],True)
        return response




