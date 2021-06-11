from datetime import datetime
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
        self.transaction=[]
        self.loan=20000

    def deposit(self,amount):
        try:
            1+amount
        except  TypeError:
            return f"The amount must be in figures"    
         
        

        self.balance+=amount
        transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
        self.transaction.append(transaction)
        return self.show_balance()  
    def show_balance(self):

        return f"Dear {self.name} you have deposited {self.amount} ypour new balance  is {self.balance}"    


    def  deposit(self,amount):
        if  amount<=0:
            return f"The amount is greater than zero" 
        else:
         self.balance += amount 
         return f"You have deposited{amount} and your balance is{self.balance}"  

    def withdraw(self,amount):
        try:
            1+amount
        except TypeError:
            return f"the amount must be in figures"
            
            
            
             

        


        if  amount<0:
            return f"The amount is lesser than zero"
        elif amount>self.balance:
            return f"Transaction not succesful"
        else:
            self.balance -= amount
          

        withdraw={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
        self.transaction.append(withdraw)
        return f"Dear {self.name}, you have withdraw{amount} and your balance is{self.balance}"
        

    def borrow(self,amount):  
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan

            return f"Dear {self.name} your loan of{self.loan} has been approved your new balance is{self.balance}"


        else:
         return  f"Dear {self.name},your loan of {self.loan}  is  not approved because the amount you want to borrow is above your limit{self.balance}"

       
    def get_statement(self):
        for transaction in self.transaction:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print("{}:You have made a {} of {}.Your new balance is {}.".format(time,narration,amount,balance)) 

    def withdraw(self,amount):
      if amount<0:
       return f"Dear {self.name} You can't borrow  amount"
      elif self.balance<amount:
       return f"Dear {self.name} Your balance is low."
      else:
       self.balance-=amount      
       return f"Dear {self.name}, You have withdrawn {amount}, Your balance is {self.balance}"
    def  show_balance(self):
     return self.balance
    def borrow(self,amount):
      if amount >=self. loan_limit:  
       return f"Dear{self. name},the amount you want to withdraw is aroud to withdraw"
      elif self.loan>0:
       return f"Dear{self.name}your loan have not been paid" 
      else:
          self.loan+=1
          self.balance+=amount
      return f"Dear {self.name}, You have borrowed {amount} your new balance is{self.balance}" 



    def repay(self,amount):
         if amount > 0:
                 return f"Dear {self.name} your loan is not valid"
         elif amount>self.loan:
            self.loan-=amount
            return f"Dear {self.name} your loan has been decreased {self.loan}"
         else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            self.balance+=amount
            now=datetime.now()

            transaction={
               "amount":amount,
               "time":now,
               "narration":"you have paid your loan"
               
            } 
            self.statement.append(transaction)
            return f"Dear {self.name} your loan has been cleared"  



    def  transfer(self,amount,account):
        try:
          1+amount
        except  TypeError:
            return f"The amount must be in figures" 
        fee=amount*0.05
        if amount+fee>self.balance:
            return f"You balance is {self.balance} ,you need  {amount+fee}"  

        else:
            self.balance-=amount+fee 
            account.deposit   (amount)
            return f"Transaction successful  you have transfered{amount} and your balance is {self.balance}"      
        


class MobileMoneyAccount(Account):
    def __init__(self, name, age, ID,service):
        super().__init__(name,age,ID)
    
        self.service=service
        self.limit=300000
 
    def  buy_airtime (self,amount):
        try:
          1+amount
        except  TypeError:
            return f"The amount must be in figures"  
        if self.balance>amount :
            return f"Hello you have bought airtime amounting to {amount}  and yor balance is {self.balance-amount}" 

        
            



