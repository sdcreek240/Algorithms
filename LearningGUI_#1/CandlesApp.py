
from tkinter import *
import MetaTrader5 as mt5
import pandas as pd
from Candles import Candles
from PIL import Image, ImageTk

class CandlesApp:

    def __init__(self, root):

        #Define list for symbol
        self.symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"]

        #Define map for timeframe
        self.timeframe_map = {
            "5M": mt5.TIMEFRAME_M5,
            "15M": mt5.TIMEFRAME_M15,
            "30M": mt5.TIMEFRAME_M30,
            "1H": mt5.TIMEFRAME_H1,
            "4H": mt5.TIMEFRAME_H4,
            "1D": mt5.TIMEFRAME_D1
        }

        #Create Label in root
        text = Label(root, text="Nothing will work unless you do.")
        text.pack()#Fit Size of window to text (--Packs a widget in the parent window)
        text2 = Label(root, text="- Maya Angelou")
        text2.pack()

        #Load image
        # image = PhotoImage(file="Algorithms\LearningGUI_#1\Images\something.gif")#Only loads GIF/PGM/PPC
        # img = Label(root, image=image)
        # img.pack()

        #Use pillow to import png/jpeg/gif
        #(Open image) -> Convert for Tkinter
        image = ImageTk.PhotoImage(Image.open("Algorithms/LearningGUI_#1/Images/getCandlesBg.jpg"))
        img = Label(root, image=image)
        # image = img.resize((50,50), Image.ANFI)
        img.image = image #Keep reference to avoid garbage collection
        img.pack()




        




