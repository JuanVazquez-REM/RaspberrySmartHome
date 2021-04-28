from websocket import create_connection
import json
from Dispositivos import Dispositivo
from Sensores import Sensores 
import RPi.GPIO as GPIO

def conexion_adonis():
    ws = create_connection("ws://54.146.120.131:3333/adonis-ws") #Se enlaza al socket

    ws.send(json.dumps({ #me uno al canal
        "t":1,
        "d": {
            "topic":"wstemp",
        }
    }))

    print("respuesta al conectarme al canal")
    print(ws.recv())

    ws.send(json.dumps({ #despues realizo un evento en el canal, es decir envio en un mensaje
        "t":7,
        "d": {
            "topic":"wstemp",
            "event":"message"
        }
    }))
    print("Respesta despues de enviar mensaje")
    print(ws.recv())
    espera = True

    #print("Listo para enviar temperatura...")
    try:
        while True:
            if(espera):
                print("Esperando Respuesta de angular....")
                messageJson = ws.recv()
                messageDecoder = json.loads(messageJson)
                data = messageDecoder['d']['data']
            
            if(data['tipo'] == "Temperatura_Humedad"):
                espera = False
                sensor = Sensores()
                response = sensor.sensor(data)
                print("Sensor registrado: ")
                print(response)
                ws.send(json.dumps({ #despues realizo un evento en el canal, es decir envio en un mensaje
                    "t":7,
                    "d": {
                        "topic":"wstemp",
                        "event":"message",
                        "data":response['temperatura']
                    }
                })) 
    except: 
        print("conexion perdida")
        conexion_adonis()
        print("Estableciendo conexion...")
    finally:
        GPIO.cleanup() 

conexion_adonis()

