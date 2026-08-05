# FORM A FILE CONTAINING NUMBERS SEPERATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS.
import numpy as np
with open("python fluency/syntax drills/file handling/numbers.txt","w+") as f:
    numbers = np.random.randint(1,50,20).tolist() # randomly generating 20 numbers b/w 1 to 50.
    formatted_numbers= ",".join(map(str,numbers))
    f.write(formatted_numbers)

def count_even():
    with open("python fluency/syntax drills/file handling/numbers.txt") as g:
        count = 0
        nums = g.read().split(sep=",")
        for num in nums:
            if int(num)%2 == 0:
                count += 1
        print(nums)
        return count
print(f"the number of even numbers is ", count_even())

