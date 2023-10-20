from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk    #pip install pillow
import random , os
from tkinter import messagebox
import tempfile





class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Parth Management System")


   #**********************************Variables************************************************

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,15000)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total= StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()







       #Product Catagories:
        self.Category=["Select Option","Laptop","Mobile","Tv","Clothes","LifeStyle"]


        self.subCatLaptop=["HP","Dell","Asus","Lenovo","samsung","apple","realme"]


        self.hp=["Pavillion","Victus","Omen","Hp15","Hp16","ENVY"]
        self.price_Pavillion=72000
        self.price_Victus=82000
        self.price_Omen=94000
        self.price_Hp15=65000
        self.price_ENVY=100000
        

        self.Dell=["inspiron","Vestro","Inspiron15","Gaming"]
        self.price_inspiron=72000
        self.price_Vestro=60000
        self.price_Inspiron15=56000
        self.price_Gaming=80000


        self.Asus=["TUF15","TAF15","ROG1","ROG5","VivoBook"]
        self.price_TUF15=67999
        self.price_TAF15=52500
        self.price_ROG1=74000
        self.price_ROG5=125000
        self.price_VivoBook=45000


        self.Lenovo=["ideaPad","ThinkPad","Legion","Yoga"]
        self.price_ideaPad=43000
        self.price_ThinkPad=59523
        self.price_Legion=92000
        self.price_Yoga=145555


        self.samsung=["book1","SamsungBook2","BookGen3"]
        self.price_book1=78520
        self.price_SamsungBook2=63000
        self.price_BookGen3=95000
        

        self.apple=["MacBookAirm1","MacBookAirm2","MacBookAirm2Pro"]
        self.price_MacBookAirm1=122000
        self.price_MacBookAirm2=135000
        self.price_MacBookAirm2Pro=214000


        self.realme=["Realmebook1","Realmebook2"]
        self.price_Realmebook1=78000
        self.price_Realmebook2=62000


        self.CatMobile=["Samsung","XaioMi","Realme","Apple","Vivo","OnePlus"]

        self.Samsung=["A31","A51","A41","A54","S8","S21Ultra","S22Ultra","M31","M54","F42"]
        self.price_A31=20000
        self.price_A51=17500
        self.price_A41=16000
        self.price_A54=34000
        self.price_S8=50000
        self.price_S21Ultra=99999
        self.price_S22Ultra=125000
        self.price_M31=18500
        self.price_M54=24000
        self.price_F42=14000


        self.XaioMi=["Note8","Note9","Note9Pro","Note9ProMax","Note10","Note11","Note12"]
        self.price_Note8=10000
        self.price_Note9=13500
        self.price_Note9Pro=14000
        self.price_Note9ProMax=15000
        self.price_Note10=16500
        self.price_Note11=18010
        self.price_Note12=25000


        self.Realme=["NarzoN55","C35","C11","Realme10Pro","Realme10Pro5g","Narzo50i"]
        self.price_NarzoN55=10000
        self.price_C35=13500
        self.price_C11=8000
        self.price_Realme10Pro=19000
        self.price_Realme10Pro5g=21000
        self.price_Narzo50i=15000
        

        self.Apple=["iphoneX","iphoneXi","iphone11","iphone12","iphone13","iphone14","iphone14pro","iphone14proMax"]
        self.price_iphoneX=50000
        self.price_iphoneXi=56000
        self.price_iphone11=65000
        self.price_iphone12=80000
        self.price_iphone13=90000
        self.price_iphone14=100000
        self.price_iphone14pro=120000
        self.price_iphone14proMax=140000


        self.Vivo=["VivoV7","vivoV9","VivoV11","VivoV12","Vivov27","VivoV29"]
        self.price_VivoV7=10000
        self.price_VivoV9=15000
        self.price_VivoV11=18000
        self.price_VivoV12=24000
        self.price_VivoV27=27000
        self.price_VivoV29=35000


        self.OnePlus=["OnePlusNord","NordCe5g","OnePlus7","OnePlus8t"]
        self.price_OnePlusNord=27000
        self.price_NordCe5g=25000
        self.price_OnePlus7=35000
        self.price_OnePlus8t=41500
        
      
        self.CatTv=["Mi","Samsung1","LG","Sony"]

        self.Mi=["Mi5A","Mi43inch","Mi55Inch"]
        self.price_Mi5A=16000
        self.price_Mi43inch=25600
        self.price_Mi55Inch=45000


        self.Samsung1=["GalaxyTv","Oled43","Oled55","Samsung8K"]
        self.price_GalaxyTv=20000
        self.price_Oled43=32000
        self.price_Oled55=55000
        self.price_Samsung8K=275000


        self.LG=["LgOled43","LgOLed55","LgOled8K"]
        self.price_LgOled43=42000
        self.price_LgOLed55=85000
        self.price_LgOled8K=225000
        

        self.Sony=["Sony43","Sony55","Sony75","Sony8k"]
        self.price_Sony43=48000
        self.price_Sony55=95000
        self.price_Sony75=245000
        self.price_Sony8K=335000


        self.CatClothes=["Pant","T-Shirt","Shirt","Kurta","Suits"]

        self.Pant=["Denim","DenimJence","Foorky","Cotten","Formall"]
        self.price_Denim=2500
        self.price_DenimJence=1700
        self.price_Foorky=2850
        self.price_Cotten=3600
        self.price_Formall=5000


        self.TShirt=["Levis","Raymand","Adidas","PUMA","Nike"]
        self.price_Levis=2000
        self.price_Raymand=1000
        self.price_Adidas=3000
        self.price_PUMA=1800
        self.price_Nike=2500


        self.Shirt=["Raymand","PeterEngland","SiyaRams","LoyalShirts"]
        self.price_Raymand=5000
        self.price_PeterEngland=7650
        self.price_SiyaRams=3650
        self.price_LoyalShirts=6000
      

        self.Kurta=["Pathani","ModiKurta","PlaneKurta","Shervani"]
        self.price_Pathani=12000
        self.price_ModiKurta=15000
        self.price_PlaneKurta=7500
        self.price_Shervani=13000
         

        self.Suits=["Raymand1","PeterEngland1","SiyaRams1","LoyalSuit1"]
        self.price_Raymand1=35000
        self.price_PeterEngland1=50000
        self.price_SiyaRams1=45000
        self.price_LoyalShirts1=70000
        

        self.CatLifeStyle=["Shampoo","Soup","Shoes","Bages"]

        self.Shampoo=["Dove","HairCare","Patnjali","ClinicPlus","SunShine"]
        self.price_Dove=750
        self.price_HairCare=500
        self.price_Patnjali=450
        self.price_ClinicPlus=700
        self.price_SunShine=350


        self.Soup=["Dove1","LifeBoy","Dettol","Santoor"]
        self.price_Dove1=350
        self.price_LifeBoy=500
        self.price_Dettol=450
        self.price_Santoor=700


        self.Shoes=["WoodLand","AdiDas","Puma","Campus","Bata"]
        self.price_WoodLand=12500
        self.price_AdiDas=15000
        self.price_Puma=7000
        self.price_Campus=4500
        self.price_Bata=10000


        self.Bages=["levis","AmericanTurister","SkyBages","Orange"]
        self.price_levis=2650
        self.price_AmericanTurister=5000
        self.price_SkyBages=4500
        self.price_Orange=1250


        lb1_title=Label(self.root,text="Billing Management System",font=("times new roman",30,"bold"),bg="red",fg="white")
        lb1_title.place(x=0,y=0,width=1430,height=45)


        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=50,width=1530,height=620)

            #Lable of Custmores


        Cust_Frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",12,"bold"),bg="light green",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

            #mobile

        self.lb1_mob=Label(Cust_Frame,text="Mobile No",font=("times new roman",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)


        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times now roman",12,"bold"),width=22)
        self.entry_mob.grid(row=0,column=1)

             #cust Name

        self.lb1_cuat_Name=Label(Cust_Frame,text="Customer Name",font=("times new roman",12,"bold"),bg="white")
        self.lb1_cuat_Name.grid(row=1,column=0,stick=W,padx=5,pady=2)


        self.entry_name=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times now roman",12,"bold"),width=22)
        self.entry_name.grid(row=1,column=1)

              #email

        self.lb1_Email=Label(Cust_Frame,text="Email_Id",font=("times new roman",12,"bold"),bg="white")
        self.lb1_Email.grid(row=2,column=0,stick=W,padx=5,pady=2)


        self.entry_Email=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times now roman",12,"bold"),width=22)
        self.entry_Email.grid(row=2,column=1)

              #Product label Frame

        Product_Frame=LabelFrame(Main_frame,text="Product",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        Product_Frame.place(x=370,y=5,width=600,height=140)


               #Category

        self.lb1_Category=Label(Product_Frame,text="Select_Category",font=("times new roman",12,"bold"),bg="white")
        self.lb1_Category.grid(row=0,column=0,stick=W,padx=5,pady=2)


        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"))
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


            #Sub category

        self.lb1_SubCategory=Label(Product_Frame,text="Select_SubCategory",font=("times new roman",12,"bold"),bg="white")
        self.lb1_SubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)


        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"))
        self.ComboSubCategory.grid(row=1,column=1,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

            #Product name

        self.lb1_Product=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white")
        self.lb1_Product.grid(row=2,column=0,stick=W,padx=5,pady=2)


        self.Combo_Product=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"))
        self.Combo_Product.grid(row=2,column=1,padx=5,pady=2)


        self.Combo_Product.bind("<<ComboboxSelected>>",self.price)

           #price

        self.lb1_Price=Label(Product_Frame,text="Price",font=("times new roman",12,"bold"),bg="white")
        self.lb1_Price.grid(row=0,column=2,stick=W,padx=5,pady=2)


        self.Combo_price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"))
        self.Combo_price.grid(row=0,column=3,padx=5,pady=2)

          #Qty

        self.lb1_Qty=Label(Product_Frame,text="Quantity",font=("times new roman",12,"bold"),bg="white")
        self.lb1_Qty.grid(row=1,column=2,stick=W,padx=5,pady=2)


        self.Combo_Qty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",11,"bold"))
        self.Combo_Qty.grid(row=1,column=3,padx=5,pady=2)

          #middle frame

        middleFrame=Frame(Main_frame,bd=10,bg="light blue")
        middleFrame.place(x=10,y=150,width=980,height=340)


        # img=Image.open("image/a4.png")
        # img=img.resize((100,250),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

 
        # lb1_img=Label(self.root,image=self.photoimg)
        # lb1_img.place(x=0,y=250,width=550,height=500)


        #search area

        Search_Frame=Frame(Main_frame,bd=2,bg="white")
        Search_Frame.place(x=980,y=20,width=450,height=40)


        self.lb1_bill=Label( Search_Frame,text="Bill Number",font=("times new roman",12,"bold"),bg="red",fg="white")
        self.lb1_bill.grid(row=0,column=0,stick=W,padx=1)


        self.bill_Qty=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",11,"bold"),width=24)
        self.bill_Qty.grid(row=0,column=1,padx=5)


        self.BtnSearch=Button(Search_Frame,text="Search",font=("arial",10,"bold"),bg="red",fg="white",width=8,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #Right bill area

        RightLabelFrame=LabelFrame(Main_frame,text="Bill System",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=980,y=75,width=380,height=410)

        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times now roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #bill counter labelframe

        Bill_Frame=LabelFrame(Main_frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="blue",fg="red")
        Bill_Frame.place(x=0,y=495,width=1520,height=120)
         
        #Sub total

        self.lb1_Subtotal=Label( Bill_Frame,text="Sub_Total",font=("times new roman",12,"bold"),bg="white")
        self.lb1_Subtotal.grid(row=0,column=0,stick=W,padx=5,pady=2)


        self.lb1_Subtotal=ttk.Entry( Bill_Frame,textvariable=self.sub_total,font=("arial",12,"bold"))
        self.lb1_Subtotal.grid(row=0,column=1,padx=5,pady=2)
     
        #tax

        self.lb1_tax=Label( Bill_Frame,text="Gov_Tax",font=("times new roman",12,"bold"),bg="white")
        self.lb1_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)


        self.lb1_tax=ttk.Entry( Bill_Frame,textvariable=self.tax_input,font=("arial",12,"bold"))
        self.lb1_tax.grid(row=1,column=1,padx=5,pady=2)

        #Total Amount

        self.lb1_TotalAmount=Label( Bill_Frame,text="Total",font=("times new roman",12,"bold"),bg="white")
        self.lb1_TotalAmount.grid(row=2,column=0,stick=W,padx=5,pady=2)


        self.lb1_TotalAmount=ttk.Entry( Bill_Frame,textvariable=self.total,font=("arial",12,"bold"))
        self.lb1_TotalAmount.grid(row=2,column=1,padx=5,pady=2)

        #buttons Frame

        Button_Frame=Frame(Bill_Frame,bd=2,bg="white")
        Button_Frame.place(x=320,y=0)


        self.BtnAddtoCart=Button(Button_Frame,command=self.Additem,height=2,text="Add To Cart",font=("arial",15,"bold"),bg="red",fg="white",width=12,cursor="hand2")
        self.BtnAddtoCart.grid(row=0,column=0)

        
        self.BtnGenerateBill=Button(Button_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="red",fg="white",width=12,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=1)


        self.BtnSave=Button(Button_Frame,command=self.Save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="red",fg="white",width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)


        self.BtnPrint=Button(Button_Frame,command=self.iprint,height=2,text="Print",font=("arial",15,"bold"),bg="red",fg="white",width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)


        self.BtnClear=Button(Button_Frame,height=2,text="Clear",font=("arial",15,"bold"),bg="red",fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)


        self.BtnExit=Button(Button_Frame,height=2,text="Exit",font=("arial",15,"bold"),bg="red",fg="white",width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)


        self.welcome()


        self.list1=[]


     ###################Function Instance######################################


    def Additem(self):
           Tax=1
           self.n=self.prices.get()
           self.m=self.qty.get()*self.n
           self.list1.append(self.m)
      
           
           self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
           self.sub_total.set(str('Rs.%.2f'%(sum(self.list1))))
           self.tax_input.set(str('Rs.%.2f'%((((sum(self.list1)) - (self.prices.get()))*Tax)/100)))
           self.total.set(str('Rs.%.2f'%(((sum(self.list1))+ ((((sum(self.list1)) - (self.prices.get()))*Tax)/100)))))
                  
    def gen_bill(self):
           if self.product.get()=="":
                  messagebox.showerror("ERROR","Please Enter The Valid Product In To The Cart")
           else:
                  text=self.textarea.get(10.0,(10.0+float(len(self.list1))))
                  self.welcome()
                  self.textarea.insert(END,"\n***********************************************************")
                  
                 
                  self.textarea.insert(END,f"\n Product Name:\t\t\t{self.product.get()}")
                  self.textarea.insert(END,f"\n Product Qty:\t\t\t{self.qty.get()}")
                  self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
                  self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
                  self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")

                  self.textarea.insert(END,"\n***********************************************************")



    def Save_bill(self):
           op=messagebox.askyesno("Save Bill","Doyou Want To Save This Bill")
           if op>0:
                  self.bill_data=self.textarea.get(1.0,END)
                  f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
                  f1.write(self.bill_data)
                  op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()}  Saved Sucessfully")
                  f1.close()

            
    def iprint(self):
           q=self.textarea.get(1.0,"end-1c")
           filename=tempfile.mktemp('.txt')
           open(filename,'w').write(q)
           os.startfile(filename,'print')
           
    def find_bill(self):
           found="no"
           for i in os.listdir("bills/"):
                  if i.split(".")[0]==self.search_bill.get():
                         f1=open("bills/(i)","r")
                         self.textarea.delete(1.0,END)
                         for d in f1:
                                self.textarea.insert(END,d)
                                f1.close()
                                found="yes"
                         
     
             
    

  
  
    def welcome(self):
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"        CyberCity Laptops,Gurugram,New Delhi")

            self.textarea.insert(END,"\n***********************************************************")

            self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
            self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
            self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
            self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

            self.textarea.insert(END,"\n***********************************************************")
            
            self.textarea.insert(END,f"\n Products\t\tQty\t\tPrice")

            self.textarea.insert(END,f"\n***********************************************************")








    def Categories(self,event=""):
        if self.Combo_Category.get()=="Laptop":
            self.ComboSubCategory.config(value=self.subCatLaptop)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobile":
            self.ComboSubCategory.config(value=self.CatMobile)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Tv":
            self.ComboSubCategory.config(value=self.CatTv)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Clothes":
            self.ComboSubCategory.config(value=self.CatClothes)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.CatLifeStyle)
            self.ComboSubCategory.current(0)
 
          #Laptops
    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="HP":
            self.Combo_Product.config(value=self.hp)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Dell":
            self.Combo_Product.config(value=self.Dell)
            self.Combo_Product.current(0)
             
        if self.ComboSubCategory.get()=="Asus":
            self.Combo_Product.config(value=self.Asus)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Lenovo":
            self.Combo_Product.config(value=self.Lenovo)
            self.Combo_Product.current(0) 

        if self.ComboSubCategory.get()=="samsung":
            self.Combo_Product.config(value=self.samsung)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="apple":
            self.Combo_Product.config(value=self.apple)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Realme":
            self.Combo_Product.config(value=self.realme)
            self.Combo_Product.current(0)   

        #mobile
        if self.ComboSubCategory.get()=="Samsung":
            self.Combo_Product.config(value=self.Samsung)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="XaioMi":
            self.Combo_Product.config(value=self.XaioMi)
            self.Combo_Product.current(0)
             
        if self.ComboSubCategory.get()=="Realme":
            self.Combo_Product.config(value=self.Realme)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Apple":
            self.Combo_Product.config(value=self.Apple)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Vivo":
            self.Combo_Product.config(value=self.Vivo)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="OnePlus":
            self.Combo_Product.config(value=self.OnePlus)
            self.Combo_Product.current(0)


        #Tv Instance
        if self.ComboSubCategory.get()=="Mi":
            self.Combo_Product.config(value=self.Mi)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Samsung1":
            self.Combo_Product.config(value=self.Samsung1)
            self.Combo_Product.current(0)
             
        if self.ComboSubCategory.get()=="LG":
            self.Combo_Product.config(value=self.LG)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Sony":
            self.Combo_Product.config(value=self.Sony)
            self.Combo_Product.current(0)


        #Clothes Instance
        if self.ComboSubCategory.get()=="Pant":
            self.Combo_Product.config(value=self.Pant)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.Combo_Product.config(value=self.TShirt)
            self.Combo_Product.current(0)
             
        if self.ComboSubCategory.get()=="Shirt":
            self.Combo_Product.config(value=self.Shirt)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Kurta":
            self.Combo_Product.config(value=self.Kurta)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Suits":
            self.Combo_Product.config(value=self.Suits)
            self.Combo_Product.current(0)

        #Life Style Instance
        if self.ComboSubCategory.get()=="Shampoo":
            self.Combo_Product.config(value=self.Shampoo)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Soup":
            self.Combo_Product.config(value=self.Soup)
            self.Combo_Product.current(0)
             
        if self.ComboSubCategory.get()=="Shoes":
            self.Combo_Product.config(value=self.Shoes)
            self.Combo_Product.current(0)

        if self.ComboSubCategory.get()=="Bags":
            self.Combo_Product.config(value=self.Bages)
            self.Combo_Product.current(0)



    # Price
    def price(self,event=""):
            #Laptop Instance


            #HP inatance
        if self.Combo_Product.get()=="Pavillion":
                self.Combo_price.config(value=self.price_Pavillion)
                self.Combo_price.current(0)
                self.qty.set(1)

        if self.Combo_Product.get()=="Victus":
                self.Combo_price.config(value=self.price_Victus)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Omen":
                self.Combo_price.config(value=self.price_Omen)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Hp15":
                self.Combo_price.config(value=self.price_Hp15)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="ENVY":
                self.Combo_price.config(value=self.price_ENVY)
                self.Combo_price.current(0)
                self.qty.set(1)


            #Dell Instance

        if self.Combo_Product.get()=="inspiron":
                self.Combo_price.config(value=self.price_inspiron)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Vestro":
                self.Combo_price.config(value=self.price_Vestro)
                self.Combo_price.current(0)
                self.qty.set(1)

        
        if self.Combo_Product.get()=="Inspiron15":
                self.Combo_price.config(value=self.price_Inspiron15)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Gaming":
                self.Combo_price.config(value=self.price_Gaming)
                self.Combo_price.current(0)
                self.qty.set(1)

        

             #Asus Instance

        if self.Combo_Product.get()=="TUF15":
                self.Combo_price.config(value=self.price_TUF15)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="TAF15":
                self.Combo_price.config(value=self.price_TAF15)
                self.Combo_price.current(0)
                self.qty.set(1)

            
        if self.Combo_Product.get()=="ROG1":
                self.Combo_price.config(value=self.price_ROG1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="ROG5":
                self.Combo_price.config(value=self.price_ROG5)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="VivoBook":
                self.Combo_price.config(value=self.price_VivoBook)
                self.Combo_price.current(0)
                self.qty.set(1)

            #Lenovo Instance

        if self.Combo_Product.get()=="ideaPad":
                self.Combo_price.config(value=self.price_ideaPad)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="ThinkPad":
                self.Combo_price.config(value=self.price_ThinkPad)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Legion":
                self.Combo_price.config(value=self.price_Legion)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Yoga":
                self.Combo_price.config(value=self.price_Yoga)
                self.Combo_price.current(0)
                self.qty.set(1)


             #Samsung Instance
    
        if self.Combo_Product.get()=="book1":
                self.Combo_price.config(value=self.price_book1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="SamsungBook2":
                self.Combo_price.config(value=self.price_SamsungBook2)
                self.Combo_price.current(0)
                self.qty.set(1)
                

        if self.Combo_Product.get()=="BookGen3":
                self.Combo_price.config(value=self.price_BookGen3)
                self.Combo_price.current(0)
                self.qty.set(1)


               #Apple Instance

        if self.Combo_Product.get()=="MacBookAirm1":
                self.Combo_price.config(value=self.price_MacBookAirm1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="MacBookAirm2":
                self.Combo_price.config(value=self.price_MacBookAirm2)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="MacBookAirm2Pro":
                self.Combo_price.config(value=self.price_MacBookAirm2Pro)
                self.Combo_price.current(0)
                self.qty.set(1)

               #Realme Instance

        if self.Combo_Product.get()=="Realmebook1":
                self.Combo_price.config(value=self.price_Realmebook1)
                self.Combo_price.current(0)
                self.qty.set(1)

        
        if self.Combo_Product.get()=="Realmebook2":
                self.Combo_price.config(value=self.price_Realmebook2)
                self.Combo_price.current(0)
                self.qty.set(1)


            #Mobile Instance

            #Samsung Instance
            
        if self.Combo_Product.get()=="A31":
                self.Combo_price.config(value=self.price_A31)
                self.Combo_price.current(0)
                self.qty.set(1)

            
        if self.Combo_Product.get()=="A51":
                self.Combo_price.config(value=self.price_A51)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="A41":
                self.Combo_price.config(value=self.price_A41)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="A54":
                self.Combo_price.config(value=self.price_A54)
                self.Combo_price.current(0)
                self.qty.set(1)

            
        if self.Combo_Product.get()=="S8":
                self.Combo_price.config(value=self.price_S8)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="S21Ultra":
                self.Combo_price.config(value=self.price_S21Ultra)
                self.Combo_price.current(0)
                self.qty.set(1)

        
        if self.Combo_Product.get()=="S22Ultra":
                self.Combo_price.config(value=self.price_S22Ultra)
                self.Combo_price.current(0)
                self.qty.set(1)

            
        if self.Combo_Product.get()=="M31":
                self.Combo_price.config(value=self.price_M31)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="M54":
                self.Combo_price.config(value=self.price_M54)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="F42":
                self.Combo_price.config(value=self.price_F42)
                self.Combo_price.current(0)
                self.qty.set(1)

           #Mi Instance
            
        if self.Combo_Product.get()=="Note8":
                self.Combo_price.config(value=self.price_Note8)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Note9":
                self.Combo_price.config(value=self.price_Note9)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Note9Pro":
                self.Combo_price.config(value=self.price_Note9Pro)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Note9ProMax":
                self.Combo_price.config(value=self.price_Note9ProMax)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Note10":
                self.Combo_price.config(value=self.price_Note10)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Note11":
                self.Combo_price.config(value=self.price_Note11)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Note12":
                self.Combo_price.config(value=self.price_Note12)
                self.Combo_price.current(0)
                self.qty.set(1)

        
              #Realme Instance

        if self.Combo_Product.get()=="Narz0N55":
                self.Combo_price.config(value=self.price_NarzoN55)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="C35":
                self.Combo_price.config(value=self.price_C35)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="C11":
                self.Combo_price.config(value=self.price_C11)
                self.Combo_price.current(0)
                self.qty.set(1)

        
        if self.Combo_Product.get()=="Realme10Pro":
                self.Combo_price.config(value=self.price_Realme10Pro)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Realme10Pro5g":
                self.Combo_price.config(value=self.price_Realme10Pro5g)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Narzo50i":
                self.Combo_price.config(value=self.price_Narzo50i)
                self.Combo_price.current(0)
                self.qty.set(1)

              #Apple Instance

        if self.Combo_Product.get()=="iphoneX":
                self.Combo_price.config(value=self.price_iphoneX)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphoneXi":
                self.Combo_price.config(value=self.price_iphoneXi)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphone11":
                self.Combo_price.config(value=self.price_iphone11)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphone12":
                self.Combo_price.config(value=self.price_iphone12)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphone13":
                self.Combo_price.config(value=self.price_iphone13)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphone14":
                self.Combo_price.config(value=self.price_iphone14)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphone14pro":
                self.Combo_price.config(value=self.price_iphone14pro)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="iphone14proMax":
                self.Combo_price.config(value=self.price_iphone14proMax)
                self.Combo_price.current(0)
                self.qty.set(1)
  
                       #Vivo Instance

        if self.Combo_Product.get()=="VivoV7":
                self.Combo_price.config(value=self.price_VivoV7)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="vivoV9":
                self.Combo_price.config(value=self.price_VivoV9)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="VivoV11":
                self.Combo_price.config(value=self.price_VivoV11)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="VivoV12":
                self.Combo_price.config(value=self.price_VivoV12)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Vivov27":
                self.Combo_price.config(value=self.price_VivoV27)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="VivoV29":
                self.Combo_price.config(value=self.price_VivoV29)
                self.Combo_price.current(0)
                self.qty.set(1)

             #Oneplus Instance

        if self.Combo_Product.get()=="OnePlusNord":
                self.Combo_price.config(value=self.price_OnePlusNord)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="NordCe5g":
                self.Combo_price.config(value=self.price_NordCe5g)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="OnePlus7":
                self.Combo_price.config(value=self.price_OnePlus7)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="OnePlus8t":
                self.Combo_price.config(value=self.price_OnePlus8t)
                self.Combo_price.current(0)
                self.qty.set(1)

           #TV Instance     

           #Mi Instance

        if self.Combo_Product.get()=="Mi5A":
                self.Combo_price.config(value=self.price_Mi5A)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Mi43inch":
                self.Combo_price.config(value=self.price_Mi43inch)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Mi55Inch":
                self.Combo_price.config(value=self.price_Mi55Inch)
                self.Combo_price.current(0)
                self.qty.set(1)


              #Samsung TV instance

        if self.Combo_Product.get()=="GalaxyTv":
                self.Combo_price.config(value=self.price_GalaxyTv)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Oled43":
                self.Combo_price.config(value=self.price_Oled43)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Oled55":
                self.Combo_price.config(value=self.price_Oled55)
                self.Combo_price.current(0)
                self.qty.set(1)
       
         #LG Instance

        if self.Combo_Product.get()=="LgOled43":
                self.Combo_price.config(value=self.price_LgOled43)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="LgOled55":
                self.Combo_price.config(value=self.price_LgOLed55)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="LgOled8K":
                self.Combo_price.config(value=self.price_LgOled8K)
                self.Combo_price.current(0)
                self.qty.set(1)


                #Sony Instance

        if self.Combo_Product.get()=="Sony43":
                self.Combo_price.config(value=self.price_Sony43)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Sony55":
                self.Combo_price.config(value=self.price_Sony55)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Sony75":
                self.Combo_price.config(value=self.price_Sony75)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Sony8K":
                self.Combo_price.config(value=self.price_Sony8K)
                self.Combo_price.current(0)
                self.qty.set(1)


            #clothes Instance

            #Pant Instance

        if self.Combo_Product.get()=="Denim":
                self.Combo_price.config(value=self.price_Denim)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="DenimJence":
                self.Combo_price.config(value=self.price_DenimJence)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Foorky":
                self.Combo_price.config(value=self.price_Foorky)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Cotten":
                self.Combo_price.config(value=self.price_Cotten)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Formall":
                self.Combo_price.config(value=self.price_Formall)
                self.Combo_price.current(0)
                self.qty.set(1)


          #T-Shirts Instance

        if self.Combo_Product.get()=="Levis":
                self.Combo_price.config(value=self.price_Levis)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Raymand":
                self.Combo_price.config(value=self.price_Raymand)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Adidas":
                self.Combo_price.config(value=self.price_Adidas)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="PUMA":
                self.Combo_price.config(value=self.price_PUMA)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Nike":
                self.Combo_price.config(value=self.price_Nike)
                self.Combo_price.current(0)
                self.qty.set(1)
           

         #Shirts Instance

        if self.Combo_Product.get()=="Raymand":
                self.Combo_price.config(value=self.price_Raymand)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="PeterEngland":
                self.Combo_price.config(value=self.price_PeterEngland)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="SiyaRams":
                self.Combo_price.config(value=self.price_SiyaRams)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="LoyalShirts":
                self.Combo_price.config(value=self.price_LoyalShirts)
                self.Combo_price.current(0)
                self.qty.set(1)

            #Kurta Instance


        if self.Combo_Product.get()=="Pathani":
                self.Combo_price.config(value=self.price_Pathani)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="ModiKurta":
                self.Combo_price.config(value=self.price_ModiKurta)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="PlaneKurta":
                self.Combo_price.config(value=self.price_PlaneKurta)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Shervani":
                self.Combo_price.config(value=self.price_Shervani)
                self.Combo_price.current(0)
                self.qty.set(1)

                #Suits Instance

        if self.Combo_Product.get()=="Raymand1":
                self.Combo_price.config(value=self.price_Raymand1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="PeterEngland1":
                self.Combo_price.config(value=self.price_PeterEngland1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="SiyaRams1":
                self.Combo_price.config(value=self.price_SiyaRams1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="LoyalSuit1":
                self.Combo_price.config(value=self.price_LoyalShirts1)
                self.Combo_price.current(0)
                self.qty.set(1)

          #LifeStyle Instance

          #Shampoo Instance

        if self.Combo_Product.get()=="Dove":
                self.Combo_price.config(value=self.price_Dove)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="HairCare":
                self.Combo_price.config(value=self.price_HairCare)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Patnjali":
                self.Combo_price.config(value=self.price_Patnjali)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="ClinicPlus":
                self.Combo_price.config(value=self.price_ClinicPlus)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="SunShine":
                self.Combo_price.config(value=self.price_SunShine)
                self.Combo_price.current(0)
                self.qty.set(1)

                #Soupm Instance

        if self.Combo_Product.get()=="Dove1":
                self.Combo_price.config(value=self.price_Dove1)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="LifeBoy":
                self.Combo_price.config(value=self.price_LifeBoy)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Dettol":
                self.Combo_price.config(value=self.price_Dettol)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Santoor":
                self.Combo_price.config(value=self.price_Santoor)
                self.Combo_price.current(0)
                self.qty.set(1)

              #Shoes Instance

        if self.Combo_Product.get()=="WoodLand":
                self.Combo_price.config(value=self.price_WoodLand)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="AdiDas":
                self.Combo_price.config(value=self.price_AdiDas)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Puma":
                self.Combo_price.config(value=self.price_Puma)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Campus":
                self.Combo_price.config(value=self.price_Campus)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Bata":
                self.Combo_price.config(value=self.price_Bata)
                self.Combo_price.current(0)
                self.qty.set(1)
 
           #Bages Instance

        if self.Combo_Product.get()=="levis":
                self.Combo_price.config(value=self.price_levis)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="AmericanTurister":
                self.Combo_price.config(value=self.price_AmericanTurister)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="SkyBages":
                self.Combo_price.config(value=self.price_SkyBages)
                self.Combo_price.current(0)
                self.qty.set(1)


        if self.Combo_Product.get()=="Orange":
                self.Combo_price.config(value=self.price_Orange)
                self.Combo_price.current(0)
                self.qty.set(1) 


































   












if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()