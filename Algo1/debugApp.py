
from tkinter import *
from tkinter import ttk

import pandas as pd
import time

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from metaInterface import timeframe_map, symbols
from metaInterface import mt5

import tkinter as tk

import mplfinance as mpf

class debugApp:    

    def centerWindow(self):
        
        self.root.update_idletasks()

        # width = self.root.winfo_width()#Retireve current width of the root window
        # height = self.root.winfo_height()
        width = 1500
        height = 750

        screenW = self.root.winfo_screenwidth()
        screenH = self.root.winfo_screenheight()

        x = (screenW - width) // 2#Division with truncation
        y = ((screenH - height) // 2) - 50

        self.root.geometry(f"{width}x{height}+{x}+{y}")
        # self.root.state("zoomed")#Windowed full screen

    def LeftFrame(self):
        
        self.frmLeft = Frame(self.root, bg="#32414e", bd=10, cursor="dot", width=240, height=890)
        self.frmLeft.grid(row=0, column=0, sticky="ns")
        self.frmLeft.grid_propagate(False)

        #Make column 0 expandable
        self.frmLeft.grid_columnconfigure(0, weight=1)

        self.frmSample = Frame(self.frmLeft, bg="#74d1c9", bd=5, height=50, width=230)
        self.frmSample.grid(row=0, column=0)

        #Define list for symbol
        self.symbols = symbols

        self.cmbSymbol = ttk.Combobox(self.frmSample, values=self.symbols, width=8, cursor="dot")
        self.cmbSymbol.set(self.symbols[0])
        self.cmbSymbol.grid(row=0, column=0, padx=5)

        #Define timeframe map
        self.timeframe_map = timeframe_map

        self.cmbTimeframe = ttk.Combobox(self.frmSample, values=list(self.timeframe_map.keys()), width=8, cursor="dot")
        self.cmbTimeframe.grid(row=0, column=1, padx=5)
        self.cmbTimeframe.set("5M")

        #Add Line/candleStick option and boolVar for comparing bool val
        self.isLineChart = BooleanVar(self.root)
        self.isLineChart.set(True)
        
        self.chkLine = Checkbutton(self.frmSample, fg="teal", text="Line chart", 
                                    variable=self.isLineChart, 
                                    onvalue=True, offvalue=False,
                                    width=8)
        self.chkLine.grid(row=1, column=0)

        #Create Button to fetch live Data
        self.btnGenerate = Button(self.frmSample, text="Generate", width=8, height=2, 
                              command=self.FetchLive,
                              font=("Terminal", 10, "bold"))
        self.btnGenerate.grid(row=2, column=0)

        #Create Button to clear chart
        self.btnClear = Button(self.frmSample, text="Clear", width=8, height=2, 
                                font=("Terminal", 10, "bold"))
        self.btnClear.grid(row=2, column=1)

    def LiveFrame(self):

        self.frmLive = Frame(self.root, bg="#32414e", bd=10, width=1345, height = 350)
        self.frmLive.grid(row=0, column=1, padx=5, sticky="n")
        self.frmLive.grid_propagate(False)

        # Prepare matplotlib figure
        self.figure = Figure(figsize=(8, 6), dpi=100)#Create matplot figure - figsize(width", height") | dpi- sets resolution
        self.ax = self.figure.add_subplot(111)#Add plot to figure - 1row | 1col | 1st plot
        self.ax.set_title(f"Live Chart")
        self.canvas = FigureCanvasTkAgg(self.figure, self.frmLive)#Embed matplotlib into tk widget
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
            
    def FetchLive(self):

        symbol = self.cmbSymbol.get()
        timeframe = self.timeframe_map.get(self.cmbTimeframe.get())

    def __init__(self, root):
        print("---Entry_debugApp---")

        self.root = root
        
        self.LeftFrame()
        self.LiveFrame()

        self.centerWindow()

        self.root.mainloop()

from main import *

if __name__=="__main__":
    bootMain()