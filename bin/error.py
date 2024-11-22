from tkinter import *
from tkinter import ttk
# import OsType as IDEN

def ERROR(receive): 
    window = Tk()
    if receive == "UNKNOWN":
        ERRORMESSAGE = "Error Code 00 \nChrome (Chromium) is not installed."
        # Geometry and Style
        window.title("Serious Error Has Occured!")
        window.geometry("400x100")
        window.resizable(False, False)

        # Widgets

        # Text 
        txtError = Text(window, height = 5, width = 52)
        txtError = Label(window, text=ERRORMESSAGE)
        # Buttons
        btnShowLog = ttk.Button(text="Show Logs")
        btnExit = ttk.Button(text="Exit")

        # Placing of objects
        txtError.place(anchor=N)
        btnShowLog.place(anchor=SW)
        btnExit.place(anchor=SE)

        # Pack Widgets
        txtError.pack()
        btnExit.pack()
        btnShowLog.pack()

        # DONT CHANGE OR PASTE
        window.mainloop()

        

