
from tkinter import *
from tkinter import ttk

import pandas as pd

from metaInterface import timeframe_map


class debugApp:    

    def LeftFrame(self):
        
        frmLeft = Frame(root, bg="#32414e", bd=10, cursor="dot", width=225, height=1600)
        frmLeft.grid(row=0, column=0, padx=5, sticky="ns")
        frmLeft.grid_propagate(False)

        #Make column 0 expandable
        frmLeft.grid_columnconfigure(0, weight=1)

        frmSample = Frame(frmLeft, bg="#74d1c9", bd=5, height=50, width=225)
        frmSample.grid(row=0, column=0)

        #Define list for symbol
        self.symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"]

        self.cmbSymbol = ttk.Combobox(frmSample, values=self.symbols, width=8, cursor="dot")
        self.cmbSymbol.set(self.symbols[0])
        self.cmbSymbol.grid(row=0, column=0, padx=5)

        #Define timeframe map
        self.timeframe_map = timeframe_map

        self.cmbTimeframe = ttk.Combobox(frmSample, values=list(self.timeframe_map.keys()), width=5, cursor="dot")
        self.cmbTimeframe.grid(row=0, column=2, padx=5)
        self.cmbTimeframe.set("5M")

        #Create Button to fetch live Data
        self.btnFetchLive = Button(frmSample, text="Live", width=4, height=2, 
                              command=self.FetchLive)
        self.btnFetchLive.grid(row=1, column=1)

        #Figure out how to retrieve values from comboboxes and write function to plot chart of data fetched

    def FetchLive(self):

        symbol = self.cmbSymbol.get()
        timeframe = self.timeframe_map.get(self.cmbTimeframe.get())

        print(timeframe)

    def __init__(self, root):
        print("---Entry_debugApp---")

        self.root = root

        self.LeftFrame()



        self.root.mainloop()



if __name__=="__main__":

    root = Tk()

    root.title("Debug Application")
    root.geometry("1600x900+175+50")
    root.attributes("-alpha", 0.6)
    root.config(bg="grey")

    app = debugApp(root)