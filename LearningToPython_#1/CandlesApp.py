import tkinter as tk
from tkinter import ttk
import MetaTrader5 as mt5
import pandas as pd
from Candles import Candles
from PIL import Image, ImageTk

class CandlesApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Candles Fetcher")
        
        # Load the background image
        img_path = "Algorithms\\LearningToPython_#1\\Images\\getCandlesBg.jpg"
        img = Image.open(img_path)
        self.bg_image = ImageTk.PhotoImage(img)

        # Set the background image for the whole window (root)
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.image = self.bg_image  # Keep a reference to the image object
        self.bg_label.place(relwidth=1, relheight=1)  # Ensure the image fills the whole window

        # Create a panel/frame to group the components (optional, if you still want grouping)
        self.panel = tk.Frame(root)  # Set light background color for panel (optional)
        self.panel.place(relx=0.5, rely=0.5, anchor="center")  # Center the panel in the window
        
        # Pre-defined lists for symbol
        self.symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"]
        
        # Define mapping of user-friendly labels to timeframe constants
        self.timeframe_map = {
            "5M": mt5.TIMEFRAME_M5,
            "15M": mt5.TIMEFRAME_M15,
            "30M": mt5.TIMEFRAME_M30,
            "1H": mt5.TIMEFRAME_H1,
            "4H": mt5.TIMEFRAME_H4,
            "1D": mt5.TIMEFRAME_D1
        }

        # Create input fields and widgets on top of the background image
        self.symbol_label = tk.Label(self.panel, text="Symbol:")  # Set bg color for labels
        self.symbol_label.grid(row=1, column=0, padx=5, pady=5)

        self.symbol_combobox = ttk.Combobox(self.panel, values=self.symbols)
        self.symbol_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.symbol_combobox.set(self.symbols[0])  # Default selection

        self.timeframe_label = tk.Label(self.panel, text="Timeframe:")
        self.timeframe_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.timeframe_combobox = ttk.Combobox(self.panel, values=list(self.timeframe_map.keys()))
        self.timeframe_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.timeframe_combobox.set("5M")  # Default selection

        self.n_label = tk.Label(self.panel, text="Number of Candles:")
        self.n_label.grid(row=3, column=0, padx=5, pady=5)
        
        self.n_entry = tk.Entry(self.panel)
        self.n_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Fetch button
        self.fetch_button = tk.Button(self.panel, text="Fetch Candles", command=self.fetch_candles)
        self.fetch_button.grid(row=4, column=0, columnspan=2, pady=5)

    def fetch_candles(self):
        symbol = self.symbol_combobox.get()  # Get selected symbol
        timeframe_label = self.timeframe_combobox.get()  # Get selected timeframe label
        timeframe = self.timeframe_map.get(timeframe_label)  # Get selected timeframe
        n = int(self.n_entry.get())  # Get number of candles
        
        # Initialize Candles class and display
        myCandles = Candles(symbol, timeframe, n)
        print(myCandles)

