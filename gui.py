import tkinter as tk
import tkinter.font as tkFont
import ctypes
import json
from PyQt5.QtWidgets import QMessageBox

#Pocetak GUi
def app_options():
    def poruka(tekst):
        pass
    def BTime_command():
        try:
            int(e3_value.get())
            # dalje
            TimeNumber["text"] = e3_value.get()
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, u"Morate uneti broj!", u"Error", 0)
            #poruka("Aloo")

    def BMax_command():
        try:
            int(e1_value.get())
            # dalje
            maxNumber["text"] = e1_value.get()
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, u"Morate uneti broj!", u"Error", 0)
            #QMessageBox.about("Title", "Message")

    def BMin_command():
        try:
            int(e2_value.get())
            # dalje
            minNumber["text"] = e2_value.get()
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, u"Morate uneti broj!", u"Error", 0)

    def save_changes_command():
        min = minNumber["text"]
        max = maxNumber["text"]

        if int(min) < 2 or int(max) > 100 or int(min) > int(max):
            ctypes.windll.user32.MessageBoxW(0, u"Uneli ste pogrešan min/max!!!", u"Error", 0)
        else:
        
            config["vreme"] = TimeNumber["text"]
            config["min"] = minNumber["text"]
            config["max"] = maxNumber["text"]
            with open("config.json", "r+") as jsonFile:
                jsonFile.seek(0)  # rewind
                json.dump(config, jsonFile)
                jsonFile.truncate()
            
            



    with open("config.json", "r") as jsonFile:
        config = json.load(jsonFile)
    root = tk.Tk()
    root.iconbitmap(default='icon.ico')
    root.iconbitmap("icon.ico")
    root.title("Options")
    #setting window size
    width=550
    height=270
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    GLabel_658=tk.Label(root)
    ft = tkFont.Font(family='Times',size=41)
    GLabel_658["font"] = ft
    GLabel_658["fg"] = "#333333"
    GLabel_658["justify"] = "center"
    GLabel_658["text"] = "Options"
    GLabel_658.place(x=30,y=10,width=261,height=70)

    e1_value = tk.StringVar()
    e1 = tk.Entry(root, textvariable=e1_value)
    e1["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    e1["font"] = ft
    e1["fg"] = "#333333"
    e1["justify"] = "center"
    e1.place(x=180,y=110,width=70,height=25)

    e2_value= tk.StringVar()
    e2=tk.Entry(root)
    e2["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    e2["font"] = ft
    e2["fg"] = "#333333"
    e2["justify"] = "center"
    e2["textvariable"] = e2_value
    e2.place(x=60,y=110,width=70,height=25)

    e3_value=tk.StringVar()
    ETime=tk.Entry(root,textvariable= e3_value)
    ETime["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    ETime["font"] = ft
    ETime["fg"] = "#333333"
    ETime["justify"] = "center"
    ETime.place(x=120,y=190,width=70,height=25)

    BMin=tk.Button(root)
    BMin["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    BMin["font"] = ft
    BMin["fg"] = "#000000"
    BMin["justify"] = "center"
    BMin["text"] = "Min"
    BMin.place(x=60,y=140,width=70,height=25)
    BMin["command"] = BMin_command

    BMax=tk.Button(root)
    BMax["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    BMax["font"] = ft
    BMax["fg"] = "#000000"
    BMax["justify"] = "center"
    BMax["text"] = "Max"
    BMax.place(x=180,y=140,width=70,height=25)
    BMax["command"] = BMax_command



    BTime=tk.Button(root)
    BTime["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    BTime["font"] = ft
    BTime["fg"] = "#000000"
    BTime["justify"] = "center"
    BTime["text"] = "Time"
    BTime.place(x=120,y=220,width=70,height=25)
    BTime["command"] = BTime_command

    TimeNumber=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    TimeNumber["font"] = ft
    TimeNumber["fg"] = "#333333"
    TimeNumber["justify"] = "center"
    TimeNumber["text"] = int(config["vreme"])#"TimeNumber"
    TimeNumber.place(x=450,y=210,width=70,height=25)

    TimeL=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    TimeL["font"] = ft
    TimeL["fg"] = "#333333"
    TimeL["justify"] = "center"
    TimeL["text"] = "Time:"
    TimeL.place(x=370,y=210,width=70,height=25)

    maxL=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    maxL["font"] = ft
    maxL["fg"] = "#333333"
    maxL["justify"] = "center"
    maxL["text"] = "Max:"
    maxL.place(x=370,y=110,width=70,height=25)

    maxNumber=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    maxNumber["font"] = ft
    maxNumber["fg"] = "#333333"
    maxNumber["justify"] = "center"
    maxNumber["text"] = config['max'] #"MaxNumebr"
    maxNumber.place(x=450,y=110,width=70,height=25)

    minL=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    minL["font"] = ft
    minL["fg"] = "#333333"
    minL["justify"] = "center"
    minL["text"] = "Min:"
    minL.place(x=370,y=150,width=70,height=25)

    minNumber=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    minNumber["font"] = ft
    minNumber["fg"] = "#333333"
    minNumber["justify"] = "center"
    minNumber["text"] = config['min'] #"MinNumebr"
    minNumber.place(x=450,y=150,width=70,height=25)

    save_changes=tk.Button(root)
    save_changes["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    save_changes["font"] = ft
    save_changes["fg"] = "#000000"
    save_changes["justify"] = "center"
    save_changes["text"] = "Save Changes"
    save_changes.place(x=370,y=20,width=152,height=48)
    save_changes["command"] = save_changes_command



    root.mainloop()
#KRAJ GUI
#app_options()
