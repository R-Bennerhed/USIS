import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from backend import*


current_url =""


def SwitchToFrameTwo(frame_two, table1, dashboard_frame):
    SetFrameTwo(frame_two,dashboard_frame)
    list_of_clients_keys, list_of_clients_values = GetTojFile(current_url,table1)
    CreateDashboardButtons(dashboard_frame,list_of_clients_keys, list_of_clients_values)

def SetUrl(url):
    global current_url
    current_url = url 

def SetFrameTwo(frame_two,dashboard_frame):
    frame_two.place(height=900,width=1300)
    dashboard_frame.place(height=1000,width=200, x=0,y=0)


def GetTojFile(current_url,table1): # This function is activated when you press the export button

    if ImportTojReport(current_url) == -1:
        File_Not_Found_Error(current_url)
    else:
        clients_of_the_month = ImportTojReport(current_url)
        list_of_clients_keys = list(clients_of_the_month.keys())
        list_of_clients_values = list(clients_of_the_month.values())

        number_of_clients = len(list_of_clients_keys)
 
        for i in range(len(list_of_clients_keys)):
            table1.insert(parent="",index="end", values=(list_of_clients_keys[i],list_of_clients_values[i])) #iid är bra att hålla koll på, det ger id i listan, allstå vart i listan saken befinner sig 
        print("clients arranged")
        return list_of_clients_keys, list_of_clients_values

def CreateDashboardButtons(dashboard_frame, list_of_clients_keys, list_of_clients_values):
    dashboard_buttons = []
    dashboard_button_x_location = 0
    dashboard_button_y_location = 50

    for i in range (len(list_of_clients_keys)):
        dashboard_buttons.append(tk.Button(dashboard_frame, text = list_of_clients_keys[i],fg="black", bg="#eaffbf",highlightcolor="red", height=3)) #TODO lägg till command
        dashboard_buttons[i].place(height=40,width=150, x=dashboard_button_x_location, y=dashboard_button_y_location)
        dashboard_button_y_location = dashboard_button_y_location + 50




def SwitchToFrameThree(frame_three, dashboard_frame):
    frame_three.place(height=900,width=1300)
    dashboard_frame.place(height=1000,width=200, x=0,y=0)






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




