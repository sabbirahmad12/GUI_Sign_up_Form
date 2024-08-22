from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ast

root = Tk()
root.title('Sign Up')
root.geometry('925x500+250+100')
root.config(bg = '#fff')


# Function area
def sign_up():
    full_name = name.get()
    user_name = username.get()
    pass_word = password.get()
    confirm_password = confirm_pass.get()

    if pass_word == confirm_password:

        try:
            file= open('sheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict = {'Name': full_name ,'username': user_name, 'password': pass_word}
            r.update(dict)
            file.truncate(0)
            file.close()

            file = open('sheet.txt','w')
            w = file.write(str(r))

            messagebox.showinfo('Sign up', 'Successfully Sign up')

        except:
            file= open('sheet.txt', 'w')
            pp = str({'Name': full_name ,'username': user_name, 'password': pass_word})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid', 'Both Password not match')


def enter(e):
    name.delete(0, 'end')

def leave(e):
    name_ = name.get()
    if name_ == '':
        name.insert(0, 'You Name')


def enter(e):
    username.delete(0, 'end')

def leave(e):
    user = username.get()
    if user == '':
        username.insert(0, 'username')


def enter(e):
    password.delete(0, 'end')

def leave(e):
    pass_ = password.get()
    if pass_ == '':
        password.insert(0, 'password')


def enter(e):
    confirm_pass.delete(0, 'end')

def leave(e):
    cf_pass = confirm_pass.get()
    if cf_pass == '':
        confirm_pass.insert(0, 'Confirm Password')


#Image Section 
img = ImageTk.PhotoImage(Image.open("signup.png"))

Label(root, image = img, bg = "white").place(x = 50, y = 50)

# Sign up Frame
frame = Frame(root, width= 350, height= 350, bg = 'white')
frame.place(x = 500, y = 50)

heading = Label(frame, text = 'Sign Up', fg = '#57a1f8', bg = 'white', font = ('comicsansms', 25, 'bold'))
heading.place(x = 120, y = 5)

# Name
name = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11) )
name.place( x= 55, y = 65)
name.insert(0, 'Your Name')
name.bind('<FocusIn>', enter)
name.bind('<FocusOut>', leave)

Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 90)

# Username
username = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11) )
username.place( x= 55, y = 115)
username.insert(0, 'username')
username.bind('<FocusIn>', enter)
username.bind('<FocusOut>', leave)

Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 140)

# Password
password = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11) )
password.place( x= 55, y = 165)
password.insert(0, 'password')
password.bind('<FocusIn>', enter)
password.bind('<FocusOut>', leave)

Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 190)

# Confirm Password
confirm_pass = Entry(frame, width = 30, fg = 'black', border = 0, bg= 'white', font = ('Microsoft YaHei UI Light', 11))
confirm_pass.place( x= 55, y = 215)
confirm_pass.insert(0, 'Confirm Password')
confirm_pass.bind('<FocusIn>', enter)
confirm_pass.bind('<FocusOut>', leave)

Frame(frame, width = 250, height= 2, bg = 'black').place(x = 50, y = 240)

# Button Section 
btn = Button(frame, text = 'Sign Up', cursor='hand2', width = 35, pady = 7, bg = '#57a1f8', fg = 'white', border = 0, command = sign_up)
btn.place(x= 50, y = 255)

# Bottom Section 
label = Label(frame, text = "I have an account?", fg = 'black', bg = 'white', font = ('Microsoft YaHei UI Light', 9))
label.place(x = 100, y = 300)

log_in_btn = Button(frame, text = 'Log in', cursor='hand2', width  = 6, border = 0, bg = 'white', fg = '#57a1f8')
log_in_btn.place(x = 210, y = 300)

root.mainloop()