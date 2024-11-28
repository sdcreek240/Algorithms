from metaInterface import *

import tkinter as tk

from debugApp import *

def initDebugApp():

    try:
        root = tk.Tk()
        root.title("Debug Application")
        root.geometry("1600x900+175+50")
        root.attributes("-alpha", 0.8)
        root.config(bg="grey")
        # root.resizable(False)

        app = debugApp(root)
        
    except Exception as e:
        print(f"Error initializing Debug Application: {e}")





if __name__ == "__main__":
    
    print("Ek is n nar")

    initMT5()

    initDebugApp()

