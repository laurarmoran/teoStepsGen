from tkinter import *
from design_step import *
import tkinter.font as tkFont


class stepsGeneration:

    def __init__(self, root):
        self.labelFont = ('Helvetica', 26)
        self.labelFrameFont = ('Helvetica', 13, 'bold')
        self.buttonFont = ('Helvetica', 16)

        self.steps_generation = Label(root, text="STEPS CONTROL", font=self.labelFont)
        self.steps_generation.grid(row=0, column=0, columnspan=4, sticky=W+E)
        self.steps_generation.grid_columnconfigure(0, weight=1)


        # Initial Position ---------------------------------------------------------------------------------------
        self.initPos_frame = LabelFrame(root, text="Initial Position", font=self.labelFrameFont)
        self.initPos_frame.grid(row=1, column=0, rowspan=2, columnspan=2, sticky=W+E)

        initPos_option = IntVar()
        self.default_radioBut = Radiobutton(self.initPos_frame, text="Default", variable=initPos_option, value=1)
        self.default_radioBut.grid(row=2, column=0)
        self.file_radioBut = Radiobutton(self.initPos_frame, text="File", variable=initPos_option, value=2)
        self.file_radioBut.grid(row=2, column=1, sticky=E)
        self.file_radioBut.grid_columnconfigure(1, weight=1)


        # First Leg Support ----------------------------------------------------------------------------------------
        self.firstLegSupp_frame = LabelFrame(root, text="First Leg Support", font=self.labelFrameFont)
        self.firstLegSupp_frame.grid(row=3, column=0, rowspan=2, columnspan=2)
        self.firstLegSupp_frame.grid_columnconfigure(0, weight=1)

        firstLeg_option = IntVar()
        self.right_radioBut = Radiobutton(self.firstLegSupp_frame, text="Right Leg", variable=firstLeg_option, value=1)
        self.right_radioBut.grid(row=4, column=0)
        self.left_radioBut = Radiobutton(self.firstLegSupp_frame, text="Left Leg", variable=firstLeg_option, value=2)
        self.left_radioBut.grid(row=4, column=1)


        # Steps parameters ---------------------------------------------------------------------------------------
        self.stepsLength = Label(root, text="Steps Length (m)")
        self.stepsLength.grid(row=1, column=2, sticky=N+S)
        self.stepsLength_txt = Entry(root, width=10)
        self.stepsLength_txt.grid(row=1, column=3)

        self.stepsHeight = Label(root, text="Height (m)")
        self.stepsHeight.grid(row=2, column=2, sticky=N + S)
        self.stepsHeight_txt = Entry(root, width=10)
        self.stepsHeight_txt.grid(row=2, column=3)

        self.stepsTime = Label(root, text="Step Time (s)")
        self.stepsTime.grid(row=3, column=2)
        self.stepsTime_txt = Entry(root, width=10)
        self.stepsTime_txt.grid(row=3, column=3)

        self.time = Label(root, text="Time (s)")
        self.time.grid(row=4, column=2, sticky=N + S)
        self.time_txt = Entry(root, width=10)
        self.time_txt.grid(row=4, column=3)


        # Steps Design Button ---------------------------------------------------------------------------------------
        self.stepsDesign_button = Button(root, text="Steps Design", command=self.stepsDesign_clicked, font=self.buttonFont)
        self.stepsDesign_button.grid(row=5, column=2, columnspan=2, sticky=W+E)


    def stepsDesign_clicked(self):  # OPENS NEW WINDOW
        designStep_window = Tk()
        designStep(designStep_window)
        designStep_window.title("Design Step")
        designStep_window.geometry("698x653")
