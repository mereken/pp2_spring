class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, money):
        self.balance+=money
        print("On your bank account:", self.balance)
        
    def withdraw(self, money):
        if self.balance>=money:
            self.balance-=money
            print("On your bank account:", self.balance)
        else:
            print("Ya vam zapreshayu")
            
dauren = Account('Dauka', 3000)
print("On your bank account:", dauren.balance)
dauren.deposit(7000)
dauren.withdraw(9000)
dauren.withdraw(1000)
dauren.withdraw(1)
dauren.deposit(50)
dauren.withdraw(51)
dauren.withdraw(49)