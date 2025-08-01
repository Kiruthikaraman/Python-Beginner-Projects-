import tkinter as tk
import time
import datetime

def update_clock():
    now = time.strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%A, %d %B %Y")
    clock_label.config(text=now)
    date_label.config(text=date)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Arial", 48), bg="black", fg="lime")
clock_label.pack(pady=10, padx=20)

date_label = tk.Label(root, font=("Arial", 24), bg="black", fg="white")
date_label.pack(pady=5, padx=20)

root.configure(bg="black")
update_clock()
root.mainloop()