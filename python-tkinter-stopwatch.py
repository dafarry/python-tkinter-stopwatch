#!/usr/bin/env python3

import tkinter as tk
from enum import Enum
import time

class digitalclock(tk.Frame):
    def __init__(self, master=None, **kwords):
        super().__init__(master, **kwords)
        bframe = tk.Frame(self)
        bframe.pack()
        self.butn = Enum('butn', "Start Stop Reset Quit")
        for bname in self.butn:
            bcall = lambda action=bname: self.showtime(action)
            tk.Button(bframe, text=bname.name, command=bcall).pack(side="left")
        self.lab = tk.Label(self, text="00:00:00", bg=self.cget("bg"))
        self.lab.pack(side="bottom")
        self.showtime(self.butn.Reset)
    def showtime(self, *args):
        if args:
            act = args[0]
            if act == self.butn.Quit:
                self.run = False
                self.quit()
            elif act == self.butn.Reset:
                self.timer = 0.0
                self.run = False
                self.lab.config(text = "00:00:00")
            elif act == self.butn.Start and self.run == False:
                self.timer = time.time() - self.timer
                self.run = True
            elif act == self.butn.Stop and self.run == True:
                self.timer = time.time() - self.timer
                self.run = False
        if self.run == True:
            tim = int(time.time() - self.timer)
            hms = (tim // 3600, tim % 3600 // 60, tim % 60)
            self.lab.config(text = '{:02d}:{:02d}:{:02d}'.format(*hms))
            self.after(200,self.showtime)
root=tk.Tk()
colr = ["sky blue", "orange", "lightgreen", "yellow", "orchid1", "bisque2"]
[digitalclock(root, bd=8, bg=c).pack() for c in colr]
root.mainloop()

