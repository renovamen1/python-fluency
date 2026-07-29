# this is a practice set for file input and output operations in python.
import readline


f1 = open('python fluency/syntax drills/sample.txt','r') 
data = f1.read() # here i am reading the file contents only using read(r) mode 
# print(data)
# print(type(data))
f1.close()


f2 = open('python fluency/syntax drills/demo.txt','r')
data2A = f2.readline()
# print(data2A)

#the main idea here for now is to understand pointers and thier positions in different read/write/append modes.
# readline gives you a clear intel on that.
data2B = f2.readline()
# print(data2B)

data3B = f2.readline(4)
# print(data3B)
f2.close()


f3 = open("python fluency/syntax drills/sample.txt","w")
# here i  am simply deleting existing and overwriting everything in the file(BASICALLY trunicating)
f3.write("yes,this text is overwritten as a result of using w mode v2")
f3.close()

f4 = open("python fluency/syntax drills/demo.txt","a")
f4.write("this is fundamental step to add content without overwriting them. becareful where your pointer is at.")
f4.close() # correctly appended at the end of the line, pointer was contemporarily pointing at.
