from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tokenize import String
from turtle import width
from typing_extensions import Self
from cv2 import setIdentity
from matplotlib.pyplot import text
import mysql.connector
from pyparsing import col
from requests import delete

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        self.Nameoftablets=StringVar()
        self.ReferenceNo=StringVar()
        self.Dose=StringVar()
        self.Nooftablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpiryDate=StringVar()
        self.DailyDose=StringVar()
        # self.SideEffects=StringVar()
        # self.FurtherInformation=StringVar()
        self.Storage=StringVar()
        # self.DrivingUsingMachine=StringVar()
        #self.HowToUseMedication=StringVar()
        #self.PatientID=StringVar()
        self.NHSNo=StringVar()
        self.PatientName=StringVar()
        self.DOB=StringVar()
        self.Address=StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="RED",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ==============================================================DataFrame====================================================================================
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,font=("arial",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=500,height=350)

        #==============================================================Buttons Frame=================================================================================
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        #===============================================================Details Frame================================================================================
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190)

        #===============================================================DataFrame Left===============================================================================
        lblNameTablet=Label(DataFrameLeft,text="Names of Tablet", font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablets ,font=("arial",12,"bold"),width=33)
        comNametablet["values"]=("Levocetirizine","Dolo 650","Azithromycin","Disprin","Crocin" )
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft,text="Reference Number", font=("arial",12,"bold"),padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,textvariable=self.ReferenceNo,font=("arial",13,"bold"),width =35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft,text="Dose", font=("arial",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,textvariable=self.Dose,font=("arial",13,"bold"),width =35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets = Label(DataFrameLeft,text="No. of Tablets", font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataFrameLeft,textvariable=self.Nooftablets,font=("arial",13,"bold"),width =35)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot = Label(DataFrameLeft,text="Lot", font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,textvariable=self.Lot,font=("arial",13,"bold"),width =35)
        txtLot.grid(row=4,column=1)

        lblissueDate = Label(DataFrameLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataFrameLeft,textvariable=self.IssueDate,font=("arial", 12, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, text="Expiry Date:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft,textvariable=self.ExpiryDate,font=("arial", 12, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2,pady=4)
        lblDailyDose.grid(row=0, column=2, sticky=W)
        txtDailyDose = Entry(DataFrameLeft,textvariable=self.DailyDose ,font=("arial", 12, "bold"), width=35)
        txtDailyDose.grid(row=0, column=3)

        # lblsideEffect = Label(DataFrameLeft, text="Side Effect:", font=("arial", 12, "bold"), padx=2,pady=6)
        # lblsideEffect.grid(row=8, column=0, sticky=W)
        # txtsideEffect = Entry(DataFrameLeft, textvariable=self.SideEffects,font=("arial", 12, "bold"), width=35)
        # txtsideEffect.grid(row=8, column=1)

        # lblFurtherinfo = Label(DataFrameLeft, text="Further Information:", font=("arial", 12, "bold"), padx=2)
        # lblFurtherinfo.grid(row=0, column=2, sticky=W)
        # txtFurtherinfo = Entry(DataFrameLeft,textvariable=self.FurtherInformation, font=("arial", 12, "bold"), width=35)
        # txtFurtherinfo.grid(row=0, column=3)

        # lblBloodPressure = Label(DataFrameLeft, text="Blood Pressure:", font=("arial", 12, "bold"), padx=2,pady=6)
        # lblBloodPressure.grid(row=1, column=2, sticky=W)
        # txtBloodPressure = Entry(DataFrameLeft, textvariable=self.DrivingUsingMachine,font=("arial", 12, "bold"), width=35)
        # txtBloodPressure.grid(row=1, column=3)

        lblstorage = Label(DataFrameLeft, text="Storage Advice:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblstorage.grid(row=1, column=2, sticky=W)
        txtstorage = Entry(DataFrameLeft,textvariable=self.Storage ,font=("arial", 12, "bold"), width=35)
        txtstorage.grid(row=1, column=3)

        # lblMedicine = Label(DataFrameLeft, text="Medication:", font=("arial", 12, "bold"), padx=2,pady=6)
        # lblMedicine.grid(row=3, column=2, sticky=W)
        # txtMedicine = Entry(DataFrameLeft, textvariable=self.HowToUseMedication,font=("arial", 12, "bold"), width=35)
        # txtMedicine.grid(row=3, column=3)

        # lblPatientId = Label(DataFrameLeft, text="Patient ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        # lblPatientId.grid(row=4, column=2, sticky=W)
        # txtPatientId = Entry(DataFrameLeft,textvariable=self.PatientID,font=("arial", 12, "bold"), width=35)
        # txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, text="NHS Number:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNhsNumber.grid(row=2, column=2, sticky=W)
        txtNhsNumber = Entry(DataFrameLeft,textvariable=self.NHSNo ,font=("arial", 12, "bold"), width=35)
        txtNhsNumber.grid(row=2, column=3)

        lblPatientName = Label(DataFrameLeft, text="Patient Name:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientName.grid(row=3, column=2, sticky=W)
        txtPatientName = Entry(DataFrameLeft,textvariable=self.PatientName, font=("arial", 12, "bold"), width=35)
        txtPatientName.grid(row=3, column=3)

        lblDateofBirth = Label(DataFrameLeft, text="D.O.B:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblDateofBirth.grid(row=4, column=2, sticky=W)
        txtDateofBirth = Entry(DataFrameLeft,textvariable=self.DOB, font=("arial", 12, "bold"), width=35)
        txtDateofBirth.grid(row=4, column=3)

        lblPatientAdd = Label(DataFrameLeft, text="Patient Address:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientAdd.grid(row=5, column=2, sticky=W)
        txtPatientAdd = Entry(DataFrameLeft,textvariable=self.Address,font=("arial", 12, "bold"), width=35)
        txtPatientAdd.grid(row=5, column=3)

        #============================================================Pescription textbox=============================================================================
        self.txtPrescription=Text(DataFrameRight,font=("arial", 12, "bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #================================================================Buttons=====================================================================================
        btnPrescription = Button(ButtonFrame,command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(ButtonFrame,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate = Button(ButtonFrame,command=self.update,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=24,height=1,padx=2)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(ButtonFrame,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=24,height=1,padx=2)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(ButtonFrame,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=24,height=1,padx=2)
        btnClear.grid(row=0,column=4)

        btnExit = Button(ButtonFrame,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=24,height=1,padx=2)
        btnExit.grid(row=0,column=5)

        #===================================================================ScrollBar===============================================================================

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)

        #====================================================================Table=================================================================================
        self.hospital_table =ttk.Treeview(DetailsFrame,column=("Nameoftablets","ReferenceNo","Dose","NoofTablets","Lot","IssueDate","ExpiryDate","DailyDose","Storage","NHSNo","PatientName","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM ,fill =X)
        scroll_y.pack(side = RIGHT ,fill =Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Nameoftablets",text="Name of tablets")
        self.hospital_table.heading("ReferenceNo",text="Reference No.")
        self.hospital_table.heading("Dose",text="Dose")
        self.hospital_table.heading("NoofTablets",text="No. of Tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("IssueDate",text="Issue Date")
        self.hospital_table.heading("ExpiryDate",text="Expiry Date")
        self.hospital_table.heading("DailyDose",text="Daily Dose")
        self.hospital_table.heading("Storage",text="Storage")
        self.hospital_table.heading("NHSNo",text="NHS No.")
        self.hospital_table.heading("PatientName",text="Patient Name")
        self.hospital_table.heading("DOB",text="Date of Birth")
        self.hospital_table.heading("Address",text="Address")

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("Nameoftablets",width=100)
        self.hospital_table.column("ReferenceNo",width=100)
        self.hospital_table.column("Dose",width=100)
        self.hospital_table.column("NoofTablets",width=100)
        self.hospital_table.column("Lot",width=100)
        self.hospital_table.column("IssueDate",width=100)
        self.hospital_table.column("ExpiryDate",width=100)
        self.hospital_table.column("DailyDose",width=100)
        self.hospital_table.column("Storage",width=100)
        self.hospital_table.column("NHSNo",width=100)
        self.hospital_table.column("PatientName",width=100)
        self.hospital_table.column("DOB",width=100)
        self.hospital_table.column("Address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=================================================================Functionality Declaration==================================================================
    def iPrescriptionData(self):
            if self.Nameoftablets.get() == "" or self.ReferenceNo.get() == "" :
                messagebox.showerror("Error","All fields are required")

            else:
                conn = mysql.connector.connect(host="localhost",username="root",password="SH@!um23",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.Nameoftablets.get(),
                                                                                                self.ReferenceNo.get(),
                                                                                                self.Dose.get(),
                                                                                                self.Nooftablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.IssueDate.get(),
                                                                                                self.ExpiryDate.get(),                                                                                                
                                                                                                self.DailyDose.get(),
                                                                                                self.Storage.get(),
                                                                                                self.NHSNo.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DOB.get(),
                                                                                                self.Address.get()
    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")
    
    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="SH@!um23",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,Dose=%s,Nooftablets=%s,Lot=%s,IssueDate=%s,ExpiryDate=%s,DailyDose=%s,Storage=%s,NHSNo=%s,PatientName=%s,DOB=%s,Address=%s where ReferenceNo=%s",(
                                                                                                self.Nameoftablets.get(),                                                                                                
                                                                                                self.Dose.get(),
                                                                                                self.Nooftablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.IssueDate.get(),
                                                                                                self.ExpiryDate.get(),                                                                                                
                                                                                                self.DailyDose.get(),
                                                                                                self.Storage.get(),
                                                                                                self.NHSNo.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DOB.get(),
                                                                                                self.Address.get(),
                                                                                                self.ReferenceNo.get(),
                                                                                                
    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="SH@!um23",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ReferenceNo.set(row[1])
        self.Dose.set(row[2])
        self.Nooftablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpiryDate.set(row[6])
        self.DailyDose.set(row[7])
        self.Storage.set(row[8])
        self.NHSNo.set(row[9])
        self.PatientName.set(row[10])
        self.DOB.set(row[11])
        self.Address.set(row[12])

    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" +self.Nameoftablets.get()+ "\n")
        self.txtPrescription.insert(END,"Reference Number.:\t\t\t" +self.ReferenceNo.get()+ "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" +self.Dose.get()+ "\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t" +self.Nooftablets.get()+ "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t" +self.Lot.get()+ "\n")
        self.txtPrescription.insert(END,"IssueDate:\t\t\t" +self.IssueDate.get()+ "\n")
        self.txtPrescription.insert(END,"ExpiryDate:\t\t\t" +self.ExpiryDate.get()+ "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" +self.DailyDose.get()+ "\n")
        #self.txtPrescription.insert(END,"Further Information:\t\t\t" +self.FurtherInformation.get()+ "\n")
        self.txtPrescription.insert(END,"Storage Advise:\t\t\t" +self.Storage.get()+ "\n")
        #self.txtPrescription.insert(END,"Patient ID:\t\t\t" +self.PatientID.get()+ "\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t" +self.NHSNo.get()+ "\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t" +self.PatientName.get()+ "\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t" +self.DOB.get()+ "\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t" +self.Address.get()+ "\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="SH@!um23",database="mydata")
        my_cursor=conn.cursor()
        query ="delete from hospital where ReferenceNo=%s"
        value=(self.ReferenceNo.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ReferenceNo.set("")
        self.Dose.set("")
        self.Nooftablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpiryDate.set("")
        self.DailyDose.set("")
        self.Storage.set("")
        self.NHSNo.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Address.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit > 0:
            root.destroy()
            return
               
if __name__== "__main__":
    root =Tk()
    ob=Hospital(root)
    root.mainloop()