import tkinter as Tk
from tkinter import *
import random

root = Tk()
root.title("Roll Dice")
root.geometry("500x450")

label = Label(root,font = ("Arabic",250,"bold"), text = "")  # \u
label.pack()

def rolldice():
    dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    label.configure(text = f'{random.choice(dice)}')
    label.pack()

button = Button(root,font = ("Arabic",25,"bold"), text = "Roll Dice", command = rolldice, bg = "pink")
button.pack()

root.mainloop()
