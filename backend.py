import pandas as pd
import datetime
import calendar
import os
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook


def ImportTojReport(current_url): #imports Monthly toj-report
    print(" I import tpj report")
    try:
        url = str(current_url)
        TOJ_report = pd.read_excel (url) #change this so one can upload a toj file in the future 
        clients_of_the_month= TojScraping(TOJ_report)
        return clients_of_the_month

    except: 
        return -1



def TojScraping(TOJ_report): 
    length = len(TOJ_report)
    clients_of_the_month = {}
    for i in range(length):
        current_client = TOJ_report.iloc[i,0]
        client_hours = TOJ_report.iloc[i,3]
        clients_of_the_month[current_client] = client_hours #By overwriting position for current_client several times, it will only leave the last row for the given client which contains total hours from TOJ
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