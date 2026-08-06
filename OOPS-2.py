# THIS PYTHON FILE INTENDS TO COVER MAIN CONCEPTS OF OOPS
# (abstraction,encapsulation,inheritance,polymorphism)


# hiding the implemntation details of a class and only showing the essential features to the user.
# here is a implementation of abstraction as a concept of Gun 

class Gun:
    def __init__(self):
        self.bullet_loaded = False
        self.cocked = False
        self.trigger_is_pulled = False

    def aim(self):
        self.bullet_loaded = True
        self.cocked = True
        print("target is locked and the bullet is ready to fire")
    def shoot(self):
        self.trigger_is_pulled = True
        print("the gun is fired at the target")


pistol = Gun()
pistol.aim() # when we are calling aim, we are only showing little info to the user and hiding the loading bullets and cocking details.
pistol.shoot() 


# Encapsulation
# wrapping data and functions into a single unit(object)

# practice exercises 
# CREATE ACCOUNT CLASS WITH TWO ATTRIBUTES- balance & account no.
#create methods for debit,credit and printing the balance.

class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.account_no = acc_no
    def debit(self,debit_amt):
        self.balance = self.balance - debit_amt
        print(debit_amt,"has been deducted from your account")
        print("the current balance is ",self.balance)

    def credit(self,credit_amt):
        self.balance = self.balance + credit_amt
        print(credit_amt,"has been transferred to your account")
        print("the current balance is ",self.balance)

    def print_bal(self):
        print("the current balance is",self.balance)

acc1 = Account(40000,"601A")
acc1.print_bal()
acc1.credit(7000)