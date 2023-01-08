from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_new_password():
    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)
    generated_password = "".join(password_list)

    pyperclip.copy(generated_password)

    password_text.delete(0, END)
    password_text.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    if website_text.get() == "" or email_text.get() == "" or password_text.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        make_sure = messagebox.askokcancel(title="Make sure", message=f"Here is the data you entered:\n"
                                                                      f"Website: {website_text.get()}\n"
                                                                      f"Email: {email_text.get()}\n"
                                                                      f"Password: {password_text.get()}\n"
                                                                      f"Are you sure you want to proceed and save it?")

        if make_sure:
            with open("data.text", mode="a") as data:
                data.write(f"{website_text.get()}  |  {email_text.get()}  |  {password_text.get()}\n")

            website_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
website.config(pady=5)

website_text = Entry(width=50)
website_text.focus()
website_text.grid(column=1, row=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)
email.config(pady=5, padx=20)

email_text = Entry(width=50)
email_text.insert(0, "omarmobarak53@gmail.com")
email_text.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
password.config(pady=5)

password_text = Entry(width=32)
password_text.grid(column=1, row=3)

generate_password = Button(text="Generate password", highlightthickness=0, command=generate_new_password)
generate_password.grid(column=2, row=3)

add = Button(width=43, text="Add", highlightthickness=0, command=add_info)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
