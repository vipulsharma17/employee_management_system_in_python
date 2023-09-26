
# Employee id, Employee name, Salary, Age, Gender, Address, City, DOB, DOJ, 
# Department Name, Designation, Pan Card number, Aadhar number
import os 
from validation import *
import sys
class Employee:
    EmpDict = { }
    def __init__(self,id,nm,sal,a,g,adr,c,db,dj,dnm,d,pn,an):
        self.ename=nm
        self.eid=id
        self.salary=sal
        self.age=a
        self.gender = g
        self.address=adr
        self.city=c
        self.dob=db
        self.doj=dj
        self.dname=dnm
        self.desgnation=d
        self.pan=pn
        self.adhhar=an 
        if self.dname in self.EmpDict.keys():
            self.EmpDict[self.dname].append(self.ename)
        else:
            self.EmpDict[self.dname] = [self.ename]
    
    def display(self):
        print("{:<6} {:<6} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10} {:<10} {:<15}".format(self.eid, self.ename, self.salary, self.age, self.gender, self.address, self.city,self.dob, self.doj, self.dname, self.desgnation,self.pan,self.adhhar))

    @classmethod
    def DisplayDept(self):
        for k,v in self.EmpDict.items():
            print ("Department Details : ",k)
            for name in v:
                print(name,end=" ")
            print("")
        


