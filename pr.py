import asyncio
import websockets
import json

async def hello():
    uri = "ws://127.0.0.1:3333/adonis-ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("1")
        greeting = await websocket.recv()
        print(f"< {greeting}")

        await websocket.send(json.dumps({ #me uno al canal
            "t":1,
            "d": {
                "topic":"wstemp",
            }
        }))
        greeting = await websocket.recv()
        print(f"< {greeting}")

        name = input("What's your name? ")
        await websocket.send(name)
        print(f"> {name}")

while True :
    asyncio.get_event_loop().run_until_complete(hello())