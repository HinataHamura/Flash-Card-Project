from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#F999B7"
TEXT = "#980F5A"
CAN ="#52006A"
FONT = ("Constantia",30,"bold")
FONT1 = ("Constantia",50,"bold")
current_card = {}
to_learn={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    # print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global flip,current_card
    window.after_cancel(flip)
    current_card = choice(to_learn)
    canvas.itemconfig(title,text="French",fill=TEXT)
    canvas.itemconfig(word,text=current_card['French'],fill=TEXT)
    canvas.itemconfig(canvas_image,image=img)
    flip=window.after(3000, change)

def change():
    canvas.itemconfig(canvas_image,image=new_image)
    canvas.itemconfig(word,fill=CAN,text=current_card['English'])
    canvas.itemconfig(title,fill=CAN,text="English")
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)

flip = window.after(3000,change)
canvas = Canvas(highlightthickness=0,height=467,width=700,bg=BACKGROUND_COLOR)
img = PhotoImage(file="images/second.png")
new_image = PhotoImage(file="images/first.png")
canvas_image=canvas.create_image(350,234,image=img)
title=canvas.create_text(350,150,text="",fill=TEXT,font=FONT)
word=canvas.create_text(350,250,text="",fill=TEXT,font=FONT1)
canvas.grid(row=0,column=0,columnspan=2,pady=10)

my_image = PhotoImage(file="images/right.png")
known_button = Button(image=my_image,command=is_known)
known_button.grid(row=1,column=0)

my_image1 = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=my_image1,command=next_card)
unknown_button.grid(row=1,column=1)

next_card()








window.mainloop()