emplist = []
print("!!! Employee Management System !!! ")
print("")
while True:
    print("")
    print("1} Add a Employee : ")
    print("2} Display Details of Employee : ")
    print("3} Display details of Employee Department wise : ")
    print("4} Search the Employee Details : ")
    print("5} Display details of Employee  with Highest salary : ")
    print("6} Delete  Employee : ")
    print("7} Update Employee Details : ")
    print("8} Display details of Employee  with Lowest salary :")
    print("9} Exit :")
    choice = int(input("Enter your choice : "))

    if (choice == 1):
        while True:
            eid=(input("Enter the EID : "))
            if isAgeValid(eid):
                        break
            else:
                print("Invalid EID")        
        
        while True:
            enm=input("Enter the Employee name : ")
            if isNameValid(enm):
                break
            else:
                print("Invalid Name")
        while True:
            ea=input("Enter the age : ")
            if isAgeValid(ea):
                break
            else:
                print("Invalid Age !!!")
        
        while True:
            ednm =input("Enter the Department name : ")
            if ednm.isalpha():
                break
            else:
                print("Invalid Department Name !!!")
        while True:
            esal =(input("Enter the Salary : "))
            if isAgeValid(esal):
                int(esal)
                break
            else:
                print("Invalid Salary !!!")
        while True:
            eg =input("Enter the gender : ")
            if isGenderValid(eg):
                break
            else:
                print("Invalid Gender !!!")
        
        eadr =input("Enter the address : ")
        while True:
            ec =input("Enter the city : ")
            if ec.isalpha():
                break
            else:
                print("Invalid City Name !!!")
        
        while True:
            edb =input("Enter the DOB (dd/mm/yyyy) : ")
            if isDateValid(edb):
                break
            else:
                print("Invalid DOB Name !!!")
        while True:
            edj =input("Enter the DOJ (dd/mm/yyyy) : ")
            if isDateValid(edj):
                break
            else:
                print("Invalid DOJ Name !!!")
        
        ed =input("Enter the Designation : ")
        while True:
            epn =input("Enter the PanCard Number : ")
            if isPanValid(epn):
                break
            else:
                print("Invalid Pan card Number !!!")
        
        while True:
            ean =input("Enter the Aadhar Card Number : ")
            if isAadharValid(ean):
                break
            else:
                print("Invalid Aadhar Number !!!")
        
        emp = Employee(eid,enm,esal,ea,eg,eadr,ec,edb,edj,ednm,ed,epn,ean)
        emplist.append(emp)
        os.system('cls')
        # print(emplist)
    elif choice==2:
        print("{:<6} {:<6} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10} {:<10} {:<20}".format("EID", "Ename", "Sal", "Age", "Gender", "Address", "City", "DOB", "DOJ", "DeptName", "Designation", "PanCardNumber", "AadharNumber"))
        for i in emplist:
            i.display( )  

    elif choice ==3:
        Employee.DisplayDept()
        
    elif choice == 4:
        print("")
        print("Press A to search by EID")
        print("Press B to search by Department Name")
        print("Press C to search by Name")
        ch = input("Enter your choice : ")
        if (ch == "A") :
            flag=False
            count=0
            while True:
                e = (input("Enter the EID to be searched : "))
                if isAgeValid(e):
                    for i in emplist:
                        if i.eid==e:
                            i.display( )
                            flag=True
                            break
                        else:
                            count = count + 1         
                else:
                    print("Invalid EID")
                if flag:
                    break
                if (count == len(emplist)):
                    print("Not found ")
                    break               
        elif (ch=="B"):
            flag=False
            count=0
            while True:
                nm = input("Enter the Dept Name to be searched : ")
                if nm.isalpha():
                    for i in emplist:
                        if i.dname==nm:
                            i.display( )
                            flag=True
                            break
                        else:
                            count = count + 1         
                else:
                    print("Invalid Dept Name")
                if flag:
                    break
                if (count == len(emplist)):
                    print("Not found ")
                    break  


        elif (ch=="C"):
            flag=False
            count=0
            while True:
                nm = input("Enter the Name to be searched : ")
                if nm.isalpha():
                    for i in emplist:
                        if i.ename==nm:
                            i.display( )
                            flag=True
                            break
                        else:
                            count = count + 1         
                else:
                    print("Invalid  Name")
                if flag:
                    break
                if (count == len(emplist)):
                    print("Not found ")
                    break 
             
    elif choice == 5:
            m=0
            for i in emplist:
                if int(i.salary) > m:
                    m = int(i.salary)
            for i in emplist:
                if int(i.salary) == m:
                    i.display()
                    
    elif choice == 6:
        eid=int(input("Enter the Employee ID  : "))
        for i in emplist:
            if int(i.eid)==eid:
                emplist.remove(i)
                print("Record Deleted !!!")
    elif choice == 7:
        print("")
        print("A) Update the name of Employee ")
        print("B) Update the DOB of Employee")
        print("C) Update the Address of Employee")
        ch = input("Enter your choice : ")
        if (ch == "A") :
            # id = int(input("Enter the EID : "))
            # for i in emplist:
            #     if int(i.eid)==id:
            #        nm=input("Enter the name to be updated :")
            #        i.ename=nm
            #     else:
            #         print("Id not found")
            flag=False
            count=0
            while True:
                id = (input("Enter the EID : "))
                if isAgeValid(id):
                    for i in emplist:
                       if (i.eid)==id:
                           nm=input("Enter the name to be updated :")
                           i.ename=nm
                           flag=True
                           break
                       else:
                            count = count + 1         
                else:
                    print("Invalid EID")
                if flag:
                    break
                if (count == len(emplist)):
                    print("Not found ")
                    break  



                    
        elif (ch=="B"):
            id = (input("Enter the EID : "))
            for i in emplist:
                if (i.eid)==id:
                   db=input("Enter the DOB to be updated :")
                   if isDateValid(db):

                    i.dob=db
                else:
                    print("Id not found")
        elif (ch=="C"):
            id = int(input("Enter the EID : "))
            for i in emplist:
                if int(i.eid)==id:
                   adr=input("Enter the Address to be updated :")
                   i.address=adr
                else:
                    print("Id not found")
        elif (ch=="D"):
            print("")
            print("1) Update the salary of specific Employee by Employee id")
            print("2) Update the salary of all Employees working in specific department")
            print("3) Update the salary of all Employees.")
            ch = int(input("Enter your choice : "))
            if (ch == 1) :
                id=int(input("Enter the EID : "))
                
                for i in emplist:
                    if int(i.eid)==id:
                        a=int(input("Enter the Salary: "))
                        i.salary=a
                    else:
                        print("Id not found !!!")
            elif (ch==2 ):
                dnm=(input("Enter the Department Name : "))
                for i in emplist:
                    if i.dname==dnm:
                        a=int(input("Enter the Salary: "))
                        i.salary=a
                    else:
                        print("Id not found !!!")
            elif (ch == 3) :
                a=int(input("Enter the New Salary: "))
                for i in emplist:
                        i.salary=a
                    
    elif choice == 8:
        min_salary = float('inf')  # Start with positive infinity as the initial minimum

        for employee in emplist:
         if int(employee.salary) < min_salary:
            min_salary = int(employee.salary)

        for employee in emplist:
            if int(employee.salary) == min_salary:
                employee.display()
    elif choice ==9:
        sys.exit(0)
    else:
        print("Invalid choice Please Enter your choice again !!!")
