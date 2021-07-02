# Initial imports
import os
import requests
import pandas as pd
import requests
import json
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import schedule, time
from pandas.tseries.offsets import BMonthEnd
import numpy as np
from datetime import datetime


# Get today's date
now = datetime.now()

# Load .env enviroment variables
load_dotenv("keys.env")

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Create the Alpaca API object
api = tradeapi.REST(
    "PKCDUIK3A26QFLD91IKP",
    "qebqNI6jVY8TzRPbmOnSY3kuNcPlGrHIVyaJllwp",
    "https://paper-api.alpaca.markets"
)

# Get account
account = api.get_account()


# Define the function that holds all the logic and will run once a day
def exec_trade():
    offset = BMonthEnd()
    last_day=offset.rollforward(DATE)
    barset = api.get_barset('SPY', 'day', limit=200)
    SPY_closes = [bar.c for bar in barset["SPY"][:]]
    SMA = np.mean(SPY_closes)
    current_price = SPY_closes[-1]
    portfolio = api.list_positions()
    open_position = False
    if "SPY" in portfolio:
        open_position=True
    if(now.date()==last_day):
        if((current_price > SMA) and (open_position)):
            api.submit_order(symbol="SPY", notional = cash_in_account, type="market")
        elif((SMA>current_price) and (not open_position)):
            api.submit_order(symbol, portfolio["SPY"].qty , 'sell', 'market', 'gtc')
            

# Set Schedule
schedule.every().day.at("14:20").do(exec_trade)


# Run the loop forever
while True:
    schedule.run_pending()
    time.sleep(1)