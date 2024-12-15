import time
import os

class Bank:

    Bank_Name="Meezan Bank Limited"

    def __init__(self,account):
        os.system('cls')
        self.typewriter(f"********************************************** {self.Bank_Name} ****************************************************")
        account=int(input("Enter Yout Account Number : "))
        self.account=account
        self.balance=0

    def typewriter(self,text,delay=0):
        for char in text:
            print(char,end="",flush=True)
            time.sleep(delay)
        print()

    def debit(self):
        amount=int(input("Enter a amount you want o Debited : "))
        self.typewriter(f"{amount} Rs has been Successfully Credited in Your Account ! ")
        self.balance+=amount
        self.typewriter(f"Your Remaining Balance is {self.balance}")
        self.printing()

    def Credit(self):
        cred=int(input("Enter the amount you want to be Credited :"))
        if (cred > self.balance):
            self.typewriter("No Enough Amount")
        else:
            self.typewriter(f"{cred} Rs has been Credited in your Account !")
            self.balance-=cred
            self.typewriter(f"Your Remaining Balance is {self.balance}")
        self.printing()

    def check_balance(self):
        self.typewriter(f"Dear User : Current Balance is {self.balance}")
        self.printing()

    def printing(self):
        self.typewriter("***************************************************************************************")
        self.typewriter(f"ID : {self.account}")
        self.typewriter("")
        self.typewriter(f"1. Credit Ammount")
        self.typewriter(f"2. Debit Amount")
        self.typewriter(f"3. Check Balance")
        self.typewriter(f"4. Exit")
        inp=int(input(""))
        if inp==1:
            call.Credit()
        elif inp==2:
            call.debit()
        elif inp==3:
            call.check_balance()
        elif inp==4:
            return False
        else:
            print("Somthing Wrong")



call=Bank("")
call.printing()

