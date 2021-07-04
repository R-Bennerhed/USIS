import pandas as pd
import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from GUI_frame_1 import *
from GUI_frame_2 import *

HEIGHT = 900
WIDTH = 1300
current_frame = 0


root = tk.Tk()
root.title("Super advanced invocing system")



def CreateFrameOne(root):
    frame_one = tk.Frame(root, bg="grey")
    frame_one.place(height=900,width=1300)

    url_box = CreateEntry(frame_one)
    CreateButtonsFrameOne(frame_one, url_box,root)
    CreateLablesFrameOne(frame_one)
    return frame_one, url_box


def CreateFrameTwo(root):
    frame_two = tk.Frame(root, bg="red")
    # frame_two.place(height=900,width=1300)
    client_overview_frame = tk.Frame(frame_two, bg="white")
    client_overview_frame.place(height=350,width=550, x=250,y=75)
    dashboard_frame = tk.Frame(frame_two, bg="#eaffbf")
    dashboard_frame.place(height=1000,width=200, x=0,y=0)
    table1 = CreateTablesFrameTwo(client_overview_frame)
    CreateButtonsFrameTwo(root,frame_two,table1)





    # # data_base_viewer = tk.Frame(frame_two, bg="white")
    # # data_base_viewer.place(height=200,width=800, x=300,y=50)


    # print("hej, frame två skapad")
    # # CreateLablesFrameTwo(root,frame_two)
    # Client_data_table = CreateTablesFrameTwo(root,frame_two)
    return frame_two, table1


#########################bellow, frame 1#########################
canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

    

################### above frame 1##############################


frame_one, url_box = CreateFrameOne(root) # Creates the first frame
frame_two, table1 = CreateFrameTwo(root) # Crates the second frame
SwitchFrameButton(frame_one,frame_two,table1) # TODO! Might need frame_two in the future
root.mainloop()







