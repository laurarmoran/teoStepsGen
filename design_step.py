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
        self.doubleSupp_frame.grid(row=1, column=0, columnspan=4, sticky=W+E)

        ### Delta CoM (m) -----------------------------------------------
        self.deltaCoM_frame = LabelFrame(self.doubleSupp_frame, text="Delta CoM (m)", font=self.labelFrameFont)
        self.deltaCoM_frame.grid(row=2, column=0, columnspan=3, sticky=W+E)

        self.deltax = Label(self.deltaCoM_frame, text="delta x")
        self.deltax.grid(row=3, column=0)
        self.deltax_txt_1 = Entry(self.deltaCoM_frame, width=8)
        self.deltax_txt_1.grid(row=4, column=0)

        self.deltay = Label(self.deltaCoM_frame, text="delta y")
        self.deltay.grid(row=3, column=1)
        self.deltay_txt_1 = Entry(self.deltaCoM_frame, width=8)
        self.deltay_txt_1.grid(row=4, column=1)

        self.deltaz = Label(self.deltaCoM_frame, text="delta z")
        self.deltaz.grid(row=3, column=2)
        self.deltaz_txt_1 = Entry(self.deltaCoM_frame, width=8)
        self.deltaz_txt_1.grid(row=4, column=2)


        # Simple Support ---------------------------------------------------------------------------------------
        self.simpleSupp_frame = LabelFrame(root, text="Simple Support", font=self.labelFrameFont)
        self.simpleSupp_frame.grid(row=5, column=0, columnspan=4, sticky=W + E)

        ### Delta CoM Phase-1 (m) -----------------------------------------------
        self.deltaCoM_phase1_frame = LabelFrame(self.simpleSupp_frame, text="Delta CoM Phase-1 (m)", font=self.labelFrameFont)
        self.deltaCoM_phase1_frame.grid(row=6, column=0, columnspan=3)

        self.deltax = Label(self.deltaCoM_phase1_frame, text="delta x")
        self.deltax.grid(row=7, column=0)
        self.deltax_txt_2 = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltax_txt_2.grid(row=8, column=0)

        self.deltay = Label(self.deltaCoM_phase1_frame, text="delta y")
        self.deltay.grid(row=7, column=1)
        self.deltay_txt_2 = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltay_txt_2.grid(row=8, column=1)

        self.deltaz = Label(self.deltaCoM_phase1_frame, text="delta z")
        self.deltaz.grid(row=7, column=2)
        self.deltaz_txt_2 = Entry(self.deltaCoM_phase1_frame, width=8)
        self.deltaz_txt_2.grid(row=8, column=2)

        ### Delta FF Phase-1 (m) -----------------------------------------------
        self.deltaFF_phase1_frame = LabelFrame(self.simpleSupp_frame, text="Delta FF Phase-1 (m)",
                                               font=self.labelFrameFont)
        self.deltaFF_phase1_frame.grid(row=6, column=3, columnspan=3)

        self.deltax = Label(self.deltaFF_phase1_frame, text="delta x")
        self.deltax.grid(row=7, column=3)
        self.deltax_txt_3 = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltax_txt_3.grid(row=8, column=3)

        self.deltay = Label(self.deltaFF_phase1_frame, text="delta y")
        self.deltay.grid(row=7, column=4)
        self.deltay_txt_3 = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltay_txt_3.grid(row=8, column=4)

        self.deltaz = Label(self.deltaFF_phase1_frame, text="delta z")
        self.deltaz.grid(row=7, column=5)
        self.deltaz_txt_3 = Entry(self.deltaFF_phase1_frame, width=8)
        self.deltaz_txt_3.grid(row=8, column=5)

        ### Delta CoM Phase-2 (m) -----------------------------------------------
        self.deltaCoM_phase2_frame = LabelFrame(self.simpleSupp_frame, text="Delta CoM Phase-2 (m)",
                                                font=self.labelFrameFont)
        self.deltaCoM_phase2_frame.grid(row=9, column=0, columnspan=3)

        self.deltax = Label(self.deltaCoM_phase2_frame, text="delta x")
        self.deltax.grid(row=10, column=0)
        self.deltax_txt_4 = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltax_txt_4.grid(row=11, column=0)

        self.deltay = Label(self.deltaCoM_phase2_frame, text="delta y")
        self.deltay.grid(row=10, column=1)
        self.deltay_txt_4 = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltay_txt_4.grid(row=11, column=1)

        self.deltaz = Label(self.deltaCoM_phase2_frame, text="delta z")
        self.deltaz.grid(row=10, column=2)
        self.deltaz_txt_4 = Entry(self.deltaCoM_phase2_frame, width=8)
        self.deltaz_txt_4.grid(row=11, column=2)

        ### Delta FF Phase-2 (m) -----------------------------------------------
        self.deltaFF_phase2_frame = LabelFrame(self.simpleSupp_frame, text="Delta FF Phase-2 (m)",
                                               font=self.labelFrameFont)
        self.deltaFF_phase2_frame.grid(row=9, column=3, columnspan=3)

        self.deltax = Label(self.deltaFF_phase2_frame, text="delta x")
        self.deltax.grid(row=10, column=3)
        self.deltax_txt_5 = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltax_txt_5.grid(row=11, column=3)

        self.deltay = Label(self.deltaFF_phase2_frame, text="delta y")
        self.deltay.grid(row=10, column=4)
        self.deltay_txt_5 = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltay_txt_5.grid(row=11, column=4)

        self.deltaz = Label(self.deltaFF_phase2_frame, text="delta z")
        self.deltaz.grid(row=10, column=5)
        self.deltaz_txt_5 = Entry(self.deltaFF_phase2_frame, width=8)
        self.deltaz_txt_5.grid(row=11, column=5)

        # Double Support ---------------------------------------------------------------------------------------
        self.doubleSupp_frame_2 = LabelFrame(root, text="Double Support", font=self.labelFrameFont)
        self.doubleSupp_frame_2.grid(row=14, column=0, columnspan=4, sticky=W + E)

        ### Delta CoM (m) -----------------------------------------------
        self.deltaCoM_frame_2 = LabelFrame(self.doubleSupp_frame_2, text="Delta CoM (m)", font=self.labelFrameFont)
        self.deltaCoM_frame_2.grid(row=15, column=0, columnspan=3, sticky=W + E)

        self.deltax = Label(self.deltaCoM_frame_2, text="delta x")
        self.deltax.grid(row=16, column=0)
        self.deltax_txt_6 = Entry(self.deltaCoM_frame_2, width=8)
        self.deltax_txt_6.grid(row=17, column=0)

        self.deltay = Label(self.deltaCoM_frame_2, text="delta y")
        self.deltay.grid(row=16, column=1)
        self.deltay_txt_6 = Entry(self.deltaCoM_frame_2, width=8)
        self.deltay_txt_6.grid(row=17, column=1)

        self.deltaz = Label(self.deltaCoM_frame_2, text="delta z")
        self.deltaz.grid(row=16, column=2)
        self.deltaz_txt_6 = Entry(self.deltaCoM_frame_2, width=8)
        self.deltaz_txt_6.grid(row=17, column=2)

        # Arms Movement ---------------------------------------------------------------------------------------
        self.arms_movement_frame = LabelFrame(root, text="Arms Movement", font=self.labelFrameFont)
        self.arms_movement_frame.grid(row=18, column=0, columnspan=4, sticky=W + E)

        ### Delta Right Hand -----------------------------------------------
        self.deltaRightHand_frame = LabelFrame(self.arms_movement_frame, text="Delta Right Hand (m)", font=self.labelFrameFont)
        self.deltaRightHand_frame.grid(row=19, column=0, columnspan=3, sticky=W + E)

        self.deltax = Label(self.deltaRightHand_frame, text="delta x")
        self.deltax.grid(row=20, column=0)
        self.deltax_txt_7 = Entry(self.deltaRightHand_frame, width=8)
        self.deltax_txt_7.grid(row=21, column=0)

        self.deltay = Label(self.deltaRightHand_frame, text="delta y")
        self.deltay.grid(row=20, column=1)
        self.deltay_txt_7 = Entry(self.deltaRightHand_frame, width=8)
        self.deltay_txt_7.grid(row=21, column=1)

        self.deltaz = Label(self.deltaRightHand_frame, text="delta z")
        self.deltaz.grid(row=20, column=2)
        self.deltaz_txt_7 = Entry(self.deltaRightHand_frame, width=8)
        self.deltaz_txt_7.grid(row=21, column=2)

        ### Delta Left Hand -----------------------------------------------
        self.deltaLeftHand_frame = LabelFrame(self.arms_movement_frame, text="Delta Left Hand (m)", font=self.labelFrameFont)
        self.deltaLeftHand_frame.grid(row=22, column=0, columnspan=3, sticky=W + E)

        self.deltax = Label(self.deltaLeftHand_frame, text="delta x")
        self.deltax.grid(row=23, column=0)
        self.deltax_txt_8 = Entry(self.deltaLeftHand_frame, width=8)
        self.deltax_txt_8.grid(row=24, column=0)

        self.deltay = Label(self.deltaLeftHand_frame, text="delta y")
        self.deltay.grid(row=23, column=1)
        self.deltay_txt_8 = Entry(self.deltaLeftHand_frame, width=8)
        self.deltay_txt_8.grid(row=24, column=1)

        self.deltaz = Label(self.deltaLeftHand_frame, text="delta z")
        self.deltaz.grid(row=23, column=2)
        self.deltaz_txt_8 = Entry(self.deltaLeftHand_frame, width=8)
        self.deltaz_txt_8.grid(row=24, column=2)

        # Number of steps box ----------------------------------------------------------------------------------
        self.numberSteps = Label(root, text="Number of Steps")
        self.numberSteps.grid(row=24, column=3)
        self.numberSteps_txt = Entry(root, width=8)
        self.numberSteps_txt.grid(row=25, column=3)

        ### Interpolation 1 -----------------------------------------------
        self.interpolation_frame_1 = LabelFrame(self.doubleSupp_frame, text="Interpolation", font=self.labelFrameFont)
        self.interpolation_frame_1.grid(row=2, column=3, rowspan=3, sticky=W + E)
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

        # Buttons -------------------------------------------------------------------------------------------------
        self.generate_button = Button(root, text="Generate Step", command=self.generate_clicked, font=self.buttonFont)
        self.generate_button.grid(row=24, column=0, rowspan=2, sticky=W+E)

        self.newStep_button = Button(root, text="New Step", command=self.newStep_clicked, font=self.buttonFont)
        self.newStep_button.grid(row=24, column=1, rowspan=2, sticky=W+E)

        self.resetTrajectory_button = Button(root, text="Reset Trajectory", command=self.resetTrajectory_clicked, font=self.buttonFont)
        self.resetTrajectory_button.grid(row=24, column=2, rowspan=2, sticky=W + E)

        self.matlab_button = Button(root, text="MATLAB visualization", font=self.buttonFont, command=self.matlab_clicked)
        self.matlab_button.grid(row=24, column=4, rowspan=2)

        self.ros_button = Button(root, text="ROS visualization", font=self.buttonFont, command=self.ros_clicked)
        self.ros_button.grid(row=24, column=5, rowspan=2)


    def generate_clicked(self):
        print("Generate button clicked")

    def newStep_clicked(self):
        print("New Step button clicked")

    def resetTrajectory_clicked(self):
        print("Reset button clicked")
        self.deltax_txt_1.delete(0, END)
        self.deltay_txt_1.delete(0, END)
        self.deltaz_txt_1.delete(0, END)
        self.deltax_txt_2.delete(0, END)
        self.deltay_txt_2.delete(0, END)
        self.deltaz_txt_2.delete(0, END)
        self.deltax_txt_3.delete(0, END)
        self.deltay_txt_3.delete(0, END)
        self.deltaz_txt_3.delete(0, END)
        self.deltax_txt_4.delete(0, END)
        self.deltay_txt_4.delete(0, END)
        self.deltaz_txt_4.delete(0, END)
        self.deltax_txt_5.delete(0, END)
        self.deltay_txt_5.delete(0, END)
        self.deltaz_txt_5.delete(0, END)
        self.deltax_txt_6.delete(0, END)
        self.deltay_txt_6.delete(0, END)
        self.deltaz_txt_6.delete(0, END)
        self.deltax_txt_7.delete(0, END)
        self.deltay_txt_7.delete(0, END)
        self.deltaz_txt_7.delete(0, END)
        self.deltax_txt_8.delete(0, END)
        self.deltay_txt_8.delete(0, END)
        self.deltaz_txt_8.delete(0, END)


    def matlab_clicked(self): # opens new window
        matlab_window = Tk()
        matlab_window.title("MATLAB visualization")
        matlab_window.geometry("898x553")

    def ros_clicked(self): # opens new window
        ros_window = Tk()
        ros_window.title("ROS visualization")
        ros_window.geometry("898x553")