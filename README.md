# delta-trader: Project 2 Team 6

# Summary
Warren Buffett recently claimed in the 2021 Berkshire Hathaway Annual Shareholders' Meeting that "the best thing to do is to buy 90% in an S&P 500 Index Fund." The wisdom behind the sentiment that one should passively invest in a broad index of stocks such as the SPY is due to the difficulty of truly beating average market returns.

We wanted to put this claim to the test to see if the best thing to do is to either simply buy and hold an index fund such as the SPY, or attempt to trade the SPY with two different algorithmic strategies which are listed below:

* Algorithmic Applied Faber’s Ivy Portfolio with signals based on 10 month moving average (200 day SMA), with trading being executed on the last trading day of the month. This ensures that our algorithm doesn't trade too often and remains more tax efficient. This strategy is inspired by the following article: https://www.newtraderu.com/2021/01/16/200-day-moving-average-strategy-that-beats-buy-and-hold/

* An algorithmic strategy using an LSTM neural network to predict prices in advance where we would buy or sell based on our LSTM model’s prediction of the next day’s closing price.

# Team Members

* Rina Niles
* Kamil Wojnowski
* Rafael Sy
* Rikin
* Chandra Kandiah

# Dataset sources used
* Yahoo finance
* PyAlgoTrade
* Alpaca
* Backtrader
* Blueshift

# Evaluation of the 200 Moving Average 

# Evaluation of the LSTM stock predictor strategy



