from websocket import create_connection
from chat_ui import ports

def send_to_ui(what):
    ws = create_connection("ws://127.0.0.1:%d" % ports.ports["chat_ui_server_ws_port"])
    ws.send(what)
    ws.close()
