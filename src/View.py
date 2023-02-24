
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

class View:
    def __init__(self):
        # Creating window color is not white so we can see the images
        windoe = tk.Tk()
        windoe.geometry("1300x700")  
        windoe.title('3335_Project2_Images')
        windoe.configure(background = 'lightblue')

        # Simple title
        my_font1 = ('times', 18, 'bold')
        l1 = tk.Label(windoe, text = 'Eight Random Images', width = 30, font = my_font1)  
        l1.grid(row = 4, column = 20, columnspan = 10)
        # How do I center image? ^   does that matter?

        labels = []

        for i in range(8):
            label = tk.Label(image = ImageTk.PhotoImage(Image.new(mode = "L", size = (200, 200), color = (255))))
            labels.append(label)

        # reference
        # Create a photoimage object of the image in the path
        # img = Image.new(mode = "L", size = (200, 200), color = (255))
        # label1 = tk.Label(image = ImageTk.PhotoImage(img))


        labels[0].place(x = 100, y = 100) # First image, prints four across then 4 across on a second row.
        labels[1].place(x = 400, y = 100) # Second
        labels[2].place(x = 700, y = 100) # Third
        labels[3].place(x = 1000, y = 100) # Fourth
        labels[4].place(x = 100, y = 400) # Fifth
        labels[5].place(x = 400, y = 400) # Sixth
        labels[6].place(x = 700, y = 400) # Seventh
        labels[7].place(x = 1000, y = 400) # Eighth

        windoe.mainloop() 

