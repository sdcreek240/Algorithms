
from tkinter import *
from tkinter import ttk

import pandas as pd
import time

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from metaInterface import timeframe_map
from metaInterface import mt5


class debugApp:    

    def LeftFrame(self):
        
        self.frmLeft = Frame(self.root, bg="#32414e", bd=10, cursor="dot", width=240, height=890)
        self.frmLeft.grid(row=0, column=0, sticky="ns")
        self.frmLeft.grid_propagate(False)

        #Make column 0 expandable
        self.frmLeft.grid_columnconfigure(0, weight=1)

        self.frmSample = Frame(self.frmLeft, bg="#74d1c9", bd=5, height=50, width=230)
        self.frmSample.grid(row=0, column=0)

        #Define list for symbol
        self.symbols = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"]

        self.cmbSymbol = ttk.Combobox(self.frmSample, values=self.symbols, width=8, cursor="dot")
        self.cmbSymbol.set(self.symbols[0])
        self.cmbSymbol.grid(row=0, column=0, padx=5)

        #Define timeframe map
        self.timeframe_map = timeframe_map

        self.cmbTimeframe = ttk.Combobox(self.frmSample, values=list(self.timeframe_map.keys()), width=8, cursor="dot")
        self.cmbTimeframe.grid(row=0, column=2, padx=5)
        self.cmbTimeframe.set("5M")

        #Create Button to fetch live Data
        self.btnFetchLive = Button(self.frmSample, text="Live", width=4, height=2, 
                              command=self.FetchLive,
                              font=("Terminal", 10, "bold"))
        self.btnFetchLive.grid(row=1, column=1, padx=5)

        #Figure out how to retrieve values from comboboxes and write function to plot chart of data fetched

    def LiveFrame(self):

        self.frmLive = Frame(self.root, bg="#32414e", bd=10, width=1345, height = 350)
        self.frmLive.grid(row=0, column=1, padx=5, sticky="n")
        self.frmLive.grid_propagate(False)

        # Prepare matplotlib figure
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Live Chart")
        self.canvas = FigureCanvasTkAgg(self.figure, self.frmLive)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    def FetchLive(self):

        symbol = self.cmbSymbol.get()
        timeframe = self.timeframe_map.get(self.cmbTimeframe.get())

        def updateChart():
            rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)
            if rates is not None:
                df = pd.DataFrame(rates)
                df['time'] = pd.to_datetime(df['time'], unit='s')

                if not hasattr(self, 'line'):  # Create the plot initially
                    self.line, = self.ax.plot(df['time'], df['close'], label="Price")
                    self.ax.legend()
                    self.ax.set_title(f"{symbol} Live Chart")
                    self.ax.set_xlabel("Time")
                    self.ax.set_ylabel("Price")
                else:  # Update data without clearing
                    self.line.set_data(df['time'], df['close'])
                    self.ax.relim()
                    self.ax.autoscale_view()

                self.canvas.draw()

            # Repeat update every 500ms (half second)
            self.frmLive.after(500, updateChart)

        # Add a toolbar for zoom/pan/reset functionality
        toolbar = NavigationToolbar2Tk(self.canvas, self.frmLive)
        toolbar.update()
        toolbar.pack(side=TOP, fill=X)

        updateChart()

    def __init__(self, root):
        print("---Entry_debugApp---")

        self.root = root
        

        self.LeftFrame()
        self.LiveFrame()



        self.root.mainloop()



if __name__=="__main__":

    root = Tk()

    root.title("Debug Application")
    root.geometry("1600x900+175+50")
    root.attributes("-alpha", 0.9)
    root.config(bg="grey", bd=5)

    app = debugApp(root)