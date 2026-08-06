# to map with real sceanrios, we started using objects in code. that is called object oriented programming.
# a class is a blueprint for creating objects.

class Employee:
    name = "Prabin Thakur"
    salary = "$10000000"
    def __init__(self,fullname):
    #     print(self)
    #     print(fullname)
        print("hi, the constructor test was successfull")

E1 = Employee("god")
# print(E1)

# ALL CLASSES HAVE A INIT FUNCTION [__init__()],WHICH IS ALWAYS EXECUTED WHEN THE OBJECT IS BEING INITIATED.
# CONSTRUCTOR OR THE INIT FUNCTION IS AUTOMATICALLY CALLED WHEN WE INITATE OR CREATE AN OBJECT (INSTANCE OF A CLASS)

# the self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class.
# in this sceanrio, E1 is the object (instance of the class 'Employee')

class Faculty:
    def __init__(self,teacher): # we can use any word inplace of "self",its just common convention.
        # whats more important is the idea that it is itself referencing to a same instance of class(object) we create. 
        self.name = teacher

f1 = Faculty("Pritam")
# print(f1.name)

# there are two types of constructors: default and parameterized 
# we can have two constructors in a class and {object attribute > class attribute}
class staff:
    def __init__(self): #this is a default constructor
        pass 
    def __init__(self,name,designation): # this is a parameterized constructor
        self.name = name 
        self.designation = designation
        self.age = 16

staff1 = staff("alice","manager")
# print(staff1.name, staff1.designation,staff1.age) 
# which among the two constructor is called simply depends upon the number of arguments passed, the one that matches

# if we have a class attribute with a same name as obj attribute , obj attribute is more preferred

# methods are functions that belong to objects.
# example:
class agent_A:
    def __init__(self,model_name,provider):
        self.model_name = model_name
        self.provider = provider
    def pricing(self):
        self.pricing = "$4/1M tokens"
        return self.pricing
agent1 = agent_A("claude-fable-5","anthropic")
# print(agent1.provider)
# print(agent1.model_name)
# print(agent1.pricing())

# practice questions
#CREATE STUDENT CLASS THAT TAKES  student NAME AND MARKS OF 3 SUBJECTS AS ARGUMENTS IN CONSTRUCTOR.
#THEN CREATE A METHOD TO PRINT THE AVERGAE

class Student:
    def __init__(self,name,sub1_marks,sub2_marks,sub3_marks):
        self.name = name
        self.subject1_marks = sub1_marks
        self.subject2_marks = sub2_marks
        self.subject3_marks = sub3_marks

    def average(self):
        return (self.subject1_marks+self.subject2_marks+self.subject3_marks)/3


s1 = Student("Peter Parker",89,98,92)
# print(s1.subject2_name,s1.subject2_marks)
# print(s1.average())


# we can do this same using list
class Students:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    def avg_marks(self):
        sum = 0
        for itr in self.marks:
            sum += itr
        return sum/3


S1 = Students("Peter Parker",[89,78,91])

# S1.name = "Spiderman"
print("hello",S1.name,"your average score is",S1.avg_marks())

