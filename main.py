import tkinter as tk
import tkinter.ttk as ttk
import pyqrcodeng
from time import sleep

class GuiApp:
    def __init__(self, master=None):
        def qrgen():
            url = pyqrcodeng.create(linkbox.get())
            url.png(namebox.get() + '.png', scale = 6)

        self.window = tk.Tk() if master is None else tk.Toplevel(master)
        self.window.configure(background="#525f98", height=200, width=200)
        self.window.geometry("320x200")
        self.window.resizable(False, False)
        label1 = ttk.Label(self.window)
        label1.configure(
            anchor="center",
            background="#000000",
            font="{Arial} 24 {bold underline}",
            foreground="#ffffff",
            padding=0,
            text='QR Code Generator')
        label1.place(
            anchor="nw",
            relheight=0.25,
            relwidth=1.0,
            relx=0.0,
            rely=0.0,
            x=0,
            y=0)
        label2 = ttk.Label(self.window)
        label2.configure(
            background="#525f98",
            font="{Arial} 12 {bold}",
            foreground="#ffffff",
            text='Your Link/numbers(or anything else)')
        label2.place(anchor="center", relx=0.5, rely=0.31, x=0, y=0)
        linkbox = ttk.Entry(self.window, name="linkbox")
        linkbox.place(
            anchor="center",
            relwidth=0.92,
            relx=0.5,
            rely=0.42,
            x=0,
            y=0)
        label3 = ttk.Label(self.window)
        label3.configure(
            background="#525f98",
            font="{Arial} 12 {bold}",
            foreground="#ffffff",
            text='Name of your QR Code file')
        label3.place(anchor="center", relx=0.5, rely=0.55, x=0, y=0)
        namebox = ttk.Entry(self.window, name="namebox")
        namebox.place(
            anchor="center",
            relwidth=0.92,
            relx=0.5,
            rely=0.66,
            x=0,
            y=0)
        generatebutton = ttk.Button(self.window, name="generatebutton")
        generatebutton.configure(text='GENERATE', command = qrgen)
        generatebutton.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.83,
            x=0,
            y=0)

        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GuiApp()
    app.run()
