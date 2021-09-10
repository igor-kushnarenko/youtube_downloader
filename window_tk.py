import tkinter as tk


def msg():
    print('Hello stdout')


top = tk.Frame()
top.pack()
tk.Label(top, text='youtube_downloader').pack(side=tk.TOP)
entry_link = tk.Entry(top)
entry_link.pack(side=tk.TOP)
widget = tk.Button(top, text='video', command=msg)
widget.pack(side=tk.BOTTOM)
widget = tk.Button(top, text='audio', command=msg)
widget.pack(side=tk.BOTTOM)

top.mainloop()