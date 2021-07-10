import tkinter as tk
from MyTkWindow import *


class SecondFrame(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        
        self.first_frame = parent

        self.CreateFrameDimensions()
        self.CreateDashboard()
        self.CreateButtons()


    def CreateDashboard(self):
        self.dashboard_frame = tk.Frame(self, bg="#eaffbf")
        self.dashboard_frame.place(height=1000,width=200, x=0,y=0)

    def CreateFrameDimensions(self):
        canvas = tk.Canvas(self, height= 900, width=1300, bg="red")
        canvas.pack()

    def CreateButtons(self):
        return_button = tk.Button(self.dashboard_frame, text="Back",command=lambda:self.destroy())
        return_button.place(height=40,width=120, x=40, y=30) 

        # export_button = tk.Button(frame_two, text = "Export invoices", background="grey",height=5)
        # export_button.place(height=40,width=120, x=1100, y=755)

        # clear_all_button = tk.Button(frame_two, text = "Clear all", background="grey",height=5, command= lambda: ClearAllData(table1))
        # clear_all_button.place(height=40,width=120, x=639, y=194)

        # clear_button = tk.Button(frame_two, text = "Clear marked lines", background="grey",height=5, command= lambda: ClearRows(table1)
        # clear_button.place(height=40,width=120, x=639, y=244)



    def start(self):
        self.mainloop()



                # export_button = tk.Button(frame_two, text = "I am lucky, export all", background="grey",height=5)
        # export_button.place(height=40,width=120, x=1100, y=800)