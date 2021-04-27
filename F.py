from websocket import create_connection
import json
from Dispositivos import Dispositivo
import RPi.GPIO as GPIO


def conexion_adonis():
    ws = create_connection("ws://54.146.120.131:3333/adonis-ws") #Se enlaza al socket

    ws.send(json.dumps({ #me uno al canal
        "t":1,
        "d": {
            "topic":"wsfoco",
        }
    }))

    print("respuesta al conectarme al canal")
    print(ws.recv())

    ws.send(json.dumps({ #despues realizo un evento en el canal, es decir envio en un mensaje
        "t":7,
        "d": {
            "topic":"wsfoco",
            "event":"message"
        }
    }))
    print("Respesta despues de enviar mensaje")
    print(ws.recv())


    #print("Listo para enviar temperatura...")
    try:
        while True:
            print("Esperando accion...")
            messageJson = ws.recv()
            print(messageJson)
            messageDecoder = json.loads(messageJson)
            data = messageDecoder['d']['data'] 

            foco = Dispositivo(data)
            print(foco)
            print("Accion completada")
    except: 
        print("conexion perdida")
        conexion_adonis()
        print("Estableciendo conexion...")
    finally:
        GPIO.cleanup()  

conexion_adonis()

