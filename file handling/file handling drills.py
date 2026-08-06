# this is a practice set for file input and output operations in python.
import readline


f1 = open('python fluency/syntax drills/sample.txt','r') 
data = f1.read() # here i am reading the file contents only using read(r) mode 
# print(data)
# print(type(data))
f1.close()


f2 = open('python fluency/syntax drills/demo.txt','r')
data2A = f2.readline() # since its the starting point, the pointer here is on the first line of demo.txt
# print(data2A)

#the main idea here for now is to understand concept of stream/pointers and thier positions in different read/write/append modes.
# readline gives you a clear intel on that.
data2B = f2.readline() #since we are on the same file 'f2',the stream/pointer has moved on to the 2nd line when previous readline was executed 
# print(data2B)

data3B = f2.readline(4) #the stream/pointer has moved again and now prints first 4 charcacters of the pointed line(3rd line in this case)
# print(data3B)
f2.close()


f3 = open("python fluency/syntax drills/sample.txt","w")
# here i  am simply deleting existing file content and overwriting everything in the file(BASICALLY trunicating)
f3.write("yes,this text is overwritten as a result of using w mode")
f3.close()

f4 = open("python fluency/syntax drills/demo.txt","a")# append = (adding content to the file not deleting the exisiting)
f4.write("\nthis is fundamental step to add content without overwriting them. becareful where your pointer is at.")
f4.close() # correctly appended at the end of the line, stream/pointer was contemporarily pointing at.

# lets move to using combined operations(both read and write)but it have its own variations
#'+' gives a add on functionality to the existing mode. 'r+' enhnaces the ability of read to write as well and so on.
# file doesnt truncate in r+ mode, but truncates in w+ mode.

f5 = open("python fluency/syntax drills/sample.txt","r+")  # r+ overwrites at the starting of the file.
data5 = f5.read() # but if i use data5 to view the data via f5, it shifts the stream/pointer to the end due to execution of read fn(method)
# print(data5)
f5.write("789")
# print(f5.read()) # here is an important observation, we cannot read the recent change(which was write operation) we did in the file until file is closed.
f5.close()

#addressing f5 issue 
f6 = open("python fluency/syntax drills/sample.txt","r+")
f6.write("@#$")
f6.close() # now this works, r+ overwrites the starting of the file.


#when we open a file in w+ mode, the exisitng content of the file is already removed and when we read, the file is null.
f7 = open("python fluency/syntax drills/demo2.txt","w+")
# print(f7.read())
f7.write("test text")
f7.close()

#if we use read&print before 'a+', it would show blank. 
#opening file in 'a+'mode, already sets the stream to the end of the content.
# it doesnt truncate but produces blank output
f8 =open("python fluency/syntax drills/demo2.txt","a+")
# print(f8.read())
f8.write("this is added by write in a+ mode") # adds/appends to the end of the line
f8.close()

#using file i/o via 'with' syntax, its like declaring a function.
with open("python fluency/syntax drills/sample.txt","r") as f9:
    print(f9.read()) # we dont require to close the file using'with' syntax and its maker stuff more modular to use.


with open("python fluency/syntax drills/sample.txt","w") as f10:
    f10.write('this is a test for write operation using with syntax')

f11 = open("python fluency/syntax drills/test3.txt","x+")
print(f11.read())
f11.write("this is a test for creating file and writing in it using x mode ")
print(f11.read()) #it has created the file and wrote in it but file has not closed yet, so shows null output uisng read&print
f11.close()

# we practiced reading and writing, creating but it now left is deleting
# we cannot delete a file directly ,so we use a builtin libary "os" module for the task

import os
os.remove("python fluency/syntax drills/test2.txt")