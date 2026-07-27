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

print(fact_recursion(6))