
from tkinter import *
import tkinter.font as tkFont

from footprints_generation import *
from steps_generation import *
#from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


class TeoStepsGen:

    def __init__(self, root):
        self.labelFont = tkFont.Font(family='Helvetica', size=50)
        self.buttonFont = tkFont.Font(family='Helvetica', size=20)

        self.teoStepsGen = Label(root, text="TEO Steps Generator", font= self.labelFont)
        self.teoStepsGen.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.footprintsGenButton = Button(root, text="Footprints Generation", command=self.footprintsGen_clicked, font=self.buttonFont)
        self.footprintsGenButton.grid(row=3, column=1, sticky=W+E)

        self.stepsGenButton = Button(root, text="Steps Control", command=self.stepsGen_clicked, font=self.buttonFont)
        self.stepsGenButton.grid(row=4, column=1, sticky=W+E)

        # Adding photo to main window
        img = PhotoImage(file="img/teo.pgm")
        label = Label(image=img)
        label.image = img
        label.grid(row=0, column=4, rowspan=8, sticky=E)


    def footprintsGen_clicked(self):
        window = Tk()
        footprintsGeneration(window)
        window.title("Footprints Generation")
        window.geometry("898x553")

    def stepsGen_clicked(self):
        window = Tk()
        stepsGeneration(window)
        window.title("Steps Generation")
        window.geometry("498x253")

def main():
    root = Tk()
    TeoStepsGen(root)
    root.title("TEO Steps Generator")
    root.geometry("650x300")

    root.mainloop()


if __name__ == '__main__':
    main()
