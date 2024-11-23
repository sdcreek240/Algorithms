
from Candles import Candles # Import Candles class

import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

#import config file
import sys
import os

# Add the MT5 directory to sys.path (it's located one level up from Project)
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'MT5'))

import config

#Import GUI class
from CandlesApp import CandlesApp
import tkinter as tk

#Define function to Initialize MetaTrader 5 connection
def InitMT5():
    if not mt5.initialize(login=config.MT5_LOGIN, password=config.MT5_PASSWORD, server=config.MT5_SERVER):
        print("Failed to initialize MT5, error code:", mt5.last_error())
        quit()

#Define function to initialize and create root window
def initWindow():

    #Initialize connection to MT5
    InitMT5()

    #Create main window - root
    root = tk.Tk()
    app = CandlesApp(root)

    #Set dimensions of root window
    root.geometry("500x400")

    #Start tinker event loop
    root.mainloop()

def main():
    print("Ek is n nar?")

    initWindow()

if __name__ == "__main__":#Ensure script runs properly - Ensures it doesn't auto run somewhere else
    main()








