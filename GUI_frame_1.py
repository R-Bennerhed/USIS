import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from backend import*
from GUI_helper_function import*



################################################### Creates button that will switch to frame 2 #######################################################
def SwitchFrameButton(frame_one, frame_two,frame_three,table1, dashboard_frame):
    switch_frame_button = tk.Button(frame_one, text = "Select properties", background="grey",height=5, command= lambda: SwitchToFrameTwo(frame_two, frame_three, table1,dashboard_frame))
    switch_frame_button.place(height=40,width=120, x=1035, y=400)


    # switch_frame_button = tk.Button(frame_one, text = "Select Properties", background="grey",height=5, command= lambda: SelectPropertiesFrame(frame_two))
    # switch_frame_button.place(height=80,width=120, x=639, y=464)




########################################################### I collect all functions that creates a button/field/table or anything that will lead to another function into frame 1  #####################################




def CreateButtonsFrameOne(frame_one, url_box, root):
    # export_button = tk.Button(frame_one, text = "Select Properties", background="grey",height=5,command= lambda:  GetTojFile(url_box.get(),1)) # Take value in the box where you pleace your URL as well as the table
    # export_button.place(height=40,width=120, x=1035, y=400)

    browse_button = tk.Button(frame_one, text = "Browse", background="grey",height=5, command= lambda: GetUrl(url_box))
    browse_button.place(height=40,width=120, x=910, y=400) 

def CreateLablesFrameOne(frame_one):
    export_instructions = tk.Label(frame_one, text = "Please enter filepath to TOJ file;", bg="grey")
    export_instructions.place(height=15,width=165, x=353,y=380)

def CreateEntry(frame_one):
    url_box = tk.Entry(frame_one, bg="white")
    url_box.place(height=40,width=550, x=350,y=400)
    return url_box


########################################################### Above, I collect all functions that creates a button/field/table or anything that will lead to another function into frame 1 #####################################

############################################################ Bellow, functions that generates a value or use inputs to generate something new ################################################################################


def GetUrl(url_box):
    file=filedialog.askopenfilename(title="Select file", filetype=(("xlsx files", ".xlsx .xls"),("All Files", "*.*")))  #Do not forget to set a convenient initial directory (initialdr="/")
    url_box.insert(0, str(file))
    url= str(file)
    SetUrl(url)



    ############################################################ Above, functions that generates a value or use inputs to generate something new ################################################################################
