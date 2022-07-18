from importlib.resources import contents
from multiprocessing import parent_process
from multiprocessing.sharedctypes import Value
from re import search
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from turtle import update
from turtle import title
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from functools import partial


class Employee :
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x5790")
        #main title
        self.root.title("Emploeey system management")
        #background
        self.bg_frame = Image.open('college_Images/background img.png')    
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes' )
        
        #====Variables======
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designition = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()


        # title 
        lbl_title=Label(self.root, text="Employee system management" , font=('times new roman ',25 ,'bold'),fg='#161185',bg='white')
        lbl_title.place(x=-990,y=0,width=2530,height=50)
        # Main Frame
        Main_frame=Frame(self.root)
        Main_frame.place(x=16,y=72,width=1500,height=699)
        
        # upper Frame
        upper_frame=Frame(Main_frame,bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=2270)
        

        # Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Department : ', font=('arial ',12 ,'bold'),fg='black',bg='white')
        lbl_dep.grid(row=0,column=0,padx=(10, 10),pady=(10,5),sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial ',12 ,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Depatment','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=1,column=0,padx=(10, 10),pady=(0,5),sticky=W)

        # Name
        lbl_Name=Label(upper_frame,font=('arial ',12 ,'bold'),text="Name:",bg='white')
        lbl_Name.grid(row=2,column=0,sticky=W,padx=(10, 10),pady=(10,5))

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22, font=('arial ',11 ,'bold'))
        txt_name.grid(row=3,column=0,padx=(10, 10),pady=(0,5))

        # lbl_Designition
        lbl_Designition=Label(upper_frame,font=('arial ',12 ,'bold'),text="Designition:",bg='white')
        lbl_Designition.grid(row=4,column=0,sticky=W,padx=(10, 10),pady=(0,5))

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22, font=('arial ',11 ,'bold'))
        txt_Designition.grid(row=5,column=0,sticky=W,padx=(10, 10),pady=(0,5))

        # Email
        lbl_email=Label(upper_frame,font=('arial ',12 ,'bold'),text="Email:",bg='white')
        lbl_email.grid(row=6,column=0,sticky=W,padx=10,pady=10)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22, font=('arial ',11 ,'bold'))
        txt_email.grid(row=7,column=0,padx=10,pady=10)

         # Dob
        lbl_dob=Label(upper_frame,font=('arial ',12 ,'bold'),text="DOB:",bg='white')
        lbl_dob.grid(row=0,column=1,sticky=W,padx=45,pady=10)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22, font=('arial ',11 ,'bold'))
        txt_dob.grid(row=1,column=1,padx=45,pady=2)

        # Doj
        lbl_doj=Label(upper_frame,font=('arial ',12 ,'bold'),text="DOJ : ",bg='white')
        lbl_doj.grid(row=2,column=1,sticky=W,padx=45,pady=10)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22, font=('arial ',11 ,'bold'))
        txt_doj.grid(row=3,column=1,padx=45,pady=2)

        # Id Proof
        lbl_proof=Label(upper_frame,font=('arial ',12 ,'bold'),text="ID Proof : ",bg='white')
        lbl_proof.grid(row=4,column=1,sticky=W,padx=45,pady=10)

        txt_proof=ttk.Entry(upper_frame,textvariable= self.var_idproof,font=('arial ',11 ,'bold'),width=22)
        txt_proof.grid(row=5,column=1,padx=45,pady=2)

        # country
        lbl_country=Label(upper_frame,font=('arial ',12 ,'bold'),text="Country:",bg='white')
        lbl_country.grid(row=6,column=1,sticky=W,padx=45,pady=10)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,font=('arial ',11 ,'bold'),width=22)
        txt_country.grid(row=7,column=1,padx=45,pady=2)
       
        # Address
        lbl_address=Label(upper_frame,font=('arial ',12 ,'bold'),text="Address : ",bg='white')
        lbl_address.grid(row=0,column=2,sticky=W,padx=17,pady=10)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22, font=('arial ',11 ,'bold'))
        txt_address.grid(row=1,column=2,padx=17,pady=10)

        # phone
        lbl_phone=Label(upper_frame,font=('arial ',12 ,'bold'),text="Phone No:",bg='white')
        lbl_phone.grid(row=2,column=2,sticky=W,padx=17,pady=10)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,font=('arial ',11 ,'bold'),width=22)
        txt_phone.grid(row=3,column=2,padx=17,pady=10)

        # CTC
        lbl_ctc=Label(upper_frame,font=('arial ',12 ,'bold'),text="Salary(CTC):",bg='white')
        lbl_ctc.grid(row=4,column=2,sticky=W,padx=17,pady=10)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_salary, font=('arial ',11 ,'bold'),width=22)
        txt_country.grid(row=5,column=2,padx=17,pady=10)
        
        # gender
        lbl_gender=Label(upper_frame,font=('arial ',12 ,'bold'),text="gender:",bg='white')
        lbl_gender.grid(row=6,column=2,sticky=W,padx=17,pady=10)
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=('arial ',11 ,'bold'),width=20)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=7,column=2,sticky=W,padx=17,pady=10)

     

        # img Frame
        img_frame= Image.open('college_Images/797866e79ccfaf11704e84cce10ef466.jpg')
        img_frame=img_frame.resize((500,335),Image.Resampling.LANCZOS)
        # img_frame.place(x=1200,y=50,width=250,height=370)
        self.photo=ImageTk.PhotoImage(img_frame)    
        self.img_frame=Label(upper_frame,image=self.photo)
        self.img_frame.place(x=966,y=20)
        
        # Button Frame
        button_frame=Frame(upper_frame,bg='white')
        button_frame.place(x=736,y=0,width=200,height=500)

        btn_add=Button(button_frame,text="Save",font=('arial ',14,'bold'),width=14,bg='#161185',command=self.add_data,fg='white', activebackground='#161185', cursor='hand2')
        btn_add.grid(row=1,column=0,padx=0,pady=47)
        # 
        btn_update=Button(button_frame,text="Update",font=('arial ',14,'bold'),width=14,command=self.update_data,bg='#4143E6',fg='white', activebackground='#4143E6', cursor='hand2')
        btn_update.grid(row=2,column=0,padx=0,pady=2) 
        # 
        btn_delete=Button(button_frame,text="Delete",font=('arial ',14,'bold'),width=14,bg='#E54B3F',command=self.delete_data,fg='white', activebackground='#E54B3F', cursor='hand2')
        btn_delete.grid(row=3,column=0,padx=0,pady=49)
        # 

        btn_clear=Button(button_frame,text="Clear",font=('arial ',14,'bold'),width=14,bg='#92B3FA',command=self.reset_data,fg='white', activebackground='#92B3FA', cursor='hand2')      
        btn_clear.grid(row=4,column=0,padx=0,pady=2)
        # 
        # down Frame
        down_frame=Frame(Main_frame,bg='white')
        down_frame.place(x=10,y=390,width=1470,height=1200)
        
        # search Frame
        search_frame=Frame(down_frame,bg='white')
        search_frame.place(x=8,y=0,width=1460,height=80)
        search_txt=Label(search_frame,font=('arial ',12 ,'bold'),text="Search  :",bg='white')
        search_txt.grid(row=0,column=0,sticky=W,padx=0,pady=0)
      
        #Search 
        self.var_com_search= StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=('arial',12,'bold'), width=18)
        com_txt_search['value']=('Select Option ','Phone','id_proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=1,column=0,sticky=W,padx=1)
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=1,column=1,padx=(52,10))

        btn_search=Button(search_frame,text="Search",font=('arial ',12,'bold'),width=15,command=self.search_data,bg='#161185',fg='white', activebackground='#161185', cursor='hand2')
        btn_search.grid(row=1,column=2,padx=20)
        # 
        btn_ShowAll=Button(search_frame,text="ShowAll",font=('arial ',12,'bold'),width=15,command=self.fetch_data,bg='#161185',fg='white', activebackground='#161185', cursor='hand2')
        btn_ShowAll.grid(row=1,column=5,padx=645)
        # 
        
        # == Employee Table ==
        # Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=7,y=65,width=1470,height=200)
        
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","dob","doj","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Degignition')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
       
        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)


        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #functions 
        
    def add_data(self) : 
        if self.var_dep.get() == ' ' or self.var_email.get() == '' :
            messagebox.showerror('Error', 'All fields are required ')
            
        else : 
            try:     
                conn=mysql.connector.connect(host='localhost',username='root',password='09384117841Ftm2001',database='project data')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_designition.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_doj.get(),
                                                                                                        self.var_idproof.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_country.get(),
                                                                                                        self.var_salary.get()  ) )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Add ',parent=self.root)
            except Exception as es : 
                messagebox.showerror('Error',f'Due to : {str(es)}' ,parent=self.root )
        
    
    #fetch  Data 
    def fetch_data(self) : 
        conn=mysql.connector.connect(host='localhost',username='root',password='09384117841Ftm2001',database='project data')
        my_cursor =conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data) != 0 :
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data :
                self.employee_table.insert('',END,values=i)
            conn.commit()
        conn.close()
        
        
    # Get Cursur
    def get_cursor(self,event="") :
            cursor_row=self.employee_table.focus()
            content=self.employee_table.item(cursor_row)
            data=content['values']     
            
            self.var_dep.set(data[0])
            self.var_name.set(data[1])
            self.var_designition.set(data[2])
            self.var_email.set(data[3])
            self.var_address.set(data[4])
            self.var_dob.set(data[5])
            self.var_doj.set(data[6])
            self.var_idproof.set(data[7])
            self.var_gender.set(data[8])
            self.var_phone.set(data[9])
            self.var_country.set(data[10])
            self.var_salary.set(data[11])


    def update_data(self):
        if self.var_dep.get() == ' ' or self.var_email.get() == '' :
            messagebox.showerror('Error', 'All fields are required ')
        else: 
            try:
                update=messagebox.askyesno('Update','Are sure update this employee data')
                if update>0:  
                    conn=mysql.connector.connect(host='localhost',username='root',password='09384117841Ftm2001',database='project data')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee set Department=%s,Name=%s,Designition=%s,id_proof=%s,Address=%s,DOB=%s,DOJ=%s,Gender=%s,Phone=%s,country=%s,salary=%s where id_proof=%s',(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_designition.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_doj.get(),
                                                                                                                                                                                    self.var_idproof.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_country.get(),
                                                                                                                                                                                    self.var_salary.get()    ))  
                else:           
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Successfully update',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_idproof.get()=="":   
            messagebox.showerror('Error',"All fields are required")  
        else:                
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root) 
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='09384117841Ftm2001',database='project data')
                    my_cursor=conn.cursor()  
                    sql='delete from employee where id_proof=%s'   
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)  
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Successfully Deleted',parent=self.root)
            except Exception as es:
                 messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  

    # reset                                                                                                                                           
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    # search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()== '':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='09384117841Ftm2001',database='project data')
                my_cursor=conn.cursor()  
                my_cursor.execute('select * from employee where '+ str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit  
                conn.close()          
            except Exception as es:
                 messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)



        
if __name__ == "__main__" : 
    root=Tk()
    obj= Employee(root)
    root.mainloop()

 
