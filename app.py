from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML page to connect to the WebSocket server
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Temperature</title>
    </head>
    <body>
        <h1>WebSocket Temperature Monitor</h1>
        <pre id="temperature"></pre>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                document.getElementById("temperature").textContent = event.data;
            };
        </script>
    </body>
</html>
"""

@app.get("/")
def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            print(f"Received data: {data}")
            # Optionally broadcast to all connected clients
            # for client in websocket.app.websocket_connections:
            #     if client is not websocket:
            #         await client.send_text(data)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

