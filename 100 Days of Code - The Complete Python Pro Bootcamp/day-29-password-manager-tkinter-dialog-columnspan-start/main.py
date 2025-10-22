from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list +=([random.choice(letters)for item in range(0,nr_letters)])

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += ([random.choice(symbols)for item1 in range(0,nr_symbols)])
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += ([random.choice(numbers)for item2 in range(0,nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    print(f"Your password is: {password}")
    pyperclip.copy(password)
    input3.delete(0, END)
    input3.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(input1.get()) == 0 or len(input2.get()) == 0 or len(input3.get()) == 0:
        messagebox.showinfo(title="empty", message="u left empty")
        return

    # messagebox.showinfo(title="title",message="message")
    is_ok = messagebox.askokcancel(title=input1.get(),message=f"{input2.get()} | {input3.get()}, ok?")

    if is_ok:
        with open("saved_passwords.txt",mode="a") as file:
            file.write(f"{input1.get()} | {input2.get()} | {input3.get()}\n")
            input1.delete(0,"end")
            input3.delete(0,"end")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)# bg=YELLOW)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

# website
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)


# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

input1 = Entry(width=35)
print(input1.get())
input1.grid(column=1, row=1, columnspan=2)
input1.focus()

input2 = Entry(width=35)
print(input2.get())
input2.grid(column=1, row=2, columnspan=2 )
input2.insert(0,"barney@aol.net")


input3 = Entry(width=21)
print(input3.get())
input3.grid(column=1, row=3)


generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()