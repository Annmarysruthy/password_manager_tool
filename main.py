from tkinter import *
from tkinter import messagebox
import random
import json
from tkinter import messagebox
# For searching password in json file


def find_password():
    try:
        file = open("data.json", "r")
        data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        website = website_entry.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the website {website} exists")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    for char in range(random.randint(8, 10)):
        password_list.append(random.choice(letters))

    for char in range(random.randint(2, 4)):
        password_list.append(random.choice(symbols))

    for char in range(random.randint(2, 4)):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save the details:\nEmail: {email}\nPassword:"
                                                              f" {password}")
        if is_ok:
            try:
                data_file = open("data.json", "r")

            except FileNotFoundError:
                data_file = open("data.json", "w")
                json.dump(new_data, data_file, indent=4)
            else:
                old_data = json.load(data_file)
                old_data.update(new_data)
                data_file.close()

                data_file = open("data.json", "w")
                json.dump(old_data, data_file, indent=4)
            data_file.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(window, height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=26)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "annmarysruthy2401@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

pwd_button = Button(text="Generate Password", command=generate_pwd)
pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
