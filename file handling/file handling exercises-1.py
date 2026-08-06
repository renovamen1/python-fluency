#Ques for Practice
# 1(a).create a new file "practice.txt" using python. add the following data in it:
''' 
hi everyone i am prabin thakur.
i am learning file handling or file i/o in Java.
i like programming in Java.
i want to built some good machine learning models. 
'''
#1(b). write a function that replaces all occurences of "java" with "python" in above file
#1(c).search if the word "learning" exsits in the file or not.

# you can open it in 'w' mode,it also creates a file but truncates
with open("python fluency/syntax drills/file handling/practice.txt","w") as f:
    f.write("hi everyone i am prabin thakur\n i am learning file handling or file i/o in Java\n i like programming in Java\n i want to built some good machine learning models")
   
with open("python fluency/syntax drills/file handling/practice.txt","r+") as g:
    words = g.read()
    updated_words=[]
    for word in words.split():
        if word.strip(".,!") in ["java","JAVA","Java"]:
            updated_words.append("python")
        else:
            updated_words.append(word)
    content = " ".join(updated_words)
    g.seek(0) #since this is r+ mode, pointer/stream already begins from 0. but the previous read have shifted the stream. so need to set it to begining.
    g.truncate()
    g.write(content)

with open("python fluency/syntax drills/file handling/practice.txt","r") as h:
    words = h.read()
    count = 0
    for word in words.split():
        if(word == 'learning'):
            count+= 1  
    if count > 0:
        print("yes,the word exists")
    else:   
        print("no,the word doesnot exist")

#WAP TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST.
#PRINT -1 IF NOT FOUND


def find_line_no(word):
    '''
    function which returns the line number in which a particular word is contained.
    '''
    line_no = 1 
    data = True
    with open("python fluency/syntax drills/file handling/demo.txt","r") as i:
        while data:
            data = i.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1

find_line_no("first")