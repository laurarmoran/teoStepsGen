
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
        self.label_font = tkFont.Font(family='Helvetica', size=50)
        self.button_font = tkFont.Font(family='Helvetica', size=20)

        self.teoStepsGen = Label(root, text="TEO Steps Generator", font= self.label_font)
        self.teoStepsGen.grid(row=0, column=0, sticky=W+E)
        self.teoStepsGen.grid_columnconfigure(0, weight=1)

        self.footprintsGenButton = Button(root, text="Footprints Generation", command=self.footprintsGen_clicked, font=self.button_font)
        self.footprintsGenButton.grid(row=6, column=0, sticky=W + E)

        self.stepsGenButton = Button(root, text="Steps Control", command=self.stepsGen_clicked, font=self.button_font)
        self.stepsGenButton.grid(row=7, column=0, sticky=W + E)

    def footprintsGen_clicked(self):
        window = Tk()
        footprints_generation(window)
        window.title("Footprints Generation")
        window.geometry("898x553")

    def stepsGen_clicked(self):
        window = Tk()
        steps_generation(window)
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
