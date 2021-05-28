class Bank:
    def __init__(self,name,age,ID):
        self.name=name
        self.age=age
        self.ID=ID
        


    def withdraw(self):
        return f"Helo {self.name},you are  {self.age}years old  yor ID number is {self.ID} you are allowed to withdraw from your account"
    def Deposit(self):
                return f"Helo {self.name},you are  {self.age}years old  yor ID number is {self.ID} you are allowed to deposit money to your account"

