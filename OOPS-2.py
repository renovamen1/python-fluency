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
        self.aim()
        self.trigger_is_pulled = True
        print("the gun is fired at the target")


pistol = Gun()
# pistol.aim() # when we are calling aim, we are only showing little info to the user and hiding the loading bullets and cocking details.
# pistol.shoot() 


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

# acc1 = Account(40000,"601A")
# acc1.print_bal()
# acc1.credit(7000)


# del keyword -- used to delete object properties or the object itself.
class Harvest:
    def __init__(self,crop_name):
        self.name = crop_name

harvest1 = Harvest("paddy")
# print(harvest1.name)
# to delete a object attribute , use [del object.attribute]
del harvest1 # to delete the entire object itself
# print(harvest1.name) # this line now errors as harvest1 as a object was deleted by previous line 


#PUBLIC AND PRIVATE ATTRIBUTE 
# PUBLIC AND PRIVATE  IS ONLY APPARENT ENTITY IN PYTHON UNLIKE JAVA, C++
#thus its only private(like) attributes and methods
class Google_acc:
    def __init__(self,gmail,password):
        self.gmail = gmail
        self.__password = password # here we have made this attribute private by using 2 underscores infront of its name
    def reset_pass(self,new_password):
        current_pass = self.__password
        print("the current password is",current_pass)
        self.__password = new_password
        print("the new password is set to",self.__password)
    def __pvt_method(self):
        print("this is for just to test about making a method private")

google_1 = Google_acc("prab1n@gmail.com","abcd123")
# print(google_1.gmail)    # this is a public attribute since it can be accessed outside the class
# print(google_1.password) # this way sensitive data is vulnerable. we dont want our credentials to be exposed 
# to fix it, we simply make the attribute private by putting (__) 2 underscores infront of attribute name 
# google_1.reset_pass("changed_pass123") # we can still call & view the password becuase private means it cannot be accessed outside classs but we can infer and call within the class
# google_1.__pvt_method() # yup, this works. method of object(google_1) is set to private and only can be acccessed with in the class