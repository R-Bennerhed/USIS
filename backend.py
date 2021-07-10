import pandas as pd
import datetime
import calendar
import os
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

import tkinter as tk
# from tkinter import filedialog, Listbox, ttk, messagebox
# from tkinter import *
# from tkinter.constants import ANCHOR
from MyTkWindow import *
from nextframe import *



current_url =""

def SetUrl(url):
    global current_url
    current_url = url 

def ImportTojReport(): #imports Monthly toj-report
    print(" I import tpj report                            ")
    print("current url", current_url)
    try:
        TOJ_report = pd.read_excel(current_url) #change this so one can upload a toj file in the future 
        print("Jag är inne i try")
        clients_of_the_month= TojScraping(TOJ_report)
        return clients_of_the_month #Clients of the months is a dictionary with clients name and associated hours

    except: 
        print("Error              !")
        return -1



def TojScraping(TOJ_report): 
    length = len(TOJ_report)
    clients_of_the_month = {}
    for i in range(length):
        current_client = TOJ_report.iloc[i,0]
        client_hours = TOJ_report.iloc[i,3]
        clients_of_the_month[current_client] = client_hours #By overwriting position for current_client several times, it will only leave the last row for the given client which contains total hours from TOJ
        print(clients_of_the_month)
    return clients_of_the_month
# This function returns a dictionary with client name and concerned total hours from TOJ

# def ImportDataBase(): #imports Monthly toj-report #funktion som öppnar databasen, retunerar hela databasen samt clienterna i en lista

#     database = pd.read_excel ("database.xlsx") #change this so one can upload a toj file in the future 
        
#     database_clients_name =  list(database['Client'])
#     return database, database_clients_name


# def main():
#     clients_of_the_month =ImportTojReport("C:/Users/robinbe/Desktop/Ultimate Super High Tech Invoicing System/toj.xlsx")
#     print(clients_of_the_month)

# main()


class SampleApp(tk.Tk):
    def __init__(self, start_frame):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(start_frame)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
