from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password_result = "".join(password_list)  # concatenate all elements of password list as a string.
    password_entry.delete(0, "end")  # from index, to index
    password_entry.insert(0, password_result)  # index, value
    pyperclip.copy(password_result)  # copy on clipboard.


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()  # get the entry data.
    email = email_entry.get()
    password = password_entry.get()

    # pop-up a message box if some entry is blank.
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error!", message="Please don't leave any filled empty!")

    else:
        is_save = messagebox.askyesno(title=website, message=f"Email: {email}\nPassword: {password}\n\nSave this "
                                                             f"website email and password?")
        # If clicked yes, messagebox returns True.
        if is_save:
            # a: stands for append, write and append value to the end.
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            # clear or delete existing value of the entry box, from start to end
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

        # if no, messagebox returns False.
        else:
            messagebox.showinfo(title="Generate new data", message="Kindly, update the details you want to change.")


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager by Carl")
window.config(padx=50, pady=50)

# Canvas -- image (c1, r0)
img = PhotoImage(file="logo.png")  # PhotoImage for creating a canvas **kw image.
cv = Canvas(width=200, height=200)
cv.create_image(100, 100, image=img)  # PhotoImage var.
cv.grid(column=1, row=0)

# Website Entry box c1, r1
website_entry = Entry(width=52)  # resize the entry box.
website_entry.grid(column=1, row=1, columnspan=2)  # column span: overlap the column to the given value.
website_entry.focus()  # place the cursor on the entry box. ready to type.

# Email entry c1, r2
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "cangelo.damee@gmail.com")  # add a pre-typed value.

# Password entry c1, r3
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Website Label c0, r1
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email/Username c0, r2
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Password c0, r3
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Add button
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Generate password button
generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(column=2, row=3)

window.mainloop()
