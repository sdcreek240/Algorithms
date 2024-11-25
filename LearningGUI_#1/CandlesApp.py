
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
        # text = Label(root, text="Nothing will work unless you do.")
        # text.pack()#Fit Size of window to text (--Packs a widget in the parent window)
        # text2 = Label(root, text="- Maya Angelou")
        # text2.pack()

        #Load image
        # image = PhotoImage(file="Algorithms\LearningGUI_#1\Images\something.gif")#Only loads GIF/PGM/PPC
        # img = Label(root, image=image)
        # img.pack()

        #Use pillow to import png/jpeg/gif

        #(Open image) -> Convert for Tkinter
        # image = ImageTk.PhotoImage(Image.open("Algorithms/LearningGUI_#1/Images/getCandlesBg.jpg"))
        # img = Label(root, image=image)
        # img.image = image #Keep reference to avoid garbage collection
        # img.pack()


        #Desing Layout

        #Create Frame Widget
        leftFrame = Frame(root, width=200, height=400, bg="grey")#Set leftFrame as part of root window -> specify width & height
        leftFrame.grid(row=0, column=0, padx=10, pady=5)#Place leftFrame in root widow using grid() -> position like excel -> padding around widget

        # #Create Frame within leftFrame
        # toolBar = Frame(leftFrame, width=180, height=185, bg="cyan", bd=5, cursor="dot") # - Notice how leftWindow resizes to match children - bd=border - cursor=dot/arrow/circle
        # toolBar.grid(row=2, column=0, padx=5, pady=5)

        # #Create Label above toolBar
        # Label(leftFrame, text="Ek is n nar").grid(row=1, column=0, padx=5, pady=5)

        #Create rFrame
        rFrame = Frame(root, width=650, height=400, bg="grey")
        rFrame.grid(row=0, column=1, padx=10, pady=5)

        #Create Frames and Labels in leftFrame
        Label(leftFrame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

        #Load image to be 'edited'
        image = PhotoImage(file="Algorithms/LearningGUI_#1/Images/Large.gif")
        originalImage = image.subsample(3,3) #Resize image using subsample
        Label(leftFrame, image=originalImage).grid(row=1, column=0, padx=5, pady=5)

        #Display image in rFrame
        Label(rFrame, image=image).grid(row=0, column=0, padx=5, pady=5)

        #Create toolBar Frame
        tbFrame = Frame(leftFrame, width=180, height=185)
        tbFrame.grid(row=2, column=0, padx=5, pady=5)

        #Example Labels
        Label(tbFrame, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(tbFrame, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

        # Example labels that could be displayed under the "Tool" menu
        Label(tbFrame, text="Select").grid(row=1, column=0, padx=5, pady=5)
        Label(tbFrame, text="Crop").grid(row=2, column=0, padx=5, pady=5)
        Label(tbFrame, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
        Label(tbFrame, text="Resize").grid(row=4, column=0, padx=5, pady=5)
        Label(tbFrame, text="Exposure").grid(row=5, column=0, padx=5, pady=5)

        #BUTTONS
        turnOn = Button(leftFrame, text="ON", width=10, height=5).grid(row=3, column=0, ipadx=5, ipady=10)
        tournOff = Button(leftFrame, text="Terminate", width=10, height=5, command=root.quit, bg="red", font="fsBold").grid(row=3, column=1, ipadx=5, ipady=10)#?

        #Define volume functions:
        def printNar():
            print("Ek is n nar")

        printNarButton = Button(leftFrame, text="Wie is n nar?", width=10, height=5, bg="blue", command=printNar).grid(row=2, column=1, ipadx=5, ipady=10)

        #Button parameters:
        #activebackground & activeforeground: set back&fore-ground colors when cursor is over button
        #bd - sets border in pixels
        #bg & fg - set back- & foreground
        #font - choose text font for button !!
        #image - ise image as button rather than text


        root.mainloop()
      


from main import *

if __name__ == "__main__":#Run CandlesApp only with initWondow from main
    initWindow()