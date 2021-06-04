# class Bank:
#     def __init__(self,name,age,ID):
#         self.name=name
#         self.age=age
#         self.ID=ID
        


#     def withdraw(self):
#         return f"Helo {self.name},you are  {self.age}years old  yor ID number is {self.ID} you are allowed to withdraw from your account"
#     def Deposit(self):
#                 return f"Helo {self.name},you are  {self.age}years old  yor ID number is {self.ID} you are allowed to deposit money to your account"

class Account:
    def __init__(self,name,age,ID):
        self.name=name
        self.age=age
        self.ID=ID
        self.balance=0
        self.loan=0
        self.loan_limit=20000

    def deposit(self,amount):
        self.balance+=amount
        return f"Dear {self.name} you have deposited {amount} andyour balance is{self.balance}"   

    def show_balance(self):

        return f"Dear {self.name} you have deposited {self.amount} ypour new balance  is {self.balance}"    


    def  deposit(self,amount):
        if  amount<=0:
            return f"The amount is greater than zero" 
        else:
         self.balance += amount 
         return f"You have deposited{amount} and your balance is{self.balance}"  

    def withdraw(self,amount):
        if  amount<0:
            return f"The amount is lesser than zero"
        elif amount>self.balance:
            return f"Transaction not succesful"
        else:
            self.balance -= amount
            return f"Dear {self.name}, you have withdraw{amount} and your balance is{self.balance}"

    def borrow(self,amount):  
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan

            return f"Dear {self.name} your loan of{self.loan} has been approved your new balance is{self.balance}"


        else:
           return  f"Dear {self.name},your loan of {self.loan}  is  not approved because the amount you want to borrow is above your limit{self.balance}"


    

