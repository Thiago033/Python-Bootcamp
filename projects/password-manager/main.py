from    tkinter  import  *
from    tkinter  import  messagebox
from    random   import  choice, randint, shuffle
import  pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    
    password = "".join(password_list)
    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open("projects/password-manager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Lock img setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="projects\password-manager\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# ---------------- Inputs ------------------- #
# Website
website_label = Label(text="Website:")
website_label.grid(column=0 , row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0 , row=2)
email_input = Entry(width=35)
email_input.insert(0, "thiagolopes_@_mail.com")
email_input.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0 , row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add data button
add_data = Button(text="Add", width=36, command=save)
add_data.grid(column=1, row=4, columnspan=2)

window.mainloop( )
