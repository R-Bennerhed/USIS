import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox

from tkinter import *
from tkinter.constants import ANCHOR
from nextframe import *

class FirstFrame(tk.Frame):
    def __init__(self, parent=None):
        self.frame=tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.second_frame = SecondFrame()
        self.CreateFrameDimensions()
        self.CreateURLTextField()
        self.CreateButtons()
        self.CreateLables()

        
        
    def start(self):
        print("hej")
        self.mainloop()

    
    def CreateFrameDimensions(self):
        self.canvas = tk.Canvas(self, height= 900, width=1300,bg="green")
        self.canvas.pack()
        

    def CreateButtons(self):
        browse_button = tk.Button(self, text = "Browse",height=5, command= lambda: self.DisplayBrowseWindow())
        browse_button.place(height=40,width=120, x=780, y=350) 
        next_screen_button = tk.Button(self, text="Next",command=lambda: [self.destroy(),self.second_frame.pack(),self.second_frame.start()])
        next_screen_button.place(height=40,width=120, x=910, y=350)

    def CreateURLTextField(self):
        self.URL_text_field = tk.Entry(self, bg="white")
        self.URL_text_field.place(height=40,width=550, x=220,y=350)


    def CreateLables(self):
        export_instructions = tk.Label(self, text = "Please enter filepath to TOJ file;")
        export_instructions.place(height=15,width=165, x=220,y=330)
        
        
    def DisplayBrowseWindow(self):
        file=filedialog.askopenfilename(title="Select file", filetype=(("xlsx files", ".xlsx .xls"),("All Files", "*.*")))  #Do not forget to set a convenient initial directory (initialdr="/")
        self.URL_text_field.insert(0, str(file))




    # def CreateButtons(self):
    #     browse_button = tk.Button(self, text = "Browse", background="grey",height=5) #command= lambda: GetUrl(url_box)
    #     browse_button.place(height=40,width=120, x=910, y=400) 
    #     next_screen = tk.Button(self, text="Next",command=lambda: [self.destroy(),nextWin.pack(),nextWin.start()])
    #     next_screen.pack()

