'''''
 Embedding matplotlib: https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
 Grid manager (text,buttons,image): https://effbot.org/tkinterbook/grid.htm
 Every widget: https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/all
'''''

import tkinter
from tkinter import *
from tkinter.ttk import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


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

    def __init__(self, window):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas_title = Label(window, text="Foot motion")
        self.canvas_title.grid(row=1, column=0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=window)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=2, column=0, rowspan=11)

        # Label Frame for text entries
        self.stepsGen_frame = LabelFrame(window, text="Steps Generation")
        self.stepsGen_frame.grid(row=0, column=1, rowspan=13)

        # Text entries
        self.numSteps = Label(self.stepsGen_frame, text="Number of steps")
        self.numSteps.grid(row=0, column=1)
        self.numSteps_txt = Entry(self.stepsGen_frame, width=10)
        self.numSteps_txt.grid(row=0, column=2)

        self.thetaVar = Label(self.stepsGen_frame, text="Theta Variation")
        self.thetaVar.grid(row=1, column=1)
        self.thetaVar_txt = Entry(self.stepsGen_frame, width=10)
        self.thetaVar_txt.grid(row=1, column=2)

        self.initFloatFoot = Label(self.stepsGen_frame, text="Initial Floating Foot")
        self.initFloatFoot.grid(row=2, column=1)
        self.data=("RIGHT", "LEFT")
        self.initFloatFoot_txt = Combobox(self.stepsGen_frame, values=self.data)
        self.initFloatFoot_txt.configure(width=9)
        self.initFloatFoot_txt.grid(row=2, column=2)

        # "Finish both feet" check box
        self.chk_state = BooleanVar()
        self.chk_state.set(True)  # set check state
        self.chk = Checkbutton(self.stepsGen_frame, text='Finish both feet', var=self.chk_state)
        self.chk.grid(row=3, column=1)

        # Text entries
        self.stepLength = Label(self.stepsGen_frame, text="Step length")
        self.stepLength.grid(row=4, column=1)
        self.stepLength_txt = Entry(self.stepsGen_frame, width=10)
        self.stepLength_txt.grid(row=4, column=2)

        self.stepHeight = Label(self.stepsGen_frame, text="Step height")
        self.stepHeight.grid(row=5, column=1)
        self.stepHeight_txt = Entry(self.stepsGen_frame, width=10)
        self.stepHeight_txt.grid(row=5, column=2)

        self.timeStep = Label(self.stepsGen_frame, text="Time of step")
        self.timeStep.grid(row=6, column=1)
        self.timeStep_txt = Entry(self.stepsGen_frame, width=10)
        self.timeStep_txt.grid(row=6, column=2)

        self.ts = Label(self.stepsGen_frame, text="Ts")
        self.ts.grid(row=7, column=1)
        self.ts_txt = Entry(self.stepsGen_frame, width=10)
        self.ts_txt.grid(row=7, column=2)

        self.doubleSupp = Label(self.stepsGen_frame, text="% Double support")
        self.doubleSupp.grid(row=8, column=1)
        self.doubleSupp_txt = Entry(self.stepsGen_frame, width=10)
        self.doubleSupp_txt.grid(row=8, column=2)

        self.d = Label(self.stepsGen_frame, text="d")
        self.d.grid(row=9, column=1)
        self.d_txt = Entry(self.stepsGen_frame, width=10)
        self.d_txt.grid(row=9, column=2)

        # Buttons
        self.generateButton = Button(self.stepsGen_frame, text="Generate", command=self.generate_clicked)
        self.generateButton.grid(column=1, row=10)

        self.resetButton = Button(self.stepsGen_frame, text="Reset", command=self.reset_clicked)
        self.resetButton.grid(column=2, row=10)

    def generate_clicked(self):
        self.lbl.configure(text='')

    def reset_clicked(self):
        self.lbl.configure(text='')


def main():
    window = Tk()
    win = TeoStepsGen(window)
    window.title("TEO Steps Generator")
    window.geometry("800x600")
    window.mainloop()

    # window.geometry("800x600")


if __name__ == '__main__':
    main()
