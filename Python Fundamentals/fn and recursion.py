#function drills 
# 1.waf to find the length of a list.(list is the parameter)
#2.waf to print the elements of a list in a single line
#3.find the factotrial of n.(n is the parameter)
#4.waf to convert USD to INR.

list_1 =[1,2,3,4,5,6,'a','b','cc','dd']

def length_of_list(list):
    return len(list)

# print(length_of_list(list_1))


def print_elements(list):
    for i in list:
        print(i,end=' ')

# print_elements(list_1)


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

# print(factorial(7))

def fact_using_while(n):
    fact = 1
    while(n>0):
        fact = fact * n
        n = n-1
    return fact

# print(fact_using_while(5))

# factorial using recursion
def fact_recursion(n):
    if (n == 0):
        return 1
    else:
        return n * fact_recursion(n-1)

# print(fact_recursion(6)) 


# practice set 
# waf to calculate sum of first n natural numbers.
# never forget to have the base case first in recursion problems.
def sum_natural_numbers(num):
    if (num == 0):
        return 0 
    return sum_natural_numbers(num -1) + num

# print(sum_natural_numbers(4)) # output - 10

#write a recursive fn  to print all the elements of a list.
def display1(list):
    for i in range(len(list)):
        print(list[i], end = "-")

# display1(list_1) #this is without using recursion.

list_2 = [10,20,30]
def display(list,index=0):
    if index == len(list):
        return 
    print(list[index],end=' ') # or we can use return/ print there 
    display(list,index + 1 )
    print('a9')
display(list_2) #this is with recursion