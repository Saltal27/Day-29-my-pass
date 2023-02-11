from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    if website_text.get() == "":
        messagebox.showerror(title="Oops", message="Please enter a website name!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                searched_website = data[website_text.get().capitalize()]

        except KeyError:
            messagebox.showerror(title="Invalid Info!",
                                 message= "The website name you entered doesn't have any stored"
                                          " info in our database"
                                         "\nYou may want to check if you spelled it correctly,"
                                         " or you You might want to add new info and save it first")

        except FileNotFoundError:
            messagebox.showerror(title="Oops!",
                                 message="No data file found")

        else:
            messagebox.showinfo(title=website_text.get(),
                                message=f"Email: {searched_website['Email']}"
                                        f"\nPassword: {searched_website['Password']}")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R',
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


# ---------------------------- CLEAR DATABASE ------------------------------- #
def clear_database():
    clear_answer = messagebox.askyesno(title="Delete the database",
                        message="Are you sure you want to delete all your previously stored info?"
                                "\nNote: This action can't be undone once you clicked the 'Yes' button")
    if clear_answer:
        with open("data.json", "w") as data_file:
            json.dump({}, data_file)
        messagebox.showinfo(title="Successfully deleted!",
                            message="Your stored info has been successfully deleted")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    info_dict = {
        website_text.get().capitalize():{
            "Email": email_text.get(),
            "Password": password_text.get()
        }
    }
    if website_text.get() == "" or email_text.get() == "" or password_text.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        make_sure = messagebox.askokcancel(title="Make sure",
                                           message=f"Here is the data you entered:\n"
                                                   f"Website: {website_text.get()}\n"
                                                   f"Email: {email_text.get()}\n"
                                                   f"Password: {password_text.get()}\n"
                                                   f"Are you sure you want to proceed and save it?"
                                                   f"\n\nNote: If the website name you entered is already saved in our"
                                                   f"database, we will replace the old info with the new one")

        if make_sure:

            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(info_dict)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(info_dict, data_file, indent=4)

            except json.decoder.JSONDecodeError:
                with open("data.json", mode="w") as data_file:
                    json.dump(info_dict, data_file, indent=4)

            else:
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="#E3E5E6")

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, background="#E3E5E6")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Lables
website = Label(text="Website:", background="#E3E5E6")
website.grid(column=0, row=1)
website.config(pady=5)

email = Label(text="Email/Username:", background="#E3E5E6")
email.grid(column=0, row=2)
email.config(pady=5, padx=20)

password = Label(text="Password:", background="#E3E5E6")
password.grid(column=0, row=3)
password.config(pady=5)

nothing = Label(background="#E3E5E6")
nothing.grid(column=0, row=4)
nothing.config(pady=8)

#Entrys
website_text = Entry(width=32)
website_text.focus()
website_text.grid(column=1, row=1)

email_text = Entry(width=50)
email_text.insert(0, "example@gmail.com")
email_text.grid(column=1, row=2, columnspan=2)

password_text = Entry(width=32)
password_text.grid(column=1, row=3)

#Buttons
search = Button(text="          Search          ", highlightthickness=0, command=search_data)
search.grid(column=2, row=1)

generate_password = Button(text="Generate password", highlightthickness=0, command=generate_new_password)
generate_password.grid(column=2, row=3)

add = Button(width=27, text="Add", highlightthickness=0, command=add_info)
add.grid(column=1, row=4)

clear = Button(text="    Clear database    ", highlightthickness=0, command=clear_database)
clear.grid(column=2, row=4)

window.mainloop()
