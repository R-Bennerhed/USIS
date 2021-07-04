import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from backend import*
from GUI_helper_function import*



################################################### Creates button that will switch to frame 2 #######################################################
def SwitchFrameButton(frame_one, frame_two,table1):
    switch_frame_button = tk.Button(frame_one, text = "Select properties", background="grey",height=5, command= lambda: SelectProperties(frame_two,table1))
    switch_frame_button.place(height=40,width=120, x=1035, y=400)


    # switch_frame_button = tk.Button(frame_one, text = "Select Properties", background="grey",height=5, command= lambda: SelectPropertiesFrame(frame_two))
    # switch_frame_button.place(height=80,width=120, x=639, y=464)




########################################################### I collect all functions that creates a button/field/table or anything that will lead to another function into frame 1  #####################################




def CreateButtonsFrameOne(frame_one, url_box, root):
    # export_button = tk.Button(frame_one, text = "Select Properties", background="grey",height=5,command= lambda:  GetTojFile(url_box.get(),1)) # Take value in the box where you pleace your URL as well as the table
    # export_button.place(height=40,width=120, x=1035, y=400)

    browse_button = tk.Button(frame_one, text = "Browse", background="grey",height=5, command= lambda: GetUrl(url_box))
    browse_button.place(height=40,width=120, x=910, y=400) 
    
    # export_button = tk.Button(frame_one, text = "Export", background="grey",height=5,command= lambda:  GetTojFile(url_box.get(),1)) # Take value in the box where you pleace your URL as well as the table
    # export_button.place(height=40,width=120, x=767, y=114)

    # browse_button = tk.Button(frame_one, text = "Browse", background="grey",height=5, command= lambda: GetUrl(url_box))
    # browse_button.place(height=40,width=120, x=639, y=114)

    # clear_all_button = tk.Button(frame_one, text = "Clear all", background="grey",height=5, command= lambda: ClearAllData(table1))
    # clear_all_button.place(height=40,width=120, x=639, y=194)

    # clear_button = tk.Button(frame_one, text = "Clear marked lines", background="grey",height=5, command= lambda: ClearRows(table1))
    # clear_button.place(height=40,width=120, x=639, y=244)

    # add_client = tk.Button(frame_one, text = "Add client to table", background="grey",height=5, command= lambda: ClearData(table1))
    # add_client.place(height=40,width=120, x=639, y=284)




def CreateLablesFrameOne(frame_one):
    export_instructions = tk.Label(frame_one, text = "Please enter filepath to TOJ file;", bg="grey")
    export_instructions.place(height=15,width=165, x=353,y=380)

def CreateEntry(frame_one):
    url_box = tk.Entry(frame_one, bg="white")
    url_box.place(height=40,width=550, x=350,y=400)
    return url_box

# def CreateTables(client_overview_frame):
#     table1= ttk.Treeview(client_overview_frame)
#     table1.place(relheight=1, relwidth=1)
#     table1["column"] = ["Client name","Hours"]
#     table1["show"] = "headings"
#     for column in table1["columns"]:
#         table1.heading(column, text=column)
#     treescrolly = tk.Scrollbar(  client_overview_frame, orient="vertical", command=table1.yview)
#     treescrollx = tk.Scrollbar(  client_overview_frame, orient="horizontal", command=table1.xview)
#     table1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
#     # treescrollx.pack(side="bottom", fill="x")
#     treescrolly.pack(side="right", fill="y")
#     return table1

########################################################### Above, I collect all functions that creates a button/field/table or anything that will lead to another function into frame 1 #####################################

############################################################ Bellow, functions that generates a value or use inputs to generate something new ################################################################################

def GetTojFile(entry,table1): # This function is activated when you press the export button

    if ImportTojReport(entry) == -1:
        File_Not_Found_Error(entry)
    else:
        clients_of_the_month = ImportTojReport(entry)
        list_of_clients_keys = list(clients_of_the_month.keys())
        list_of_clients_values = list(clients_of_the_month.values())
 
        for i in range(len(list_of_clients_keys)):
            print("i forlooopen ------------------")
            table1.insert(parent="",index="end", values=(list_of_clients_keys[i],list_of_clients_values[i])) #iid är bra att hålla koll på, det ger id i listan, allstå vart i listan saken befinner sig 


def GetUrl(url_box):
    file=filedialog.askopenfilename(title="Select file", filetype=(("xlsx files", ".xlsx .xls"),("All Files", "*.*")))  #Do not forget to set a convenient initial directory (initialdr="/")
    url_box.insert(0, str(file))
    url= str(file)
    SetUrl(url)



    ############################################################ Above, functions that generates a value or use inputs to generate something new ################################################################################
