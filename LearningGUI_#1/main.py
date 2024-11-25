
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
from tkinter import * #Bad practice to import * / rather import as variable

#Define function to Initialize MetaTrader 5 connection
def InitMT5():
    if not mt5.initialize(login=config.MT5_LOGIN, password=config.MT5_PASSWORD, server=config.MT5_SERVER):
        print("Failed to initialize MT5, error code:", mt5.last_error())
        quit()

#Define function to initialize and create root window
def initWindow():

    #Initialize connection to MT5
    InitMT5()

   # Create main window - root
    root = Tk()
    root.title("LearningGUI_#1_root")

    #Make root window bigger
    root.geometry("1600x900+50+50")#Width * height + x + y

    #Make root window windowed fullscreen
    root.state("zoomed")

    #Set transparency
    root.attributes("-alpha", 0.9)

    #Set baclground color
    # root.configure(background="yellow")
    root.config(bg="dark grey")

    #Set min size and max size
    # root.minsize(200, 200)#Min size
    # root.maxsize(500, 500)#Max size

    # Set up app
    app = CandlesApp(root)

def main():
    print("Ek is n nar?")

    initWindow()

if __name__ == "__main__":#Ensure script runs properly - Ensures it doesn't auto run somewhere else
    main()








