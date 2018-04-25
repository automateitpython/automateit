import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

def gui():
    root = tk.Tk()
    root.geometry("450x450")
    root.wm_title("Automate It") 
    Label = tk.Label(root, text = 'Automate It', font = ('Comic Sans MS',18))
