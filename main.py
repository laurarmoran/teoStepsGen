
from tkinter import *
import tkinter.font as tkFont

from footprints_generation import *
from steps_generation import *


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
        self.labelFont = tkFont.Font(family='Helvetica', size=50)
        self.buttonFont = tkFont.Font(family='Helvetica', size=20)

        self.teoStepsGen = Label(root, text="TEO Steps Generator", font= self.labelFont)
        self.teoStepsGen.grid(row=0, column=0, columnspan=3, sticky=W+E)

        self.footprintsGenButton = Button(root, text="Footprints Generation", command=self.footprintsGen_clicked, font=self.buttonFont)
        self.footprintsGenButton.grid(row=6, column=1, sticky=W+E)

        self.stepsGenButton = Button(root, text="Steps Control", command=self.stepsGen_clicked, font=self.buttonFont)
        self.stepsGenButton.grid(row=7, column=1, sticky=W+E)

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
    root.geometry("600x300")

    root.mainloop()


if __name__ == '__main__':
    main()
