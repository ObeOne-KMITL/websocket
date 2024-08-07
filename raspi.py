import asyncio
import websockets

def read_temperature();
    voltage = adc.value*3.3
    temperature = voltage*100
    return temperature 

async def send_temperature():
    uri = "ws://<YOUR_SERVER_IP>:<PORT>"  # Replace with your WebSocket server address and port

    async with websockets.connect(uri) as websocket:
        while True:
                temp = read_temperature()
                message = f"Temperature: {temperature:.2f}°C"
                await websocket.send(message)
                print(f"Sent: {message}")
                await asyncio.sleep(5)  # Adjust the delay as needed

if __name__ == "__main__":
asyncio.get_event_loop().run_until_complete(send_temperature())
