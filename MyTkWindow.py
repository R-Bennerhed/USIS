import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox

from tkinter import *
from tkinter.constants import ANCHOR
import nextframe
from backend import *

class FirstFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.parent = parent
        self.CreateFrameDimensions()
        self.CreateURLTextField()
        self.CreateButtons()
        self.CreateLables()

        
        
#    def start(self):
#        self.mainloop()

    
    def CreateFrameDimensions(self):
        self.canvas = tk.Canvas(self, height= 900, width=1300,bg="green")
        self.canvas.pack()
        

    def CreateButtons(self):
        browse_button = tk.Button(self, text = "Browse",height=5, command= lambda: self.DisplayBrowseWindow())
        browse_button.place(height=40,width=120, x=780, y=350) 
        next_screen_button = tk.Button(self, text="Next",command=lambda: [self.parent.switch_frame(nextframe.SecondFrame)]) 
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
        url= str(file)
        SetUrl(url)




    


    def File_Not_Found_Error(entry):
            print("Nu är vi i file not found error-funktionen")
            if entry == "":
                tk.messagebox.showerror("Something is wrong, stupid homan!", "Please browse URL; Allowed formats; Excel .xlsx and .xls")
            else:
                tk.messagebox.showerror("Something is wrong, stupid homan!", "The submitted URL is probably false")



    # def CreateButtons(self):
    #     browse_button = tk.Button(self, text = "Browse", background="grey",height=5) #command= lambda: GetUrl(url_box)
    #     browse_button.place(height=40,width=120, x=910, y=400) 
    #     next_screen = tk.Button(self, text="Next",command=lambda: [self.destroy(),nextWin.pack(),nextWin.start()])
    #     next_screen.pack()

