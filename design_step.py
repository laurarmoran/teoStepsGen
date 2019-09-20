from tkinter import *
import tkinter.font as tkFont


class designStep:

    def __init__(self, root):
        self.labelFont = ('Helvetica', 26)
        self.labelFrameFont = ('Helvetica', 13, 'bold')
        self.buttonFont = ('Helvetica', 16)

        self.steps_generation = Label(root, text="DESIGN STEP", font=self.labelFont)
        self.steps_generation.grid(row=0, column=0, columnspan=6, sticky=W+E)
        self.steps_generation.grid_columnconfigure(0, weight=1)

        # Double Support ---------------------------------------------------------------------------------------
        self.doubleSupp_frame = LabelFrame(root, text="Double Support", font=self.labelFrameFont)
        self.doubleSupp_frame.grid(row=1, column=0, columnspan=6, sticky=W+E)

        ### Delta CoM (m) -----------------------------------------------
        self.deltaCoM_frame = LabelFrame(self.doubleSupp_frame, text="Delta CoM (m)", font=self.labelFrameFont)
        self.deltaCoM_frame.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.deltax = Label(self.deltaCoM_frame, text="delta x")
        self.deltax.grid(row=1, column=0)
        self.deltax_txt = Entry(self.deltaCoM_frame, width=8)
        self.deltax_txt.grid(row=2, column=0)

        self.deltay = Label(self.deltaCoM_frame, text="delta y")
        self.deltay.grid(row=1, column=1)
        self.deltay_txt = Entry(self.deltaCoM_frame, width=8)
        self.deltay_txt.grid(row=2, column=1)

        self.deltaz = Label(self.deltaCoM_frame, text="delta z")
        self.deltaz.grid(row=1, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_frame, width=8)
        self.deltaz_txt.grid(row=2, column=2)




        # Simple Support ---------------------------------------------------------------------------------------
        self.simpleSupp_frame = LabelFrame(root, text="Simple Support", font=self.labelFrameFont)
        self.simpleSupp_frame.grid(row=3, column=0, columnspan=6, sticky=W + E)

        ### Delta CoM Phase-1 (m) -----------------------------------------------
        self.deltaCoM_phase1_frame = LabelFrame(self.simpleSupp_frame, text="Delta CoM Phase-1 (m)", font=self.labelFrameFont)
        self.deltaCoM_phase1_frame.grid(row=4, column=0, columnspan=3)

        self.deltax = Label(self.deltaCoM_phase1_frame, text="delta x")
        self.deltax.grid(row=5, column=0)
        self.deltax_txt = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltax_txt.grid(row=6, column=0)

        self.deltay = Label(self.deltaCoM_phase1_frame, text="delta y")
        self.deltay.grid(row=5, column=1)
        self.deltay_txt = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltay_txt.grid(row=6, column=1)

        self.deltaz = Label(self.deltaCoM_phase1_frame, text="delta z")
        self.deltaz.grid(row=5, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltaz_txt.grid(row=6, column=2)

        ### Delta FF Phase-1 (m) -----------------------------------------------
        self.deltaFF_phase1_frame = LabelFrame(self.simpleSupp_frame, text="Delta FF Phase-1 (m)",
                                               font=self.labelFrameFont)
        self.deltaFF_phase1_frame.grid(row=4, column=3, columnspan=3)

        self.deltax = Label(self.deltaFF_phase1_frame, text="delta x")
        self.deltax.grid(row=5, column=3)
        self.deltax_txt = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltax_txt.grid(row=6, column=3)

        self.deltay = Label(self.deltaFF_phase1_frame, text="delta y")
        self.deltay.grid(row=5, column=4)
        self.deltay_txt = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltay_txt.grid(row=6, column=4)

        self.deltaz = Label(self.deltaFF_phase1_frame, text="delta z")
        self.deltaz.grid(row=5, column=5)
        self.deltaz_txt = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltaz_txt.grid(row=6, column=5)

        ### Delta CoM Phase-2 (m) -----------------------------------------------
        self.deltaCoM_phase2_frame = LabelFrame(self.simpleSupp_frame, text="Delta CoM Phase-2 (m)",
                                                font=self.labelFrameFont)
        self.deltaCoM_phase2_frame.grid(row=7, column=0, columnspan=3)

        self.deltax = Label(self.deltaCoM_phase2_frame, text="delta x")
        self.deltax.grid(row=8, column=0)
        self.deltax_txt = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltax_txt.grid(row=9, column=0)

        self.deltay = Label(self.deltaCoM_phase2_frame, text="delta y")
        self.deltay.grid(row=8, column=1)
        self.deltay_txt = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltay_txt.grid(row=9, column=1)

        self.deltaz = Label(self.deltaCoM_phase2_frame, text="delta z")
        self.deltaz.grid(row=8, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltaz_txt.grid(row=9, column=2)

        ### Delta FF Phase-2 (m) -----------------------------------------------
        self.deltaFF_phase2_frame = LabelFrame(self.simpleSupp_frame, text="Delta FF Phase-2 (m)",
                                               font=self.labelFrameFont)
        self.deltaFF_phase2_frame.grid(row=7, column=3, columnspan=3)

        self.deltax = Label(self.deltaFF_phase2_frame, text="delta x")
        self.deltax.grid(row=8, column=3)
        self.deltax_txt = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltax_txt.grid(row=9, column=3)

        self.deltay = Label(self.deltaFF_phase2_frame, text="delta y")
        self.deltay.grid(row=8, column=4)
        self.deltay_txt = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltay_txt.grid(row=9, column=4)

        self.deltaz = Label(self.deltaFF_phase2_frame, text="delta z")
        self.deltaz.grid(row=8, column=5)
        self.deltaz_txt = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltaz_txt.grid(row=9, column=5)

        ### Interpolation Double Support-----------------------------------------------
        self.interpolation_frame = LabelFrame(self.doubleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame.grid(row=1, column=3, columnspan=3, sticky=W + E)
        # self.interpolation_frame.grid_rowconfigure(2, weight=1)
        # self.interpolation_frame.grid_columnconfigure(5, weight=1)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame)
        self.init_var.set(" ")  # default value
        self.interpolation_txt = OptionMenu(self.interpolation_frame, self.init_var, *self.data_interpolation)
        self.interpolation_txt.grid(row=2, column=5, sticky=W + E)
        self.interpolation_txt.configure(width=9)
        self.interpolation_txt.grid_columnconfigure(5, weight=1)

        ### Interpolation Simple Support-----------------------------------------------
        self.interpolation_frame = LabelFrame(self.simpleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame.grid(row=10, column=0, columnspan=3, sticky=W+E)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame)
        self.init_var.set(" ")  # default value
        self.interpolation_txt = OptionMenu(self.interpolation_frame, self.init_var, *self.data_interpolation)
        self.interpolation_txt.grid(row=11, column=1, sticky=W+E)
        self.interpolation_txt.configure(width=9)

        ### Interpolation Simple Support-----------------------------------------------
        self.interpolation_frame = LabelFrame(self.simpleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame.grid(row=10, column=3, columnspan=3, sticky=W+E)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame)
        self.init_var.set(" ")  # default value
        self.interpolation_txt = OptionMenu(self.interpolation_frame, self.init_var, *self.data_interpolation)
        self.interpolation_txt.grid(row=11, column=4, sticky=W+E)
        self.interpolation_txt.configure(width=9)


        '''''
        # Steps Design Button ---------------------------------------------------------------------------------------
        self.stepsDesign_button = Button(root, text="Steps Design", command=self.stepsDesign_clicked, font=self.buttonFont)
        self.stepsDesign_button.grid(row=5, column=2, columnspan=2, sticky=W+E)


    def stepsDesign_clicked(self):  # OPENS NEW WINDOW
        designStep_window = Tk()
        #designStep_window = Toplevel(window)
        designStep_window.title("Design Step")
        designStep_window.geometry("898x553")
        '''''