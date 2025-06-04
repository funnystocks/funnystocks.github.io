from tkinter import *
import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
width = pyautogui.size().width
height = pyautogui.size().height
root = Tk()
root.geometry(str(width) + "x" + str(height))
root.title("Virtual Machine")
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
wh = (w, h)
one_twentieth = (int(w*0.05), int(h*0.05))
one_eightieth = (int(w*0.0125), int(h*0.0125))
desktop = Image.open("desktop/desktop.jpg")
red = Image.open("desktop/red.png")
green = Image.open("desktop/green.png")
blue = Image.open("desktop/blue.png")
img = [ImageTk.PhotoImage(desktop.resize(wh, Image.LANCZOS)), ImageTk.PhotoImage(red.resize(one_twentieth, Image.LANCZOS)), ImageTk.PhotoImage(green.resize(one_twentieth, Image.LANCZOS)), ImageTk.PhotoImage(blue.resize(one_twentieth, Image.LANCZOS))]
def click(color, red, green, blue, label):
    size = (w, h-int(h*0.05)-int(h*0.05))
    images = [ImageTk.PhotoImage(red.resize(size, Image.LANCZOS)), ImageTk.PhotoImage(green.resize(size, Image.LANCZOS)), ImageTk.PhotoImage(blue.resize(size, Image.LANCZOS))]
    if color == "red":
        label.config(image=images[0])
        label.image = images[0]
    elif color == "green":
        label.config(image=images[1])
        label.image = images[1]
    elif color == "blue":
        label.config(image=images[2])
        label.image = images[2]
    else:
        label.config(image="")
        label.image = ""
background = Label(root, image=img[0])
background.place(x=0, y=0)
label = Label(root, image="", borderwidth=0, relief="flat", highlightthickness=0)
label.place(x=0, y=one_twentieth[1])
convoluted = (w - (one_twentieth[0]*3 + one_eightieth[0]*2)) / 2
editor = Button(root, image=img[1], command=lambda: click("red", red, green, blue, label), borderwidth=0, relief="flat", highlightthickness=0)
editor.place(x=convoluted, y=h-img[1].height())
browser = Button(root, image=img[2], command=lambda: click("green", red, green, blue, label), borderwidth=0, relief="flat", highlightthickness=0)
browser.place(x=convoluted + one_eightieth[0] + one_twentieth[0], y=h-img[2].height())
explorer = Button(root, image=img[3], command=lambda: click("blue", red, green, blue, label), borderwidth=0, relief="flat", highlightthickness=0)
explorer.place(x=convoluted + (one_eightieth[0]*2) + (one_twentieth[0]*2), y=h-img[3].height())
x = Button(root, image=img[1], command=lambda: click("", red, green, blue, label), borderwidth=0, relief="flat", highlightthickness=0)
x.place(x=0, y=0)
root.mainloop()