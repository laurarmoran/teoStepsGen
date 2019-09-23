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
        self.deltaCoM_frame.grid(row=2, column=0, columnspan=3, sticky=W+E)

        self.deltax = Label(self.deltaCoM_frame, text="delta x")
        self.deltax.grid(row=3, column=0)
        self.deltax_txt = Entry(self.deltaCoM_frame, width=8)
        self.deltax_txt.grid(row=4, column=0)

        self.deltay = Label(self.deltaCoM_frame, text="delta y")
        self.deltay.grid(row=3, column=1)
        self.deltay_txt = Entry(self.deltaCoM_frame, width=8)
        self.deltay_txt.grid(row=4, column=1)

        self.deltaz = Label(self.deltaCoM_frame, text="delta z")
        self.deltaz.grid(row=3, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_frame, width=8)
        self.deltaz_txt.grid(row=4, column=2)




        # Simple Support ---------------------------------------------------------------------------------------
        self.simpleSupp_frame = LabelFrame(root, text="Simple Support", font=self.labelFrameFont)
        self.simpleSupp_frame.grid(row=5, column=0, columnspan=6, sticky=W + E)

        ### Delta CoM Phase-1 (m) -----------------------------------------------
        self.deltaCoM_phase1_frame = LabelFrame(self.simpleSupp_frame, text="Delta CoM Phase-1 (m)", font=self.labelFrameFont)
        self.deltaCoM_phase1_frame.grid(row=6, column=0, columnspan=3)

        self.deltax = Label(self.deltaCoM_phase1_frame, text="delta x")
        self.deltax.grid(row=7, column=0)
        self.deltax_txt = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltax_txt.grid(row=8, column=0)

        self.deltay = Label(self.deltaCoM_phase1_frame, text="delta y")
        self.deltay.grid(row=7, column=1)
        self.deltay_txt = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltay_txt.grid(row=8, column=1)

        self.deltaz = Label(self.deltaCoM_phase1_frame, text="delta z")
        self.deltaz.grid(row=7, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltaz_txt.grid(row=8, column=2)

        ### Delta FF Phase-1 (m) -----------------------------------------------
        self.deltaFF_phase1_frame = LabelFrame(self.simpleSupp_frame, text="Delta FF Phase-1 (m)",
                                               font=self.labelFrameFont)
        self.deltaFF_phase1_frame.grid(row=6, column=3, columnspan=3)

        self.deltax = Label(self.deltaFF_phase1_frame, text="delta x")
        self.deltax.grid(row=7, column=3)
        self.deltax_txt = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltax_txt.grid(row=8, column=3)

        self.deltay = Label(self.deltaFF_phase1_frame, text="delta y")
        self.deltay.grid(row=7, column=4)
        self.deltay_txt = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltay_txt.grid(row=8, column=4)

        self.deltaz = Label(self.deltaFF_phase1_frame, text="delta z")
        self.deltaz.grid(row=7, column=5)
        self.deltaz_txt = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltaz_txt.grid(row=8, column=5)

        ### Delta CoM Phase-2 (m) -----------------------------------------------
        self.deltaCoM_phase2_frame = LabelFrame(self.simpleSupp_frame, text="Delta CoM Phase-2 (m)",
                                                font=self.labelFrameFont)
        self.deltaCoM_phase2_frame.grid(row=9, column=0, columnspan=3)

        self.deltax = Label(self.deltaCoM_phase2_frame, text="delta x")
        self.deltax.grid(row=10, column=0)
        self.deltax_txt = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltax_txt.grid(row=11, column=0)

        self.deltay = Label(self.deltaCoM_phase2_frame, text="delta y")
        self.deltay.grid(row=10, column=1)
        self.deltay_txt = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltay_txt.grid(row=11, column=1)

        self.deltaz = Label(self.deltaCoM_phase2_frame, text="delta z")
        self.deltaz.grid(row=10, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltaz_txt.grid(row=11, column=2)

        ### Delta FF Phase-2 (m) -----------------------------------------------
        self.deltaFF_phase2_frame = LabelFrame(self.simpleSupp_frame, text="Delta FF Phase-2 (m)",
                                               font=self.labelFrameFont)
        self.deltaFF_phase2_frame.grid(row=9, column=3, columnspan=3)

        self.deltax = Label(self.deltaFF_phase2_frame, text="delta x")
        self.deltax.grid(row=10, column=3)
        self.deltax_txt = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltax_txt.grid(row=11, column=3)

        self.deltay = Label(self.deltaFF_phase2_frame, text="delta y")
        self.deltay.grid(row=10, column=4)
        self.deltay_txt = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltay_txt.grid(row=11, column=4)

        self.deltaz = Label(self.deltaFF_phase2_frame, text="delta z")
        self.deltaz.grid(row=10, column=5)
        self.deltaz_txt = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltaz_txt.grid(row=11, column=5)

        # Double Support ---------------------------------------------------------------------------------------
        self.doubleSupp_frame_2 = LabelFrame(root, text="Double Support", font=self.labelFrameFont)
        self.doubleSupp_frame_2.grid(row=14, column=0, columnspan=6, sticky=W + E)

        ### Delta CoM (m) -----------------------------------------------
        self.deltaCoM_frame_2 = LabelFrame(self.doubleSupp_frame_2, text="Delta CoM (m)", font=self.labelFrameFont)
        self.deltaCoM_frame_2.grid(row=15, column=0, columnspan=3, sticky=W + E)

        self.deltax = Label(self.deltaCoM_frame_2, text="delta x")
        self.deltax.grid(row=16, column=0)
        self.deltax_txt = Entry(self.deltaCoM_frame_2, width=8)
        self.deltax_txt.grid(row=17, column=0)

        self.deltay = Label(self.deltaCoM_frame_2, text="delta y")
        self.deltay.grid(row=16, column=1)
        self.deltay_txt = Entry(self.deltaCoM_frame_2, width=8)
        self.deltay_txt.grid(row=17, column=1)

        self.deltaz = Label(self.deltaCoM_frame_2, text="delta z")
        self.deltaz.grid(row=16, column=2)
        self.deltaz_txt = Entry(self.deltaCoM_frame_2, width=8)
        self.deltaz_txt.grid(row=17, column=2)

        # Arms Movement ---------------------------------------------------------------------------------------
        self.arms_movement_frame = LabelFrame(root, text="Arms Movement", font=self.labelFrameFont)
        self.arms_movement_frame.grid(row=18, column=0, columnspan=6, sticky=W + E)

        ### Delta Right Hand -----------------------------------------------
        self.deltaRightHand_frame = LabelFrame(self.arms_movement_frame, text="Delta Right Hand (m)", font=self.labelFrameFont)
        self.deltaRightHand_frame.grid(row=19, column=0, columnspan=3, sticky=W + E)

        self.deltax = Label(self.deltaRightHand_frame, text="delta x")
        self.deltax.grid(row=20, column=0)
        self.deltax_txt = Entry(self.deltaRightHand_frame, width=8)
        self.deltax_txt.grid(row=21, column=0)

        self.deltay = Label(self.deltaRightHand_frame, text="delta y")
        self.deltay.grid(row=20, column=1)
        self.deltay_txt = Entry(self.deltaRightHand_frame, width=8)
        self.deltay_txt.grid(row=21, column=1)

        self.deltaz = Label(self.deltaRightHand_frame, text="delta z")
        self.deltaz.grid(row=20, column=2)
        self.deltaz_txt = Entry(self.deltaRightHand_frame, width=8)
        self.deltaz_txt.grid(row=21, column=2)

        ### Delta Left Hand -----------------------------------------------
        self.deltaLeftHand_frame = LabelFrame(self.arms_movement_frame, text="Delta Left Hand (m)", font=self.labelFrameFont)
        self.deltaLeftHand_frame.grid(row=22, column=0, columnspan=3, sticky=W + E)

        self.deltax = Label(self.deltaLeftHand_frame, text="delta x")
        self.deltax.grid(row=23, column=0)
        self.deltax_txt = Entry(self.deltaLeftHand_frame, width=8)
        self.deltax_txt.grid(row=24, column=0)

        self.deltay = Label(self.deltaLeftHand_frame, text="delta y")
        self.deltay.grid(row=23, column=1)
        self.deltay_txt = Entry(self.deltaLeftHand_frame, width=8)
        self.deltay_txt.grid(row=24, column=1)

        self.deltaz = Label(self.deltaLeftHand_frame, text="delta z")
        self.deltaz.grid(row=23, column=2)
        self.deltaz_txt = Entry(self.deltaLeftHand_frame, width=8)
        self.deltaz_txt.grid(row=24, column=2)



        ### Interpolation 1 -----------------------------------------------
        self.interpolation_frame_1 = LabelFrame(self.doubleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame_1.grid(row=2, column=3, rowspan=3, columnspan=3, sticky=W + E)
        self.interpolation_frame_1.grid_columnconfigure(3, weight=1)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame_1)
        self.init_var.set(" ")  # default value
        self.interpolation_txt_1 = OptionMenu(self.interpolation_frame_1, self.init_var, *self.data_interpolation)
        self.interpolation_txt_1.grid(row=3, column=3, columnspan=3)
        self.interpolation_txt_1.configure(width=15)

        ### Interpolation 2 -----------------------------------------------
        self.interpolation_frame_2 = LabelFrame(self.simpleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame_2.grid(row=12, column=0, columnspan=3, sticky=W+E)
        self.interpolation_frame_2.grid_columnconfigure(0, weight=1)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame_2)
        self.init_var.set(" ")  # default value
        self.interpolation_txt_2 = OptionMenu(self.interpolation_frame_2, self.init_var, *self.data_interpolation)
        self.interpolation_txt_2.grid(row=13, column=0, columnspan=3)
        self.interpolation_txt_2.configure(width=15)

        ### Interpolation 3 -----------------------------------------------
        self.interpolation_frame_3 = LabelFrame(self.simpleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame_3.grid(row=12, column=3, columnspan=3, sticky=W+E)
        self.interpolation_frame_3.grid_columnconfigure(3, weight=1)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame_3)
        self.init_var.set(" ")  # default value
        self.interpolation_txt_3 = OptionMenu(self.interpolation_frame_3, self.init_var, *self.data_interpolation)
        self.interpolation_txt_3.grid(row=13, column=3, columnspan=3)
        self.interpolation_txt_3.configure(width=15)
        #self.interpolation_txt_3.grid_columnconfigure(3, weight=1)

        ### Interpolation 4 -----------------------------------------------
        self.interpolation_frame_4 = LabelFrame(self.doubleSupp_frame_2, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame_4.grid(row=15, column=3, rowspan=3, columnspan=3, sticky=W + E)
        self.interpolation_frame_4.grid_columnconfigure(3, weight=1)
        #self.interpolation_frame_4.grid_columnconfigure(4, weight=0)
        #self.interpolation_frame_4.grid_columnconfigure(5, weight=0)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame_4)
        self.init_var.set(" ")  # default value
        self.interpolation_txt_4 = OptionMenu(self.interpolation_frame_4, self.init_var, *self.data_interpolation)
        self.interpolation_txt_4.grid(row=16, column=3, columnspan=3)
        self.interpolation_txt_4.configure(width=15)
        self.interpolation_txt_4.grid_columnconfigure(3, weight=1)

        ### Interpolation 5 -----------------------------------------------
        self.interpolation_frame_5 = LabelFrame(self.arms_movement_frame, text="Interpolation",font=self.labelFrameFont)
        self.interpolation_frame_5.grid(row=19, column=3, rowspan=3, columnspan=3, sticky=W + E)
        self.interpolation_frame_5.grid_columnconfigure(3, weight=1)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame_5)
        self.init_var.set(" ")  # default value
        self.interpolation_txt_5 = OptionMenu(self.interpolation_frame_5, self.init_var, *self.data_interpolation)
        self.interpolation_txt_5.grid(row=20, column=3, columnspan=3)
        self.interpolation_txt_5.configure(width=15)

        ### Interpolation 6 -----------------------------------------------
        self.interpolation_frame_6 = LabelFrame(self.arms_movement_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame_6.grid(row=22, column=3, rowspan=3, columnspan=3, sticky=W + E)
        self.interpolation_frame_6.grid_columnconfigure(3, weight=1)

        self.data_interpolation = ("Linear", "")
        self.init_var = StringVar(self.interpolation_frame_6)
        self.init_var.set(" ")  # default value
        self.interpolation_txt_6 = OptionMenu(self.interpolation_frame_6, self.init_var, *self.data_interpolation)
        self.interpolation_txt_6.grid(row=23, column=3, columnspan=3)
        self.interpolation_txt_6.configure(width=15)
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