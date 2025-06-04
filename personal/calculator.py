# calculator.py - A basic calculator in tkinter, built more efficiently
# Made by funnystocks (https://github.com/funnystocks), this builds upon calculator (v1).py
# No restrictions on usage - this is released into the public domain - 6/2025
import tkinter as tk
import pyautogui
width = pyautogui.size().width
height = pyautogui.size().height
root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
root.title("Calculator - more efficiently built")
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
frame = tk.Frame(root, relief="flat", borderwidth=0, highlightthickness=0)
frame.place(x=0, y=h / 5, width=w, height=(h*4/5))
result = tk.StringVar(value="")
numbers = tk.Label(root, textvariable=result, relief="flat", borderwidth=0, highlightthickness=0)
numbers.place(x=0, y=0, width=w, height=h / 5)
def calculate(operator):
    if operator == "=":
        try:
            result.set(eval(result.get()))
        except:
            result.set("")
    else:
        result.set(result.get() + operator)
root.update_idletasks()
f_width = frame.winfo_width()
f_height = frame.winfo_height()
chars = [["1", "2", "3", "+"], ["4", "5", "6", "-"], ["7", "8", "9", "*"], [".", "0", "=", "/"]]
buttons = []
for arrays in range(len(chars)):
    for c in range(len(chars[arrays])):
        buttons.append(tk.Button(frame, text=chars[arrays][c], relief="flat", borderwidth=0, highlightthickness=0, command=lambda name=chars[arrays][c]: calculate(name)))
        buttons[len(buttons)-1].place(x=(c*f_width/4), y=(arrays*f_height/4), width=f_width/4, height=f_height/4)
root.mainloop()