from websocket import create_connection
import json
import RPi.GPIO as GPIO
from Dispositivos import Dispositivo

def conexion_adonis():
    ws = create_connection("ws://54.146.120.131:3333/adonis-ws")

    ws.send(json.dumps({ #me uno al canal
        "t":1,
        "d": {
            "topic":"wstemp",
        }
    }))
    print("respuesta al conectarme al canal")
    print(ws.recv())
    ws.send(json.dumps({ #despues realizo un evento en el canal
        "t":7,
        "d": {
            "topic":"wstemp",
            "event":"message",
            "data":"Hola aws"
        }
    }))
    print("respuesta al conectarme al channel y enviar un mensaje")
    print(ws.recv())

    print("recibiendo mensajes...")
    try:
        
        while True:
            result = ws.recv()
            result = json.loads(result)
            print ("Recibidos: ")
            data = result['d']['data']
            print(data)
            #Foco = Dispositivo()
        


    except: 
        print("conexion perdida")
        conexion_adonis()
        print("Estableciendo conexion...")

