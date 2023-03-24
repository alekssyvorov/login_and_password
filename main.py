from tkinter import *
from tkinter import messagebox
import pickle
from tkinter import font


HEIGHT = 550
WIDTH = 550


def registration():
    label_error = None

    frame = Frame(root)
    frame.place(relx=0.2, rely=0.2, relwidth=0.7, relheight=0.7)

    label = Label(frame, text='Sing UP', font='18')
    label.place(relwidth=1, relheight=0.1)

    label_register = Label(frame, text='Login: ')
    label_register.place(relx=0.01, rely=0.2)
    login_entry = Entry(frame)
    login_entry.place(relx=0.3, rely=0.2, relwidth=0.6)

    label_pass1 = Label(frame, text='Password: ')
    label_pass1.place(relx=0.01, rely=0.35)
    login_pass1 = Entry(frame, show='*')
    login_pass1.place(relx=0.3, rely=0.35, relwidth=0.6)

    label_pass2 = Label(frame, text='Confirm\npassword: ')
    label_pass2.place(relx=0.01, rely=0.5)
    login_pass2 = Entry(frame, show='#')
    login_pass2.place(relx=0.3, rely=0.55, relwidth=0.6)

    button = Button(frame, text='Sing Up', command=lambda: singup())
    button.place(relx=0.4, rely=0.8, relwidth=0.3)

    def singup():
        nonlocal label_error
        error = ''

        if label_error:
            label_error.destroy()

        # Error label
        if len(login_entry.get()) == 0:
            error = '*login error'
        elif len(login_pass1.get()) < 6:
            error = '*your password needs to be at least 6 character'
        elif not login_pass1.get() == login_pass2.get():
            error = '*password error'
        else:
            save()
        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.7)

    def save():
        data = dict()
        data[login_entry.get()] = login_pass1.get()
        f = open('login.txt', 'wb')
        pickle.dump(data, f)
        f.close()
        login_form()

    def login_form():
        frame = Frame(root, bd=10)
        frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')

        # Sign in text label
        label = Label(frame, text='Sign In', font='16')
        label.place(relwidth=1, relheight=0.1)

        # Login
        label_login = Label(frame, text='Login: ')
        label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

        enter_login = Entry(frame)
        enter_login.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)

        # Password
        label_password = Label(frame, text='Password: ')
        label_password.place(rely=0.4, relwidth=0.35, relheight=0.1)

        enter_password = Entry(frame, show='*')
        enter_password.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)

        button = Button(frame, text='Sign in', command=lambda: login_pass())
        button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)

        def login_pass():
            f = open('login.txt', 'rb')
            a = pickle.load(f)
            f.close()
            if enter_login.get() in a and enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo('Welcome', 'Welcome to the Game.')
            else:
                messagebox.showerror('Error!', 'Invalid login or password')


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='image/bg3.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_singup = Button(root, text='Sing Up', bg='gold', command=registration)
button_singup.place(relx=0.2, rely=0.1, relwidth=0.3)
button_singin = Button(root, text='Sing In', bg='gold')
button_singin.place(relx=0.5, rely=0.1, relwidth=0.3)

# print(font.families())
# print(len(font.families()))

root.mainloop()
