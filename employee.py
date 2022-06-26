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
        img_logo_mask = Image.open('college_Images/name of image')
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
        
          
        # Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)
        
        
        # upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information', font=('times new roman ',11 ,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)
        

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department', font=('arial ',11 ,'bold'),fg='white')
        lbl_dep.gride(row=0,column=0,padx=2,sticky=W)


        combo_dep=ttk.Combobox(upper_frame,font=('arial ',12 ,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Depatment','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.gride(row=0,column=1,padx=2,pady=10,sticky=W)


        # Name
        lbl_Name=Label(upper_frame,font=('arial ',12 ,'bold'),text="Name:",bg='white')
        lbl_Name.gride(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)


        # lbl_Designition
        lbl_Designition=Label(upper_frame,font=('arial ',12 ,'bold'),text="Designition:",bg='white')
        lbl_Designition.gride(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)


        # Email
        lbl_email=Label(upper_frame,font=('arial ',12 ,'bold'),text="Email:",bg='white')
        lbl_email.gride(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)


        # Address
        lbl_address=Label(upper_frame,font=('arial ',12 ,'bold'),text="Address:",bg='white')
        lbl_address.gride(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)


        # Married
        lbl_married_status=Label(upper_frame,font=('arial ',12 ,'bold'),text="Married Status:",bg='white')
        lbl_married_status.gride(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married=ttk.Combobox(upper_frame,state="readonly",font=('arial ',11 ,'bold'),width=17)

        com_txt_married['value']=("Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,colun=3,sticky=W,padx=2,pady=7)

      
        # Dob
        lbl_dob=Label(upper_frame,font=('arial ',12 ,'bold'),text="DOB:",bg='white')
        lbl_dob.gride(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)


       # Doj
        lbl_doj=Label(upper_frame,font=('arial ',12 ,'bold'),text="DOJ:",bg='white')
        lbl_doj.gride(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)


    
        # Id Proof
        com_txt_proof=ttk.Combobox(upper_frame,state="readonly",font=('arial ',11 ,'bold'),width=22)

        com_txt_proof['value']=("Select ID Proof","PAN CARD","DRIVING LICENSE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(upper_frame,width=22, font=('arial ',11 ,'bold'))
        txt_proof.gride(row=4,column=1,padx=2,pady=7)


        # gender
        lbl_gender=Label(upper_frame,font=('arial ',12 ,'bold'),text="gender:",bg='white')
        lbl_gender.gride(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(upper_frame,state="readonly",font=('arial ',11 ,'bold'),width=22)

        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)


        # phone
        lbl_phone=Label(upper_frame,font=('arial ',12 ,'bold'),text="Phone No:",bg='white')
        lbl_phone.gride(row=4,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,font=('arial ',11 ,'bold'),width=22)
        txt_phone.grid(row=0,column=5,padx=2,pady=7)


        # country
        lbl_country=Label(upper_frame,font=('arial ',12 ,'bold'),text="Country:",bg='white')
        lbl_country.gride(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,font=('arial ',11 ,'bold'),width=22)
        txt_country.grid(row=1,column=5,padx=2,pady=7)


        # CTC
        lbl_ctc=Label(upper_frame,font=('arial ',12 ,'bold'),text="Salary(CTC):",bg='white')
        lbl_ctc.gride(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(upper_frame,font=('arial ',11 ,'bold'),width=22)
        txt_country.grid(row=2,column=5,padx=2,pady=7)

        # mask image
        img_mask = Image.open('college_Images/name of image')
        img_mask= img_mask.resize((220,220),Image.ANTIALIAS)
        self.photomask=ImageTk.PhotoImage(img_mask)    
        
        self.image_mask=Label(upper_frame,image=self.photomask)
        self.image_mask.place(x=1000,y=0,width=220,height=220)

        # Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=12,y=10,width=170,height=210)
        

        btn_add=Button(button_frame,text="Save",font=('arial ',15,'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text="Update",font=('arial ',15,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5) 
        
        btn_delete=Button(button_frame,text="Delete",font=('arial ',15,'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",font=('arial ',15,'bold'),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        
        
        # down Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table', font=('times new roman ',11 ,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        #search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='search Employee Information', font=('times new roman ',11 ,'bold'),fg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)
        
        search_by=Label(search_by,text='Search by : ',font=('arial ',11,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        
        #Search 
        self.var_com_search= StringVar()
        com_txt_search=ttk.Combobox(search_frame,state="readonly",font=('arial',12,'bold'), width=18)
        com_txt_search['Value']=('Select Option ','Phone','idProof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        
        txt_search=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="search",font=('arial ',11,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)
        
        btn_ShowAll=Button(search_frame,text="ShowAll",font=('arial ',11,'bold'),width=14,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)
        
        Stayhome=LabelFrame(search_frame,bg='white',text='Stay Home', font=('times new roman ',11 ,'bold'),fg='red')
        Stayhome.place(x=780,y=0,width=600,height=30)
        
        img_logo_mask = Image.open(r'college_Images/name of image')
        img_logo_mask=img_logo_mask.resize((50,50),Image.ANTIALIAS)
        self.photo_logo_mask=ImageTk.PhotoImage(img_logo_mask)    
        self.logo=Label(self.root,image=self.photo_logo_mask)
        self.logo.place(x=900,y=0,width=50,height=30)
        
        
        # == Employee Table ==
        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)
        
        
        
        
        
        
        
        
if __name__ == "__main__" : 
    root=TK()
    obj= Employee(root)
    root.mainloop()
