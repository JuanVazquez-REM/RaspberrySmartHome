from websocket import create_connection
import json
from Dispositivos import Dispositivo
from Sensores import Sensores

def conexion_adonis():
    data={'sensor': "TEMPERATURA_HUMEDAD",'tipo':"DHT11",'pin': 14} #Diccionario del sensor temperartura
    ws = create_connection("ws://54.146.120.131:3333/adonis-ws") #Se enlaza al socket

    ws.send(json.dumps({ #me uno al canal
        "t":1,
        "d": {
            "topic":"wstemp",
        }
    }))
    print("respuesta al conectarme al canal")
    print(ws.recv())
    """ print("respuesta al conectarme al channel y enviar un mensaje")
    print(ws.recv()) """

    print("Listo para enviar temperatura...")
    try:
        while True:
            sensor = Sensores(data)
            print("Temperatura: "+ sensor['message']['temperatura'])
            ws.send(json.dumps({ #despues realizo un evento en el canal, es decir envio en un mensaje
                "t":7,
                "d": {
                    "topic":"wstemp",
                    "event":"message",
                    "data":sensor['message']['temperatura']
                }
            }))
            #Foco = Dispositivo()
        
    except: 
        print("conexion perdida")
        conexion_adonis()
        print("Estableciendo conexion...")


def prueba():
    data={'sensor': "TEMPERATURA_HUMEDAD",'tipo':"DHT11",'pin': 14} #Diccionario del sensor temperartura
    sensor = Sensores()
    sensor.sensor(data)
    print("Temperatura: "+ sensor['message']['temperatura'])

prueba()

