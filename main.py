import pyperclip
from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_generator = PasswordGenerator()


def generate_password():
    new_password = password_generator.generate()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data_entry = f"{website} | {email} | {password}\n"

    if len(website.strip()) == 0:
        messagebox.showwarning("website", "you left the website field blank")
    elif len(email.strip()) == 0:
        messagebox.showwarning("email", "you left the email field blank")
    elif len(password.strip()) == 0:
        messagebox.showwarning("password", "you left the password field blank")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {email}\n"
                                                                f"Password: {password} \n Is it ok to save?")
    with open("data.txt", mode="a") as data_file:
        data_file.write(data_entry)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "user@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
