import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from backend import*



def CreateLablesFrameThree(data_base_viewer):  #Labels in dataviewer
    ########Row one#######
    client_name= tk.Label(data_base_viewer, text = "Client name;", bg="white", anchor="w")
    client_name.place(height=15,width=80, x=20,y=20)

    invoice_date= tk.Label(data_base_viewer, text = "Invoice date;", bg="white", anchor="w")
    invoice_date.place(height=15,width=85, x=20,y=55)
   
    our_reference = tk.Label(data_base_viewer, text = "Our Reference;", bg="white", anchor="w")
    our_reference.place(height=15,width=85, x=20,y=90)

    your_reference = tk.Label(data_base_viewer, text = "Your Reference;", bg="white", anchor="w")
    your_reference.place(height=15,width=85, x=20,y=125)
    
    total_hours= tk.Label(data_base_viewer, text = "Total Hours;", bg="white", anchor="w")
    total_hours.place(height=15,width=85, x=20,y=160)

    ########Row two#######   
    expiry_date= tk.Label(data_base_viewer, text = "Expiry;", bg="white",anchor="w")
    expiry_date.place(height=15,width=185, x=260,y=55)

    df_charge= tk.Label(data_base_viewer, text = "Df charge;", bg="white",anchor="w")
    df_charge.place(height=15,width=85, x=260,y=125)

    currency= tk.Label(data_base_viewer, text = "Currency;", bg="white",anchor="w")
    currency.place(height=15,width=85, x=260,y=160)

    ########Row three#######
    organization_number= tk.Label(data_base_viewer, text = "Organization nr;", bg="white",anchor="w")
    organization_number.place(height=15,width=95, x=485,y=20)

    adress= tk.Label(data_base_viewer, text = "Adress;", bg="white",anchor="w")
    adress.place(height=15,width=85, x=485,y=55)

    postal_code= tk.Label(data_base_viewer, text = "Postal Code;", bg="white",anchor="w")
    postal_code.place(height=15,width=85, x=485,y=90)

    city= tk.Label(data_base_viewer, text = "City;", bg="white",anchor="w")
    city.place(height=15,width=85, x=485,y=125)

    country= tk.Label(data_base_viewer, text = "Country;", bg="white",anchor="w")
    country.place(height=15,width=85, x=485,y=160)


def CreateEntriesFrameThree(data_base_viewer):#Entries in dataviewer

        ########Row one#######

    client_name_box = tk.Entry(data_base_viewer, bg="white")
    client_name_box.place(height=15,width=370, x=107,y=20)

    invoice_date_box = tk.Entry(data_base_viewer, bg="white")
    invoice_date_box.place(height=15,width=150, x=107,y=55)

    our_reference_box = tk.Entry(data_base_viewer, bg="white")
    our_reference_box.place(height=15,width=150, x=107,y=90)

    your_reference_box = tk.Entry(data_base_viewer, bg="white")
    your_reference_box.place(height=15,width=150, x=107,y=125)

    total_hours_box = tk.Entry(data_base_viewer, bg="white")
    total_hours_box.place(height=15,width=150, x=107,y=160)

 ########Row two#######   

     
    expiry_date_box= tk.Entry(data_base_viewer, bg="white")
    expiry_date_box.place(height=15,width=172, x=303,y=55)

    df_charge_box=(tk.Entry(data_base_viewer, bg="white"))
    df_charge_box.place(height=15,width=172, x=303,y=125)
    currency_box = (tk.Entry(data_base_viewer, bg="white"))
    currency_box.place(height=15,width=172, x=303,y=160)
    



    

    ########Row three#######
    organization_number_box= tk.Entry(data_base_viewer, bg="white")
    organization_number_box.place(height=15,width=120, x=580,y=20)

    adress_box = tk.Entry(data_base_viewer, bg="white")
    adress_box.place(height=15,width=120, x=580,y=55)

    postal_code_box = tk.Entry(data_base_viewer, bg="white")
    postal_code_box.place(height=15,width=120, x=580,y=90)

    city_box = tk.Entry(data_base_viewer, bg="white")
    city_box.place(height=15,width=120, x=580,y=125)

    country_box = tk.Entry(data_base_viewer, bg="white")
    country_box.place(height=15,width=120, x=580,y=160)

