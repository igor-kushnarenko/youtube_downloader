from tkinter import *

from app import YouTubeDownloader


def video_download():
    link = entry_link.get()
    downloader = YouTubeDownloader(link)
    video = downloader.video_init()
    downloader.video_downloader(video)
    lbl['text'] = 'Sucsess'


def audio_download():
    link = entry_link.get()
    downloader = YouTubeDownloader(link)
    video = downloader.video_init()
    downloader.audio_downloader(video)
    lbl['text'] = 'Sucsess'


window = Tk()
window.title('youtuber')
window.geometry('200x100')

lbl = Label(window, text='insert video link', font=("FreeMono", 10))
lbl.grid(row=0, column=0)

entry_link = Entry(window, width=25)
entry_link.grid(row=1, column=0)

widget = Button(window, text='audio', font=("FreeMono", 10), command=audio_download)
widget.grid(row=2, column=0)

widget = Button(window, text='video', font=("FreeMono", 10), command=video_download)
widget.grid(row=3, column=0)

window.mainloop()