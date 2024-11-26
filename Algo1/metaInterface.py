import MetaTrader5 as mt5

#import config file
import sys
import os

# Add the MT5 directory to sys.path (it's located one level up from Project)
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'MT5'))

import config

timeframe_map = {
            "5M": mt5.TIMEFRAME_M5,
            "15M": mt5.TIMEFRAME_M15,
            "30M": mt5.TIMEFRAME_M30,
            "1H": mt5.TIMEFRAME_H1,
            "4H": mt5.TIMEFRAME_H4,
            "1D": mt5.TIMEFRAME_D1
        }

#Initialize MetaTrader5 connection
def initMT5():

    if not mt5.initialize(login=config.MT5_LOGIN, password=config.MT5_PASSWORD, server=config.MT5_SERVER):
        print("Failed to initialize MT5, error code:", mt5.last_error())
        quit()