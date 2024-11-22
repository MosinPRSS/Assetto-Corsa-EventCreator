import tkinter as Tk
# import OsType as IDEN

def ERROR(receive): 
    window = Tk.Tk()
    if receive == "UNKNOWN":
        # Geometry and Style
        window.title("Serious Error Has Occured!")
        window.geometry("400x100")
        window.iconbitmap("applogo.ico")
        window.resizable(False, False)
        window.mainloop()
        

ERROR("UNKNOWN")
