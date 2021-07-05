import json
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import asyncio
import websocket
from pprintpp import pprint as pp

load_dotenv('/Users/kamilwojnowski/Fintech/keys.env')

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
base_url = 'wss://paper-api.alpaca.markets/stream'

alpaca_stream_output = []

# Authentication and listener setup function
def on_open(ws):
    auth_data = {
        "action": "authenticate",
        "data": {
            "key_id": alpaca_api_key, 
            "secret_key": alpaca_secret_key
        }
    }
    ws.send(json.dumps(auth_data))
    print('open')

    listen_message = {
            "action": "listen", 
            "data": {
                "streams": ["trade_updates"]
            }
        }
    ws.send(json.dumps(listen_message))
    print("listening...")
    
# Receives and prints incoming messages from server
def on_message(ws, message_server):
    json_message = json.loads(message_server)
    pp(json_message)

def on_cont_message(ws, message_server, continueflag=0):
    json_message = json.loads(message_server)
    pp(json_message)
    alpaca_stream_output.append(json_message)
    
    
# Error handler
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("connection closed")

# websocket-client library function
ws = websocket.WebSocketApp(base_url, on_open=on_open, on_message=on_message, on_cont_message=on_cont_message, on_error=on_error, on_close=on_close)
ws.run_forever()
