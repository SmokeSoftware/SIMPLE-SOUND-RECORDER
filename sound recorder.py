import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sounddevice as sd
import soundfile as sf

Effector = tk.Tk()
Effector.title("SOUND RECORDER")
Effector.minsize(400,200)
Effector.maxsize(400,200)

def RECORDER_ACTİVE():
    try:
        time = int(RECORDER_TİME_İNPUT_AREA.get())

    except Exception as e:
        nomsg = Tk()
        nomsg.withdraw()
        messagebox.showerror("ERROR!","SOMETHİNG'S WRONG!\nPLEASE TRY AGAİN!")
        
    try:
        record = sd.rec(int(time * 44100), samplerate = 44100, channels = 2)
        sd.wait()
        record_name = str(filedialog.asksaveasfilename())+".wav"
        if record_name is None:
            return record_name
        
        sf.write(str(record_name), record, 44100)
        yesmsg = Tk()
        yesmsg.withdraw()
        messagebox.showinfo("İMFORMATİON","RECORDİNG İS COMPLETED!\n" + str(record_name))

    except Exception as e:
        nomsg = Tk()
        nomsg.withdraw()
        messagebox.showerror("ERROR!","SOMETHİNG'S WRONG!\nPLEASE TRY AGAİN!")

RECORDER_START_BUTTON = tk.Button(Effector,text = "START",fg = "lime",bg = "black",activebackground = "black",activeforeground = "lime",font = "Arial 80",command = RECORDER_ACTİVE)
RECORDER_START_BUTTON.place(width = 400,height = 100,x = 0,y = 100)

RECORDER_TİME_İNPUT_AREA_İNFO = tk.Label(Effector,text = "ENTER THE\n TİME:",fg = "blue",bg = "white",font = "Arial 20")
RECORDER_TİME_İNPUT_AREA_İNFO.place(width = 200,height = 100,x = 0,y = 0)

RECORDER_TİME_İNPUT_AREA = tk.Entry(Effector,fg = "blue",bg = "white",font = "Arial 60")
RECORDER_TİME_İNPUT_AREA.place(width = 200,height = 100,x = 200,y = 0)

Effector.mainloop()
