# **** PASSWORD GENERATOR ****

''' @author Shivam Srivastava '''

# Importing Libraries

from tkinter import *
import random
import string
import pyperclip

# Initialize window

root = Tk()
root.geometry("380x550+550+100")
root.resizable(0, 0)
root.configure(bg='#856ff8')
root.title("PASSWORD GENERATOR")
root.iconbitmap(r"password_generator-logo.ico")

# Heading
heading = Label(root, text=' PASSWORD GENERATOR ', borderwidth=2,
                relief=SOLID, bg="blue", fg='white', font='Times 20 bold').pack(pady=20)
Label(root, text='For more enquiry to DM me\n www.instagram.com/itsshivamsrivastava/',
      bg='#856ff8', fg='white', font='arial 12 bold').pack(side=BOTTOM)

# Select password length
pass_label1 = Label(root, text='PASSWORD LENGTH', bg='#856ff8',
                    fg='black', font='Helvetica 15 bold').pack(pady=20)
pass_len = IntVar() # Holds an integer; default value 0.
length = Spinbox(root, from_=8, to_=50, textvariable=pass_len,
                 width=22, borderwidth=2, relief=SOLID, font='Times 14').pack()

# Define function for generating password
pass_str = StringVar() # Holds a string; default value ""

def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

# Button Widgets
Button(root, text="GENERATE PASSWORD", borderwidth=3, relief=SOLID,
       bg="goldenrod1", font='Times 14 bold', command=Generator).pack(pady=30)

pass_label2 = Label(root, text=' GENERATED PASSWORD ', borderwidth=2, relief=SOLID,
                    bg='sky blue', fg='red', font='Helvetica 15 bold').pack(pady=25)
Entry(root, textvariable=pass_str, width=18, borderwidth=2,
      relief=SOLID, font=('Helvetica', 12)).pack()


# Function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='Copy To Clipboard', borderwidth=3, relief=SOLID,
       bg="goldenrod1", font='Times 14 bold', command=Copy_password).pack(pady=25)


# loop to run program
root.mainloop()
