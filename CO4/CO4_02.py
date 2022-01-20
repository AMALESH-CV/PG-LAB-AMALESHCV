class Bank:
    def __init__(self):
        self.acbal=0
        
    def details(self):
        print("\nEnter Your Account Details\n")
        self.acno=int(input("Enter Your Account Number: "))
        self.name=input("Enter Your Name: ")
        self.actype=input("Enter Type of Account: ")
        
    def display(self):
        print("\n YOUR BANK ACCOUNT DETAILS \n")
        print("YOUR ACCOUNT NUMBER IS: ",self.acno)
        print("YOUR NAME IS: ",self.name)
        print("YOUR ACCOUNT TYPE IS: ",self.actype)
        print("YOUR CURRENT ACCOUNT BALANCE IS: ",self.acbal)
        
    def deposit(self):
        self.amount=int(input("Enter the Amount to be Deposited: "))
        self.acbal=self.acbal+self.amount
        print("Balance After Deposit: ",self.acbal)
        
    def withdraw(self):
        self.amount=int(input("Enter the Amount to be Withdrawn: "))
        self.acbal=self.acbal-self.amount
        print("Balance After Withdrawel: ",self.acbal)
        
        
B=Bank()
B.details()
x=1
while(x!=0):
        print("\nEnter Your Choice \n 1.Deposite\n2.Withdraw\n3.View Account Details\n")
        x=int(input("Enter Choice: "))

        if x==1:
            B.deposit()
        elif x==2:
            B.withdraw()
        elif x==3:
            B.display()
        else:
            print("\n Invalid Operation")



