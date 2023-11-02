from tkinter import *
from datetime import datetime, timezone
import time

root = Tk()
root.title('World Clock')
root.minsize(450, 450)
root.configure(background = 'snow')

lblTime = Label(root, text = '', bg = 'light blue')
lblTime.place(relx = 0.5, rely = 0.45, anchor = CENTER)

def getTime():
    timeStr = str(datetime.now())
    timeStr = timeStr[ int(timeStr.index(' ')) + 1 : -1]
    timeStr = timeStr[ 0: int(timeStr.index('.')) ] 
    lblTime['text'] = timeStr

btnTime = Button(root, text = 'Get Current Time', command = lambda: getTime())
btnTime.place(relx = 0.5, rely = 0.55, anchor = CENTER)

root.mainloop()