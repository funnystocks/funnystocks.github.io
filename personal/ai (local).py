# ai (local).py - A basic chat app in tk using the ollama library
# Made by funnystocks (https://github.com/funnystocks) with assistance from Google Gemini in debugging, understanding Tkinter concepts, and implementing features
# No restrictions on usage - this is released into the public domain - 5/2025
import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import ollama
import threading
width = pyautogui.size().width
height = pyautogui.size().height
root = tk.Tk()
root.title("AI Chat App (Local)")
root.geometry(str(width) + "x" + str(height))
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
l = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=w, height=h, borderwidth=0, relief="flat", highlightthickness=0)
l.place(x=0, y=0, width=w, height=(h*7/8))
l.config(state='disabled')
var = tk.StringVar(value="")
def press(event):
    if event.keysym == 'Return':
        clear(var.get())
root.bind("<Key>", press)
def respond(msg):
    root.after(0, update, "AI: " + ollama.chat(model='llama3', messages=[{'role': 'user', 'content': msg}])['message']['content'] + "\n\n")
def update(msg):
    l.config(state='normal')
    l.insert(tk.END, msg)
    l.config(state='disabled')
    l.see(tk.END)
def clear(msg):
    var.set("")
    update("Me: " + msg + "\n\n")
    t = threading.Thread(target=respond, args=(msg,))
    t.daemon = True
    t.start()
entry = tk.Entry(root, textvariable=var, borderwidth=0, relief="flat", highlightthickness=0)
entry.place(x=(w / 4), y=(h*7/8), width=(w*7/16), height=h / 8)
send = tk.Button(root, text="Send", borderwidth=0, relief="flat", highlightthickness=0, command=lambda: clear(var.get()))
send.place(x=(w*11/16), y=(h*7/8), width=w / 16, height=h / 8)
root.mainloop()