
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

from tabulate import tabulate

#Define colors for output formatting
COLOR_OPEN = '\033[92m'#Green
COLOR_CLOSE = '\033[94m'#Blue
COLOR_HIGH = '\033[93m'#Yellow
COLOR_LOW = '\033[91m'#Red
COLOR_RESET = '\033[0m'#Reset color

class Candles:

    def __init__(self, symbol, timeframe, n):
        
        #Initialise member variables
        self.symbol = symbol
        self.timeframe = timeframe
        self.n = n
        self.candles = []

        #Call fetchCandles() to populate candles
        self.fetchCandles()

    #Fetch Candle data and populate candles member variable with it
    def fetchCandles(self):

        #Fetch n candles data
        rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, self.n)

        #Check if candles were fetched
        if rates is None:
            print(f"Failed to fetch candles for {self.symbol}. Error: ", mt5.last_error())
            return
        
        #Create Pandas DataFrame - Easier Processing
        self.candles = pd.DataFrame(rates)
        self.candles['time'] = pd.to_datetime(self.candles['time'], unit='s')#Specifies that data already in frame time column is in seconds and should be converted to date time

        

    #Define string representation of Candles object
    def __repr__(self):
        return f"Candles[{self.symbol}]\n{self.candles[['time', 'open', 'high', 'low', 'close']]}"

        
