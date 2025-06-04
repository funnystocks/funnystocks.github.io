# explorer.py - A basic file explorer in tkinter
# Made by funnystocks (https://github.com/funnystocks) with assistance from Google Gemini in debugging, understanding Tkinter concepts, and implementing features
# No restrictions on usage - this is released into the public domain - 5/2025
import tkinter as tk
from tkinter import font
import pyautogui
from PIL import Image, ImageTk
import os
import sys
def open_file(file):
    os.system("open " + file)
def create_buttons(dir):
    for w in root.winfo_children():
        w.destroy()
    c = 0
    buttons = []
    listing = ["abcdefghijklmnopqrstuvwxyz0123456789"] + sorted(os.listdir(dir))
    for f in (listing):
        f = os.path.join(dir, f)
        if os.path.isfile(f):
            buttons.append(tk.Button(root, text=f + " size: " + str(os.path.getsize(f)), borderwidth=0, relief="flat", highlightthickness=0, command=lambda name=f: open_file(name)))
        elif os.path.isdir(f):
            buttons.append(tk.Button(root, text=f, borderwidth=0, relief="flat", highlightthickness=0, command=lambda name=f: create_buttons(name)))
        else:
            f = os.path.dirname(dir)
            buttons.append(tk.Button(root, text=f, borderwidth=0, relief="flat", highlightthickness=0, command=lambda name=f: create_buttons(name)))
        buttons[len(buttons)-1].place(x=0, y=24*c)
        c += 1
width = pyautogui.size().width
height = pyautogui.size().height
root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.title("File Explorer")
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
d = sys.argv[1]
create_buttons(d)
root.mainloop()