import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("dicee")
dice = ["C:/Users/punya/OneDrive/Desktop/one.png","C:/Users/punya/OneDrive/Desktop/two.png"
    ,"C:/Users/punya/OneDrive/Desktop/three.png","C:/Users/punya/OneDrive/Desktop/four.png","C:/Users/punya/OneDrive/Desktop/five.png","C:/Users/punya/OneDrive/Desktop/six.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x=100,y=75)
label2.place(x=700,y=75)


def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2
button = tk.Button(window,text="ROLLLL", fg="green",font = "Times 10 bold",command=dice_roll)
button.place(x = 630,y = 200)
window.mainloop()
#
# def rolldice():
#     a = random.randint(1,6)
#     label = tk.Label(window,text=a).pack()
#
# button = tk.Button(window,text="roll",command=rolldice)
# button.pack()