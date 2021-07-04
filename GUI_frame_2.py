import tkinter as tk
from tkinter import filedialog, Listbox, ttk, messagebox
from tkinter import *
from tkinter.constants import ANCHOR
from backend import*
from GUI_helper_function import*


def CreateButtonsFrameTwo(root,frame_two,table1):
    print("hej")

    export_button = tk.Button(frame_two, text = "I am lucky, export all", background="grey",height=5)
    export_button.place(height=40,width=120, x=1100, y=800)
    
    export_button = tk.Button(frame_two, text = "Export invoices", background="grey",height=5)
    export_button.place(height=40,width=120, x=1100, y=755)

    
    clear_all_button = tk.Button(frame_two, text = "Clear all", background="grey",height=5, command= lambda: ClearAllData(table1))
    clear_all_button.place(height=40,width=120, x=639, y=194)

    clear_button = tk.Button(frame_two, text = "Clear marked lines", background="grey",height=5, command= lambda: ClearRows(table1))
    clear_button.place(height=40,width=120, x=639, y=244)


    # browse_button = tk.Button(frame_two, text = "Test2", background="blue",height=5)
    # browse_button.place(height=40,width=120, x=639, y=114)

    # clear_all_button = tk.Button(frame_two, text = "Test 3 all", background="white",height=5)
    # clear_all_button.place(height=40,width=120, x=639, y=194)

def CreateTablesFrameTwo(client_overview_frame):
    table1= ttk.Treeview(client_overview_frame)
    table1.place(relheight=1, relwidth=1)
    table1["column"] = ["Client name","Hours", "Our Reference"]
    table1["show"] = "headings"
    for column in table1["columns"]:
        table1.heading(column, text=column)
    treescrolly = tk.Scrollbar(  client_overview_frame, orient="vertical", command=table1.yview)
    treescrollx = tk.Scrollbar(  client_overview_frame, orient="horizontal", command=table1.xview)
    table1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    # treescrollx.pack(side="bottom", fill="x")
    treescrolly.pack(side="right", fill="y")
    return table1



# def CreateTablesFrameTwo(root, frame_two):
#     print("hej")
#     # table2= ttk.Treeview(frame_two)
#     # table2.place(relheight=0.5, relwidth=0.5)
#     # table2["column"] = ["Client name","Hours"]
#     # table2["show"] = "headings"
#     # for column in table2["columns"]:
#     #     table2.heading(column, text=column)
#     # treescrolly = tk.Scrollbar(frame_two, orient="vertical", command=table2.yview)
#     # treescrollx = tk.Scrollbar(frame_two, orient="horizontal", command=table2.xview)
#     # table2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
#     # # treescrollx.pack(side="bottom", fill="x")
#     # treescrolly.pack(side="right", fill="y")


