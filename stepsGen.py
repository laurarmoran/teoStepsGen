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


''''
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.NONE, expand=0)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)
'''''

#         self.stepsGen_frame.grid_columnconfigure(7, weight=0)


class TeoStepsGen:

    def __init__(self, window):

        self.customFont = tkFont.Font(family="Arial black", size=13)

        ######### Embedding matplotlib canvas
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas_title = Label(window, text="Foot motion", font=self.customFont)
        self.canvas_title.grid(row=0, column=2, columnspan=5)

        self.canvas = FigureCanvasTkAgg(self.fig, master=window)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, rowspan=12, columnspan=8, sticky=E+W)
        #self.canvas.get_tk_widget().grid_rowconfigure(7, weight=0)

        ######## LabelFrame for Steps Generation
        self.stepsGen_frame = LabelFrame(window, text="Steps Generation", font=self.customFont)
        self.stepsGen_frame.grid(row=1, column=8, rowspan=12, columnspan=2)

        # Steps Generation
        self.numSteps = Label(self.stepsGen_frame, text="Number of steps")
        self.numSteps.grid(row=2, column=8)
        self.numSteps_txt = Entry(self.stepsGen_frame, width=10)
        self.numSteps_txt.grid(row=2, column=9)

        self.thetaVar = Label(self.stepsGen_frame, text="Theta Variation")
        self.thetaVar.grid(row=3, column=8)
        self.thetaVar_txt = Entry(self.stepsGen_frame, width=10)
        self.thetaVar_txt.grid(row=3, column=9)

        self.initFloatFoot = Label(self.stepsGen_frame, text="Initial Floating Foot")
        self.initFloatFoot.grid(row=4, column=8)
        self.data = ("RIGHT", "LEFT")
        # self.initFloatFoot_txt = Combobox(self.stepsGen_frame, values=self.data)  # uses ttk wich changes theme colour
        self.init_var = StringVar(self.stepsGen_frame)
        self.init_var.set(" ")  # default value
        self.initFloatFoot_txt = OptionMenu(self.stepsGen_frame, self.init_var, *self.data)
        self.initFloatFoot_txt.grid(row=14, column=1)
        #self.initFloatFoot_txt.configure(width=7)

        self.initFloatFoot_txt.configure(width=9)
        self.initFloatFoot_txt.grid(row=4, column=9)

        # "Finish both feet" check box
        self.chk_state = BooleanVar()
        self.chk_state.set(True)  # set check state
        self.chk = Checkbutton(self.stepsGen_frame, text='Finish both feet', var=self.chk_state)
        self.chk.grid(row=5, column=8)

        # More text entries
        self.stepLength = Label(self.stepsGen_frame, text="Step length")
        self.stepLength.grid(row=6, column=8)
        self.stepLength_txt = Entry(self.stepsGen_frame, width=10)
        self.stepLength_txt.grid(row=6, column=9)

        self.stepHeight = Label(self.stepsGen_frame, text="Step height")
        self.stepHeight.grid(row=7, column=8)
        self.stepHeight_txt = Entry(self.stepsGen_frame, width=10)
        self.stepHeight_txt.grid(row=7, column=9)

        self.timeStep = Label(self.stepsGen_frame, text="Time of step")
        self.timeStep.grid(row=8, column=8)
        self.timeStep_txt = Entry(self.stepsGen_frame, width=10)
        self.timeStep_txt.grid(row=8, column=9)

        self.ts = Label(self.stepsGen_frame, text="Ts")
        self.ts.grid(row=9, column=8)
        self.ts_txt = Entry(self.stepsGen_frame, width=10)
        self.ts_txt.grid(row=9, column=9)

        self.doubleSupp = Label(self.stepsGen_frame, text="% Double support")
        self.doubleSupp.grid(row=10, column=8)
        self.doubleSupp_txt = Entry(self.stepsGen_frame, width=10)
        self.doubleSupp_txt.grid(row=10, column=9)

        self.d = Label(self.stepsGen_frame, text="d")
        self.d.grid(row=11, column=8)
        self.d_txt = Entry(self.stepsGen_frame, width=10)
        self.d_txt.grid(row=11, column=9)

        # Generate & Reset Buttons
        self.generateButton = Button(self.stepsGen_frame, text="Generate", command=self.generate_clicked)
        self.generateButton.grid(row=12, column=8, sticky=W+E)
        #self.generateButton.configure(background='#28b0b1')

        self.resetButton = Button(self.stepsGen_frame, text="Reset", command=self.reset_clicked)
        self.resetButton.grid(row=12, column=9, sticky=W+E)

        ######## LabelFrame for Local Motion
        self.localMotion_frame = LabelFrame(window, text="Local Motion", font=self.customFont)
        self.localMotion_frame.grid(row=13, column=0, rowspan=5, columnspan=3)

        # Local Motion
        self.feet = Label(self.localMotion_frame, text="Feet")
        self.feet.grid(row=14, column=0)
        self.data_localMotion = ("Polynomial 1", "Polynomial 2", "Polynomial 3")
        #self.feet_txt = Combobox(self.localMotion_frame, values=self.data_localMotion)
        self.init_var = StringVar(self.localMotion_frame)
        self.init_var.set(" ")  # default value
        self.feet_txt = OptionMenu(self.localMotion_frame, self.init_var, *self.data_localMotion)
        self.feet_txt.grid(row=14, column=1)
        self.feet_txt.configure(width=9)

        self.ZMP = Label(self.localMotion_frame, text="ZMP")
        self.ZMP.grid(row=15, column=0)

        self.CoG = Label(self.localMotion_frame, text="C0G")
        self.CoG.grid(row=16, column=0)
        #self.CoG_txt = Combobox(self.localMotion_frame, values=self.data_localMotion)
        self.init_var = StringVar(self.localMotion_frame)
        self.init_var.set(" ")  # default value
        self.CoG_txt = OptionMenu(self.localMotion_frame, self.init_var, *self.data_localMotion)
        self.CoG_txt.grid(row=15, column=1)
        self.CoG_txt.configure(width=9)

        self.arms = Label(self.localMotion_frame, text="Arms")
        self.arms.grid(row=17, column=0)
        #self.arms_txt = Combobox(self.localMotion_frame, values=self.data_localMotion)
        self.init_var = StringVar(self.localMotion_frame)
        self.init_var.set(" ")  # default value
        self.arms_txt = OptionMenu(self.localMotion_frame, self.init_var, *self.data_localMotion)
        self.arms_txt.grid(row=17, column=1)
        self.arms_txt.configure(width=9)

        # Trajectory Buttons
        self.feet_traj_button = Button(self.localMotion_frame, text="Feet Trajectory", command=self.feet_traj_button)
        self.feet_traj_button.grid(row=14, column=2)

        self.ZMP_traj_button = Button(self.localMotion_frame, text="ZMP Trajectory", command=self.ZMP_traj_button)
        self.ZMP_traj_button.grid(row=15, column=2)

        self.CoG_traj_button = Button(self.localMotion_frame, text="ZMP Trajectory", command=self.CoG_traj_button)
        self.CoG_traj_button.grid(row=16, column=2)

        self.arms_traj_button = Button(self.localMotion_frame, text="Arms Trajectory", command=self.arms_traj_button)
        self.arms_traj_button.grid(row=17, column=2)

        ######## LabelFrame for CoG Generation
        self.CoGgeneration_frame = LabelFrame(window, text="CoG Generation", font=self.customFont)
        self.CoGgeneration_frame.grid(row=13, column=3, rowspan=5, columnspan=4, sticky=N+S)

        self.Lambda = Label(self.CoGgeneration_frame, text="Lambda")
        self.Lambda.grid(row=14, column=3)
        self.Lambda_txt = Entry(self.CoGgeneration_frame, width=5)
        self.Lambda_txt.grid(row=14, column=4)

        self.zc = Label(self.CoGgeneration_frame, text="Zc (m)")
        self.zc.grid(row=14, column=5)
        self.zc_txt = Entry(self.CoGgeneration_frame, width=5)
        self.zc_txt.grid(row=14, column=6)

        self.beta = Label(self.CoGgeneration_frame, text="Beta")
        self.beta.grid(row=15, column=3)
        self.beta_txt = Entry(self.CoGgeneration_frame, width=5)
        self.beta_txt.grid(row=15, column=4)

        self.g = Label(self.CoGgeneration_frame, text="g (m/s2)")
        self.g.grid(row=15, column=5)
        self.g_txt = Entry(self.CoGgeneration_frame, width=5)
        self.g_txt.grid(row=15, column=6)

        self.alpha = Label(self.CoGgeneration_frame, text="Alpha")
        self.alpha.grid(row=16, column=3)
        self.alpha_txt = Entry(self.CoGgeneration_frame, width=5)
        self.alpha_txt.grid(row=16, column=4)

        self.dash = Label(self.CoGgeneration_frame, text="-")
        self.dash.grid(row=16, column=5)
        self.dash_txt = Entry(self.CoGgeneration_frame, width=5)
        self.dash_txt.grid(row=16, column=6)

        ######## LabelFrame for Plots
        self.plots_frame = LabelFrame(window, text="Plots", font=self.customFont)
        self.plots_frame.grid(row=13, column=7, rowspan=5, sticky=N+S)
        self.plots_frame.grid_rowconfigure(14, weight=1)
        self.plots_frame.grid_rowconfigure(15, weight=1)

        self.whole_traj_button = Button(self.plots_frame, text="Whole trajectory", command=self.whole_traj_clicked)
        self.whole_traj_button.grid(row=14, column=7)

        self.feet_traj_button = Button(self.plots_frame, text="Feet trajectory", command=self.feet_traj_button)
        self.feet_traj_button.grid(row=15, column=7)

        ######## LabelFrame for Joints Space
        self.jointsSpace_frame = LabelFrame(window, text="Joints Space", font=self.customFont)
        self.jointsSpace_frame.grid(row=13, column=8, rowspan=5, sticky=N+S)
        self.jointsSpace_frame.grid_rowconfigure(14, weight=2)
        self.jointsSpace_frame.grid_rowconfigure(15, weight=1)
        self.jointsSpace_frame.grid_columnconfigure(8, weight=1)

        self.stepBystep_button = Button(self.jointsSpace_frame, text="Step by step", command=self.stebBystep_clicked)
        self.stepBystep_button.grid(row=14, column=8, sticky=W+E)

        ######## LabelFrame for Visualization
        self.visualiz_frame = LabelFrame(window, text="Visualization", font=self.customFont)
        self.visualiz_frame.grid(row=13, column=9, rowspan=5, sticky=N+S)
        self.visualiz_frame.grid_rowconfigure(14, weight=1)
        self.visualiz_frame.grid_rowconfigure(15, weight=1)

        self.matlab_button = Button(self.visualiz_frame, text="MATLAB visualization", command=self.matlab_clicked)
        self.matlab_button.grid(row=14, column=9)

        self.ros_button = Button(self.visualiz_frame, text="ROS visualization", command=self.ros_clicked)
        self.ros_button.grid(row=15, column=9)

    def generate_clicked(self):
        self.lbl.configure(text='')

    def reset_clicked(self):
        self.numSteps_txt.delete(0,END)
        self.thetaVar_txt.delete(0,END)
        self.stepLength_txt.delete(0,END)
        self.stepHeight_txt.delete(0,END)
        self.timeStep_txt.delete(0,END)
        self.ts_txt.delete(0,END)
        self.doubleSupp_txt.delete(0,END)
        self.d_txt.delete(0,END)
        return

    def feet_traj_button(self):
        self.lbl.configure(text='')

    def ZMP_traj_button(self):
        self.lbl.configure(text='')

    def CoG_traj_button(self):
        self.lbl.configure(text='')

    def arms_traj_button(self):
        self.lbl.configure(text='')

    def stebBystep_clicked(self): # changes matplotlib chart
        self.lbl.configure(text='')
        # fig2 = Figure(figsize=(4, 4), dpi=100)
        # t = np.arange(0, 5, .01)
        # fig2.add_subplot(121).plot(t, 2.5 * np.cos(1.23 * np.pi * t))
        # canvas2 = FigureCanvasTkAgg(fig2, master=window)  # A tk.DrawingArea.
        # canvas2.draw()
        # canvas2.get_tk_widget().grid(row=1, column=0, rowspan=12, columnspan=8, sticky=E + W)

    def matlab_clicked(self): # opens new window
        matlab_window = Toplevel(self.visualiz_frame)
        matlab_window.title("MATLAB visualization")
        matlab_window.geometry("898x553")

    def ros_clicked(self): # opens new window
        ros_window = Toplevel(self.visualiz_frame)
        ros_window.title("ROS visualization")
        ros_window.geometry("898x553")

    def whole_traj_clicked(self):
        self.lbl.configure(text='')

    def feet_traj_clicked(self):
        self.lbl.configure(text='')




def main():
    window = Tk()
    win = TeoStepsGen(window)
    window.title("TEO Steps Generator")
    window.geometry("898x553")

    window.mainloop()


if __name__ == '__main__':
    main()
