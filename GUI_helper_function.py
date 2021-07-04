import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from backend import*


current_url =""


def SelectProperties(frame_two, table1):
    SetFrameTwo(frame_two)
    GetTojFile(current_url,table1)

def SetUrl(url):
    global current_url
    current_url = url 

def SetFrameTwo(frame_two):
    frame_two.place(height=900,width=1300)


def GetTojFile(current_url,table1): # This function is activated when you press the export button

    if ImportTojReport(current_url) == -1:
        File_Not_Found_Error(current_url)
    else:
        clients_of_the_month = ImportTojReport(current_url)
        list_of_clients_keys = list(clients_of_the_month.keys())
        list_of_clients_values = list(clients_of_the_month.values())
 
        for i in range(len(list_of_clients_keys)):
            print("i forlooopen ------------------")
            table1.insert(parent="",index="end", values=(list_of_clients_keys[i],list_of_clients_values[i])) #iid är bra att hålla koll på, det ger id i listan, allstå vart i listan saken befinner sig 




def ClearAllData(table1):
    for i in table1.get_children():
        table1.delete(i)

    
def ClearRows(table1):
        marked_rows = table1.selection()
        for i in marked_rows:
            table1.delete(i)
    


def File_Not_Found_Error(entry):
    print("Nu är vi i file not found error-funktionen")
    if entry == "":
        tk.messagebox.showerror("Something is wrong, stupid homan!", "Please browse URL; Allowed formats; Excel .xlsx and .xls")
    else:
        tk.messagebox.showerror("Something is wrong, stupid homan!", "The submitted URL is probably false")




