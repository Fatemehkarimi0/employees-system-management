
from tkinter import *
from PIL import ImageTk
from PIL import Image
import os

class LoginForm:
    
    def callback(self) :
        os.system(' python employee.py')
  
    def __init__(self, window) :
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # =================== Background Image ===================
        self.bg_frame = Image.open('college_Images/background img.png')    
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes' )

        # =================== Login Frame ===================
        self.lgn_frame = Frame(self.window, bg='white', width='980',
                               height=650, highlightbackground="#264F83", highlightthickness=14,borderwidth=0, )
        self.lgn_frame.pack(padx=30, pady=30)
        self.lgn_frame.place(x=278, y=95)
        
        # =================== Left Side Image ===================
        self.side_image = Image.open('college_Images/Left img.jpg')
            
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='white')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=160)

        # =================== Sign In Image ===================
        self.sign_in_lable = Label(
            self.lgn_frame, text='Login', bg='white', fg='black', font=('yu gothic ui', 28, 'bold'))
        self.sign_in_lable.place(x=560, y=145)
        self.sign_in_lable = Label(self.lgn_frame, text='Welcome to the Employee management system',
                                   bg='white', fg='gray', font=('yu gothic ui', 11))
        self.sign_in_lable.place(x=560, y=198)

        # =================== Email ===================
        self.username_label = Label(
            self.lgn_frame, text='Email', bg='white', font=('yu gothic ui', 13, 'bold'))
        self.username_label.place(x=560, y=245)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT,
                                    bg='white', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.username_entry.place(x=565, y=276, width=270)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=565, y=305)
      
        # =================== Password ===================
        self.password_label = Label(
            self.lgn_frame, text='Password', bg='white', font=('yu gothic ui', 13, 'bold'),)
        self.password_label.place(x=560, y=340)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT,
                                    bg='white', fg='#6b6a69', font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry.place(x=565, y=371, width=244)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)

        self.password_line.place(x=565, y=400)

        # =================== forgot password ===================
        self.forgot_button = Button(self.lgn_frame, text='Forgot Password ?', font=(
            'yu gothic ui', 11, 'bold'), fg='#CC3931', width=15, bd=0, bg='white',activebackground='white',cursor='hand2')
        self.forgot_button.place(x=557, y=410)

         # =================== Login button ===================
        self.login_button = Button(self.lgn_frame, text='LOGIN', font=(
            'yu gothic ui', 15, 'bold '), command=self.callback, fg='white', width=25, bd=0, bg='#264F83', activebackground='#264F83', cursor='hand2',borderwidth=0)
        self.login_button.place(x=562, y=465, width=305, height=40)
        

        
        # =================== Sign Up ===================
        self.sign_label = Label(self.lgn_frame, text='No account yet ?', font=(
            'yu gothic ui', 11, 'bold'), background="white", fg='gray')
        self.sign_label.place(x=599, y=515)

        self.signup_button = Button(self.lgn_frame, text='SIGN UP NOW ', font=(
            'yu gothic ui', 12, 'bold'), fg='#264F83', width=25, bd=0,bg='white', activebackground='white', cursor='hand2')

        self.signup_button.place(x=718, y=510, width=111, height=35)

        # =================== Show/Hide Password ===================

        self.show_image = Image.open('college_Images/show and hide password img/show.png')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(
        self.lgn_frame, image=self.photo1, bg='white', activebackground='white', cursor='hand2', bd=0, command=self.show)

        self.show_button.image = self.photo1
        self.show_button.place(x=830, y=372)

        self.hide_image = Image.open(
                'college_Images/show and hide password img/hide.png')
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
            self.hide_button = Button(
            self.lgn_frame, image=self.photo, bg='white', activebackground='white', cursor='hand2', bd=0, command=self.hide)
            self.hide_button.image = self.photo
            self.hide_button.place(x=830, y=372)
            self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(
        self.lgn_frame, image=self.photo1, bg='white', activebackground='white', cursor='hand2', bd=0, command=self.show)

        self.show_button.image =self.photo1
        self.show_button.place(x=830, y=372)
        self.password_entry.config(show='*')



def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


if __name__ == '__main__':
    page()
