import tkinter as tk
# from tkinter import filedialog, Listbox, ttk, messagebox
# from tkinter import *
# from tkinter.constants import ANCHOR
import MyTkWindow 
from backend import *


# HEIGHT = 900
# WIDTH = 1300
# current_frame = 0

#root = FirstFrame()
#root.pack()
# root.title("Super advanced invocing system")

#root.start()


# canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH)
# canvas.pack()


app = SampleApp(MyTkWindow.FirstFrame)
app.mainloop()

# root.mainloop()
