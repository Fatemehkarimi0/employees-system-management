from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk

class Employee :
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+070")
        #main title
        self.root.title("Emploeey system management")
        
        # title 
        lbl_title=Label(self.root, text="EMPLOOYEE MANAGEMANT SYSTEM" , font=('times new roman ',37 ,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        #we should add Image folder
        img_logo = Image.open('college_Images/name of image')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)    
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)
        
        #box of image
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
        
        #fix path of image
        #first image header
        img1 = Image.open('college_Images/name of image')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)    
        
        self.image_1=Label(img_frame,image=self.photo1)
        self.image_1.place(x=0,y=0,width=540,height=160)
         
        #2nd image header
        img2 = Image.open('college_Images/name of image')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)    
        
        self.image_2=Label(img_frame,image=self.photo2)
        self.image_2.place(x=540,y=0,width=540,height=160)
        
        #third image header
        img3 = Image.open('college_Images/name of image')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)   
         
        self.image_3=Label(self.root,image=self.photo3)
        self.image_3.place(x=1000,y=0,width=540,height=160)
        
        
        
        
        
        
        
        
        
if __name__ == "__main__" : 
    root=TK()
    obj= Employee(root)
    root.mainloop()