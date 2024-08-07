# web_socket_server.py

import asyncio
import websockets

async def receive_temperature(websocket, path):
    async for message in websocket:
        print(f"Received temperature: {message}")

start_server = websockets.serve(receive_temperature, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
