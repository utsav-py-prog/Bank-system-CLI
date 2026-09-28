#  A  BASIC BANKING SYSTEM USING PYTHON
import random
import string

def heading():

    print("----------------------------------------------------------------------------------------------------------")
    print("                                 WELCOME TO BANK CLI                                                 ")
    print("----------------------------------------------------------------------------------------------------------")

heading()


def generate_captcha():

    chars= string.ascii_letters

    return "".join(random.choice(chars) for i in range(5))

Accountnum=None

Name=None

Balance=0

service={"Create Account":1,
         "Pin":2,
         "Check Balance":3,
         "Deposite":4,
         "Withdraw":5,
         "Update":6,
         "Find Account":7,
         }
def read_accounts():
    accounts=[]
    try:
        with open("Account.txt","r") as f:

            content=f.read()

    except FileNotFoundError:
        return accounts

    content=content.replace("\r\n","\n")
    if not content.strip():

        return accounts
    
    for record in content.strip().split("\n\n"):

        record=record.strip()

        if not record:

            continue
        try:
            line=record.split("\n")

            Name=line[0].split(":",1)[1].strip()

            accnum=int(line[1].split(":",1)[1].strip())

            Balance=int(line[2].split(":",1)[1].strip())

            accounts.append({"Name": Name, "Accountnum": accnum, "Balance": Balance})

        except(IndexError,ValueError):
            continue
    return accounts
    
def write_accounts(accounts):

    with open("Account.txt","w") as f:
        for acc in accounts: 

            f.write(F"Name:{acc["Name"]}\nAccount Number:{acc["Accountnum"]}\nBalance:{acc["Balance"]}\n\n")


def find_acc(accounts,acnum):
    for acc in accounts:

        if acc["Accountnum"]==acnum:
            return acc
        
    return None

def save_file_to():
   print("----------------------------------------------------------------------------------------------------------")
   print("                                 WELCOME TO ACCOUNT FILE                                             ")
   print("----------------------------------------------------------------------------------------------------------")
   
   with open("Account.txt","a") as f:
      
      f.write(F"Name:{Name}\nAccount Number:{Accountnum}\nBalance:{Balance}\n\n")

def create():
     global Accountnum
     global Name
     global Balance
     Name=input("PLEASE ENTER YOUR NAME: ")

     GovId =input("Choose a Government ID of your choice (ADHAAR/PANCARD): ")

     if GovId=="ADHAAR":
          
          Number=int(input("enter your ADHAAR number: "))

         
          print("ADHAAR entered")

          Accountnum=random.randint(1000000000,9999999999)

          print(F'Your Account Number is: {Accountnum}')

          print("----------------------------------------------------------------------------------------------------------")

          Balance=0

          save_file_to()

           
    

     elif GovId=="PANCARD":

             Number=input("enter your PANCARD number: ")

             if Number.isalnum():
              
              Accountnum=random.randint(1000000000,9999999999)

              print(F'Your Account Number is: {Accountnum}')

              Balance=0

              save_file_to()

             else:
              
              print("Invalid GovID")
     else:
      
      print("INVALID ID")


def Pin():

    accounts=read_accounts()

    acnum=int(input("Enter your account number: "))

    acc=find_acc( accounts, acnum)

    if acc is None:

        print("No Account Exists Yet.")

        return
    
    AcPin=int(input("Enter Your six Digit Pin: "))

    confirmPin=int(input("Re enter Your six Digit Pin: "))

    if AcPin==confirmPin:
            print("Pin Created")
    else:
            print("Pin does not match")


def findaccount():
   accounts=read_accounts()

   Acnum=int(input("Enter your Account number: "))
   acc=find_acc(accounts,Acnum)
   if acc is None:
       
       print("INVALID ACCOUNT NUMBER")
       return
   
   capthca=generate_captcha()

   print(f"Captcha: {capthca}")

   entered_captcha=input("ENTER CAPTCHA AS SHOWN ABOVE: ")

   if entered_captcha==capthca:
                       
     print(F"Name:{acc["Name"]}")

     print(F"Accountnum:{acc["Accountnum"]}")

     print(F"Balance:{acc["Balance"]}")

   else:
       print("INCORRECT CAPTCHA")




def Checkbalance():
   accounts=read_accounts()

   Acnum=int(input("Enter your account number: "))

   acc=find_acc(accounts,Acnum)

   if acc:
       print(F"Account balance {acc["Balance"]}")

   else:
       print("INVALID ACCOUNT NUMBER")
 
 
def Deposite():
  
  accounts=read_accounts()

  AccNum=int(input("Enter your accont number: "))

  acc=find_acc(accounts,AccNum)

  if acc:
    Amount=int(input("Enter amount: "))
  
    
    acc["Balance"]+=Amount
    
    write_accounts(accounts)
        
    print(F"{Amount} has been credited . Avl balance{acc["Balance"]}")
 


  else:

    print("INVALD ACCOUNT NUMBER")



def withdraw():
    accounts=read_accounts()

    AccNum=int(input("Enter your account number: "))

    acc=find_acc(accounts,AccNum)

    if acc:

        Amount=int(input("Enter amount: "))

        if acc["Balance"]>= Amount:

            acc["Balance"]-=Amount

            write_accounts(accounts)

            print(F"{Amount} has been withdrawn. Avl balance{acc["Balance"]}")

        else:
            print("Low Balance")

    else:
        print("INVALID ACCOUNT NUMBER")


    

def update():

    choice=input("Do you want to Update your details?")

    if choice!="yes":
        return

    accounts=read_accounts()

    acnum=int(input("Enter account number: "))

    entered_name=input("enter your name to verify: ")

    acc=find_acc(accounts,acnum)

    if acc and acc["Name"]==entered_name:

        Details=input("What do you want to change?")

        if Details!=Name:

            new_name=input("Enter new name: ")

            acc["Name"]=new_name

            write_accounts(accounts)

            print(F"New name is {new_name}")



        else:
            print("Unsupprted field")
    else:
        print("INVALID ACCOUNT NUMBER OR NAME")

     



service_call={1:create,
              2:Pin,
              3:Checkbalance,
              4:Deposite,
              5:withdraw,
              6:update,
              7:findaccount,
              } 
while True:
    print(service)

    user=int(input("Enter The service that you require: "))

    if user in service_call:
     
     service_call[user]()
    else:
        print("INVALID SERIVCE REQUESTED!")

    again = input("Do you want another service? (Yes/No): ")

    if again != "Yes":
        print("Thank You!")
        break
    
