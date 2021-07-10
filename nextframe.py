import tkinter as tk
from backend import *
import MyTkWindow 
from tkinter import *
from tkinter import filedialog, Listbox, ttk, messagebox


class SecondFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.parent = parent
        self.CreateFrameDimensions()
        self.CreateDashboard()
        self.CreateTableFrame()
        self.CreateButtons()
        self.CreateTable()
        self.DisplayClientData()
        self.CreateDashboardButtons()


    def CreateDashboard(self):
        self.dashboard_frame = tk.Frame(self, bg="#eaffbf")
        self.dashboard_frame.place(height=1000,width=200, x=0,y=0)
    
    def CreateTableFrame(self):
        self.table_frame = tk.Frame(self, bg="white")
        self.table_frame.place(height=350,width=550, x=250,y=75)

    def CreateFrameDimensions(self):
        canvas = tk.Canvas(self, height= 900, width=1300, bg="red")
        canvas.pack()

    def CreateDashboardButtons(self):
        return_button = tk.Button(self.dashboard_frame, text="Back",command=lambda: self.parent.switch_frame(MyTkWindow.FirstFrame))#self.destroy(), self.first_frame.pack(), self.first_frame.start()])
        return_button.place(height=40,width=120, x=40, y=30) 
        dashboard_button_list = []
        dashboard_button_x_location = 40
        dashboard_button_y_location = 50

        for i in range (len(self.list_of_clients_keys)):
            dashboard_button_list.append(tk.Button(self.dashboard_frame, text = self.list_of_clients_keys[i],fg="black", bg="#eaffbf",highlightcolor="red", height=3)) #TODO lägg till command
            dashboard_button_list[i].place(height=40,width=150, x=dashboard_button_x_location, y=dashboard_button_y_location)
            dashboard_button_y_location = dashboard_button_y_location + 50


    def CreateButtons(self):
        export_button = tk.Button(self, text = "Export invoices", background="grey",height=5)
        export_button.place(height=40,width=120, x=1100, y=755)

        clear_all_button = tk.Button(self, text = "Clear all", background="grey",height=5)
        clear_all_button.place(height=40,width=120, x=639, y=194)

        clear_button = tk.Button(self, text = "Clear marked lines", background="grey",height=5)
        clear_button.place(height=40,width=120, x=639, y=244)


    def CreateTable(self):
        self.table1= ttk.Treeview(self.table_frame)
        self.table1.place(relheight=1, relwidth=1)
        self.table1["column"] = ["Client name","Hours"]
        self.table1["show"] = "headings"
        for column in self.table1["columns"]:
            self.table1.heading(column, text=column)
        treescrolly = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table1.yview)
        treescrollx = tk.Scrollbar(self.table_frame, orient="horizontal", command=self.table1.xview)
        self.table1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        # treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")


    def DisplayClientData(self): # This function is activated when you press the export button

    # if ImportTojReport(current_url) == -1:
    #     File_Not_Found_Error(current_url)
    # else:
        clients_of_the_month = ImportTojReport()
        self.list_of_clients_keys = list(clients_of_the_month.keys())
        self.list_of_clients_values = list(clients_of_the_month.values())

 
        for i in range(len(self.list_of_clients_keys)):
            self.table1.insert(parent="",index="end", values=(self.list_of_clients_keys[i],self.list_of_clients_values[i])) #iid är bra att hålla koll på, det ger id i listan, allstå vart i listan saken befinner sig 
        print("clients arranged")




    # for i in range (len(list_of_clients_keys)):
    #     dashboard_buttons.append(tk.Button(dashboard_frame, text = list_of_clients_keys[i],fg="black", bg="#eaffbf",highlightcolor="red", height=3, command=lambda: SwitchToFrameThree(frame_three,dashboard_frame))) #TODO lägg till command
    #     dashboard_buttons[i].place(height=40,width=150, x=dashboard_button_x_location, y=dashboard_button_y_location)
    #     dashboard_button_y_location = dashboard_button_y_location + 50


    #def start(self):
    #    self.mainloop()



                # export_button = tk.Button(frame_two, text = "I am lucky, export all", background="grey",height=5)
        # export_button.place(height=40,width=120, x=1100, y=800)