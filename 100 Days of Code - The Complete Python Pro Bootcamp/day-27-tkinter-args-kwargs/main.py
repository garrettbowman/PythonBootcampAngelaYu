from tkinter import *
from playground import add

def button_clicked():
    # print("I got clicked")
    my_label.config(text=f"{input.get()}")


add(1,2,4,54,4,3,3)
window = Tk()
window.title("My first gui program.")
window.minsize(width=500, height=300)
window.config(padx=20,pady=30)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))


my_label["text"]= "new label"
my_label.config(text= "new label",padx=20,pady=20)
# my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)


button = Button(text="Click me", command=button_clicked)

# button.config(pack=left)
# button.pack()
button.grid(column=1,row=1)

button2 = Button(text="Click me", command=button_clicked)
button2.grid(column=2,row=0)

input = Entry(width=10)
input.get()
# input.pack()
input.grid(column=3,row=2)






window.mainloop()

