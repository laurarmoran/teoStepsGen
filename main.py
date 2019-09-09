'''''
 Embedding matplotlib: https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
 Grid manager (text,buttons,image): https://effbot.org/tkinterbook/grid.htm
 Every widget: https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/all
'''''

import tkinter
from tkinter import *
#from tkinter.ttk import *
import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from footprints_generation import *


''''
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.NONE, expand=0)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)
'''''


class TeoStepsGen:

    def __init__(self, root):
        self.label_font = tkFont.Font(family='Helvetica', size=50)
        self.button_font = tkFont.Font(family='Helvetica', size=20)

        self.teoStepsGen = Label(root, text="TEO Steps Generator", font= self.label_font)
        self.teoStepsGen.grid(row=0, column=0, sticky=W+E)
        self.teoStepsGen.grid_columnconfigure(0, weight=1)

        self.footprintsGenButton = Button(root, text="Footprints Generation", command=self.footprintsGen_clicked, font=self.button_font)
        self.footprintsGenButton.grid(row=6, column=0, sticky=W + E)

        self.stepsGenButton = Button(root, text="Steps Generation", command=self.stepsGen_clicked, font=self.button_font)
        self.stepsGenButton.grid(row=7, column=0, sticky=W + E)


    def footprintsGen_clicked(self):
        window = Tk()
        footprints_generation(window)
        window.title("Footprints Generation")
        window.geometry("898x553")

    def stepsGen_clicked(self):
        window = Tk()
        footprints_generation(window)
        window.title("Steps Generation")
        window.geometry("898x553")
        window.mainloop()

def main():
    root = Tk()
    TeoStepsGen(root)
    root.title("TEO Steps Generator")
    root.geometry("600x300")

    root.mainloop()


if __name__ == '__main__':
    main()
