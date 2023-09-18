from random import randint


class Bank:
    def __init__(self):  # Constructor (Memory Initialize)
        self.accountNumber =  randint(100000, 999999)
        self.name = input("Enter your account name = ")
        self.balance = 0
        self.branch = input("Enter branch name = ")
    
    # def createAccount(self):
    #     self.accountNumber = randint(100000, 999999)
    #     self.name = input("Enter your account name = ")
    #     self.balance = 0
    #     self.balance = input("Enter branch name = ")

    # def createAccount2(self, name: str, branch: str = "City Light", balance: int = 0):
    #     self.accountNumber = randint(100000, 999999)
    #     self.name = name
    #     self.balance = balance
    #     self.branch = branch

    def showBalance(self):
        print(f"Your current balance is = {self.balance}")

    def transfer(self,other,amount):
        if self.balance>amount:
            self.balance-=amount
            other.balance+=amount
            
            print()
            self.showBalance()
            print()
            other.display()
        else:
            print("not suffcient balance")


    def withdraw(self):
        amt = int(input("Enter amount to withdraw = "))
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amt
            self.showBalance()

    def deposit(self):
        amt = int(input("Enter amount to deposit = "))
        self.balance += amt
        self.showBalance()
        
    def display(self):
        print(f"Account number = {self.accountNumber}")
        print(f"Account name = {self.name}")
        print(f"Account balance = {self.balance}")
        print(f"Account branch = {self.branch}")

accounts:[object]=[]

accounts: list[Bank] = []

while True:
    print("\n1) Add an account")
    print("2) View all accounts")
    print("3) Search a account")
    print("4) deposite in your account")
    print("5) withdraw in your account")
    print("6) Transfer money ")
    print("7) Exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        # accounts.insert(0, obj)
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts added till yet")
        else:
            for i in range(0, len(accounts)):
                accounts[i].display()
    elif choice==3:
         while True:
            print("\n1) search by name")
            print("2) search bu acount-num")
            print("3) Exit")
            choice1 = int(input("Enter your choice = "))
            if choice1==1:
                name1=input("enter your name: ")
                for i in range(0, len(accounts)):
                    if accounts[i].name==name1:
                        print(accounts[i].display())
                        break
                else:
                    print("No data found according to name")
            elif choice1==2:
                acc=int(input("Enter your acc number = "))
                for i in range(0,len(accounts)):
                    if accounts[i].accountNumber==acc:
                        print(accounts[i].display())
                        break
                else:
                     print("No data found according to account num")
            else:
                break

    elif choice==4:
        acc=int(input("Enter your acc number = "))
        for i in range(0,len(accounts)):
            if accounts[i].accountNumber==acc:
                accounts[i].deposit()
                accounts[i].display()
                break
        else:
            print("Enter proper acc number")
    elif choice == 5:
        acc=int(input("Enter your acc number = "))
        for i in range(0,len(accounts)):
            if accounts[i].accountNumber==acc:
                accounts[i].withdraw()
                accounts[i].display()
                break
        else:
            print("Enter proper acc number")
    elif choice == 6:
        acc=int(input("Enter your acc number = "))
        acc2=int(input("Enter your acc number = "))
        amount=int(input("Enter amount you wish to trandfer: "))
        flag=False
        for i in range(0,len(accounts)):
            if accounts[i].accountNumber==acc2:
                other=accounts[i]
                flag=True
                break
        else:
            print("Enter proper acount number 2")
        if flag:
            for i in range(0,len(accounts)):
                    if accounts[i].accountNumber==acc:
                        accounts[i].transfer(other,amount)
                        break
            else:
                print("Enter proper acc number 1")
    elif choice == 7:
        break
    else:
        print("Invalid Choice")