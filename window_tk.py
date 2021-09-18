from tkinter import *


def msg():
    lbl.configure(text='Download success.')


window = Tk()
window.title('youtuber')
window.geometry('200x90')

lbl = Label(window, text='insert video link', font=("FreeMono", 10)).pack(side=TOP)

entry_link = Entry(window)
entry_link.pack(side=TOP)

widget = Button(window, text='audio', font=("FreeMono", 10), command=msg)
widget.pack(side=RIGHT)

widget = Button(window, text='video', font=("FreeMono", 10), command=msg)
widget.pack(side=LEFT)

window.mainloop()