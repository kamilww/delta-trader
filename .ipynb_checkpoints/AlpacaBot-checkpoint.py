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


# Load .env enviroment variables
load_dotenv("keys.env")

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Create the Alpaca API object
api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    "https://paper-api.alpaca.markets"
)



# Define the function that holds all the logic and will run once a day
def exec_trade():
    now = datetime.now().date()
    account = api.get_account()
    cash = int(float(account.cash))
    offset = BMonthEnd()
    last_day=offset.rollforward(now)
    barset = api.get_barset('SPY', 'day', limit=200)
    SPY_closes = [bar.c for bar in barset["SPY"][:]]
    SMA = np.mean(SPY_closes)
    current_price = int(SPY_closes[-1])
    positions = api.list_positions()
    portfolio = [position.symbol for position in positions]
    open_position = False
    spy_qty = 0
    if [position for position in api.list_positions() if position.symbol=="SPY"]:
        spy_qty= int([position.qty for position in api.list_positions() if position.symbol=="SPY"][0])
        
    if "SPY" in portfolio:
        open_position=True
    if(now.date()==last_day):
        if((current_price > SMA) and (open_position)):
            api.submit_order(symbol="SPY", qty = int(cash/current_price), type="market", side="buy", time_in_force="gtc")
        elif((SMA>current_price) and (not open_position)):
            api.submit_order(symbol="SPY", qty=spy_qty, type="market", side="sell", time_in_force="gtc")
            

# Set Schedule
def running_print():
    print("Hello your bot is running")

schedule.every(10).seconds.do(running_print)
schedule.every().day.at("14:20").do(exec_trade)


# Run the loop forever
while True:
    schedule.run_pending()
    time.sleep(1)