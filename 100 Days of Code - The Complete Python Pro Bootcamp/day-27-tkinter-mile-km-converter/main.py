from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = float(input.get())
    number.config(text=f"{round(new_text *1.6,2)}")


window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=100)

#Label
my_label = Label(text="is equal to", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
my_label.grid(column=0, row=1)
my_label.config(padx=20, pady=20)

miles = Label(text="miles", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
miles.grid(column=2, row=0)

number = Label(text="0", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
number.grid(column=1, row=1)

km = Label(text="km", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)





window.mainloop()