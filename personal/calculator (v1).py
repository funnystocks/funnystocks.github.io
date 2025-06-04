# calculator (v1).py - A basic calculator in tkinter
# Made by funnystocks (https://github.com/funnystocks) with assistance from Google Gemini in debugging, understanding Tkinter concepts, and implementing features
# No restrictions on usage - this is released into the public domain - 5/2025
import tkinter as tk
import pyautogui
width = pyautogui.size().width
height = pyautogui.size().height
root = tk.Tk()
root.title("Calculator")
root.geometry(str(width) + "x" + str(height))
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
v = tk.StringVar(value="")
label = tk.Label(root, textvariable=v, borderwidth=0, relief="flat", highlightthickness=0)
def calculate(operator):
    if operator == "=":
        try:
            result = eval(v.get())
        except:
            result = ""
        v.set(str(result))
    else:
        v.set(v.get() + operator)
zero = tk.Button(root, text="0", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="0": calculate(name))
one = tk.Button(root, text="1", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="1": calculate(name))
two = tk.Button(root, text="2", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="2": calculate(name))
three = tk.Button(root, text="3", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="3": calculate(name))
four = tk.Button(root, text="4", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="4": calculate(name))
five = tk.Button(root, text="5", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="5": calculate(name))
six = tk.Button(root, text="6", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="6": calculate(name))
seven = tk.Button(root, text="7", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="7": calculate(name))
eight = tk.Button(root, text="8", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="8": calculate(name))
nine = tk.Button(root, text="9", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="9": calculate(name))
add = tk.Button(root, text="+", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="+": calculate(name))
subtract = tk.Button(root, text="-", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="-": calculate(name))
multiply = tk.Button(root, text="*", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="*": calculate(name))
divide = tk.Button(root, text="/", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="/": calculate(name))
decimal = tk.Button(root, text=".", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name=".": calculate(name))
equal = tk.Button(root, text="=", borderwidth=0, relief="flat", highlightthickness=0, command=lambda name="=": calculate(name))
label.place(x=0, y=0, width=w, height=h / 5)
one.place(x=0, y=h / 5, width=w / 4, height=h / 5)
two.place(x=w / 4, y=h / 5, width=w / 4, height=h / 5)
three.place(x=w / 2, y=h / 5, width=w / 4, height=h / 5)
four.place(x=0, y=(h*2) / 5, width=w / 4, height=h / 5)
five.place(x=w / 4, y=(h*2) / 5, width=w / 4, height=h / 5)
six.place(x=w / 2, y=(h*2) / 5, width=w / 4, height=h / 5)
seven.place(x=0, y=(h*3) / 5, width=w / 4, height=h / 5)
eight.place(x=w / 4, y=(h*3) / 5, width=w / 4, height=h / 5)
nine.place(x=w / 2, y=(h*3) / 5, width=w / 4, height=h / 5)
decimal.place(x=0, y=(h*4) / 5, width=w / 4, height=h / 5)
zero.place(x=w / 4, y=(h*4) / 5, width=w / 4, height=h / 5)
equal.place(x=w / 2, y=(h*4) / 5, width=w / 4, height=h / 5)
add.place(x=(w*3) / 4, y=h / 5, width=w / 4, height=h / 5)
subtract.place(x=(w*3) / 4, y=(h*2) / 5, width=w / 4, height=h / 5)
multiply.place(x=(w*3) / 4, y=(h*3) / 5, width=w / 4, height=h / 5)
divide.place(x=(w*3) / 4, y=(h*4) / 5, width=w / 4, height=h / 5)
root.mainloop()