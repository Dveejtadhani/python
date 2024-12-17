#!/usr/bin/env python
# coding: utf-8

# In[1]:


# opening a file:
f = open("filename.txt","mode")
# values of mode = reading(r), writing(w), append(a), r+(r n w), w+, a+,


# In[ ]:





# In[16]:


f = open("Will.txt","w")
# various property of file property
# 1. name
# 2. mode
# 3. closed
# 4. readable()
# 5. writeable()
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


# In[35]:


# writing data to txt file
f = open("Will.txt","w")
f.write("hello, how are you doing? \nhaha \n")
f.close()


# In[1]:


f = open("Will.txt","w")
list = ['a','A',"lksad"]
f.writelines(list) #input only in list[]
f.write("\n hello...")
f.close()


# In[2]:


# Reading character from the txt file
# 1. read()
# 2. read(n)
# 3. readline()
# 4. readlines()
f = open("Will.txt","r")
print(f.read())
f.close()


# In[3]:


f = open("Will.txt","r")
print(f.read(3))
f.close()


# In[4]:


f = open("Will.txt","r")
print(f.readline())
f.close()


# In[89]:


f = open("Will.txt","r")
print(f.readlines())
f.close()


# In[85]:


f = open("Will.txt","r+")
f.write("abc")
print(f.readline())
f.close()


# In[87]:


f = open("Will.txt","w+")
f.write("gudnyt")
print(f.read())
f.close()


# In[91]:


f = open("Will.txt","a+")
f.write("Hello")
f.close()


# In[129]:


f = open("Will.txt","a+")
print(f.read()) #pointer at last, o/p = ntgs
f.close()


# In[134]:


# WAPP to create a file hello.txt and printed "hello world" in 1000lines
f = open("hello.txt","w")
for i in range(0,1000):
    f.write("Hello world\n")
f.close()


# In[136]:


# WAPP to count number 0f lines in txt file
f = open("hello.txt","r")
r = f.readlines()
print(len(r))


# In[1]:


# WAPP to create a list that contians the first word of every line in the textfile
f = open("first.txt","w+")
f.write("hello hi\nGood morning\nHow are you\nI am fine")
f.close()


# In[25]:


f = open("first.txt")
l = []
for i in f: 
    i.split()
    x = i.split()
    l.append(x[0])
print(l)


# In[35]:


# WAPP to create a list contains the words that has character 'e'
f = open("first.txt")
l = []
for i in f: 
    for j in i.split(): 
        if 'e' in j:
            l.append(j)
print(l)


# In[42]:


# WAPP to copy all contain of one file to another file in reverse other
f1 = open("file1.txt","r")
f2 = open("reverse.txt","w+")
x = f1.read()
reverse = x[::-1]
f2.write(reverse)
f1.close()
f2.close()


# In[57]:


# WAPP to copy odd numbers line of one file to another file 
f1 = open("file1.txt","r")
f2 = open("oddfile.txt","w+")
x = f1.readlines()
odd = x[::2]

        f2.write(x[i])
f1.close()
f2.close()

        


# In[64]:


# WAPP that read a file line-by-line each line read from txt file is copied to another file with line number specified as prefix of line
f1 = open("file1.txt")
f2 = open("prefix.txt","w+")
x = f1.readlines()
l = len(x)
for i in range(l):
    f2.write(str(i+1)+" "+ x[i])
f1.close()
f2.close()


# In[81]:


# WAPP to reverse the contain of one file and store it in second file 
# and also convert the contain of second file into uppercase and store it into thrid file 
# and also count number of vowels in thrid file and also print only second line from the contain of the thrid file 
f1 = open("one.txt")
f2 = open("two.txt","w+")
f3 = open("three.txt","w+")
x1 = f1.read()
reverse = x1[::-1]
f2.write(reverse)
f1.close()
f2.close()
x2 = reverse.upper()
f3.write(x2)
f3.close()
count = 0
f3 = open("three.txt")
x3 = f3.readlines()
for i in x3:
    if 'E' or 'A' or 'U' or 'V' or 'I' in i:
        count+=1
print("Count of vowels in thrid file:",count)
print("Second line from the thrid file:",x3[1])


# In[123]:


f3 = open("three.txt")
x3 = f3.read()
v = x3.split()
count = 0
print(v)
for i in v:
    for j in i:
        print(j)
        if ('E' or 'A' or 'U' or 'I' or 'O') == a:
            count+=1
        else: 
            pass
print("Count of vowels in thrid file:",count)
print("Second line from the thrid file:",x3[1])


# In[132]:


# WAPP to count words,character and spaces from text file
f1 = open("one.txt")
x = f1.read()
words = x.split()
print("count of words:",len(words))
print("count of space:",x.count(" "))
count = 0
for i in x:
    for j in i:
        count+=1
print("count of character:",count)


# In[5]:


# WAPP to accept a sentence from a user till the user enter "END" each sentence entered by the user should be a new line in file
# display only those line which begins with capital letter 
file  = open("user.txt","w+")
x = input("Enter a sentence: ")
while x!="END":
    if x=="END":
        pass
    else:
        file.write(x+"\n")
        x = input("Enter a sentence:")
file.close()
f = open("user.txt")
line = f.readlines()
l = len(line)
for i in range(0,l):
    if line[i][0].isupper():
        print(line[i])
    else: 
        pass


# In[ ]:


# WAPP to count frequency of words in the giiven txt file 
f = open("one.txt")
x = f.read()
words = x.split()
l = []
for i in words:
    if i not in l:
        l.append(i)
    else:
        pass
for i in l:
    print(i,x.count(i))


# In[ ]:


# WAPP such that your solution should promt for a file name and display five lines at a time from the txt file..
# pausing each time to ask the user to press any key to continue or 'q' to exit
# filename = input("Enter filename: ")
file = open("file1.txt")
x = file.readlines()
count = 0
flag = 0
l = len(x)
print(l)
for i in range(len(x)):
        if flag == 0:
                for j in range(0,5):
                    print(x[count])
                    count+=1
                    l-=1
                inp = input("press any key to continue or press 'q' to stop and exit")
                if inp=='q':
                    flag=1
                else:
                    flag=0
        elif flag == 1:
            break  
file.close()    


# In[9]:


# WAPP to search a word in text file 
file = open("one.txt")
x = file.read()
list = x.split()
print(list)
l = len(list)
ip = input("Enter the word: ")
cnt = 0
for j in list[cnt]:
    if j.find(ip):
        print("Word found at line",j)
        print(x.index(ip))
    cnt+=1
        


# In[61]:


# WAPP to compare to text file if they are different give the row and column number in the file where the first difference occurs 
f1 = open("one.txt")
f2 = open("one1.txt")
x1 = f1.readlines()
x2 = f2.readlines()
l1 = []
l2 = []
for i in x1: 
    for j in i:
        l1.append(j)
for i in x2: 
    for j in i:
        l2.append(j)
l = len(l1) if len(l1)>len(l2) else len(l2)
line = 0
for i in range(0,l):
    if x1[i]==x2[i]:
        pass
    else:
        print("difference found at line(row)",i+1)  
        line = i
        break
z = len(x1[line])
for i in range(0,l):
    if l1[i]==l2[i]:
        pass
    else:
        print("column",(i+1)-z)


# In[8]:


# WAPP to open the file mbox.txt and read it line-by-line and print mail id 27
f = open("mbox.txt")
x = f.readlines()
print(x)

f.close()


# In[20]:


# WAPP to read file mbox.txt and figure out who has send the greatest number of the mail
f = open("mbox.txt")
x = f.readlines()
count = 0
dic = {'a':1,'b':2}
for i in x:
    s = i.split()
    for j in range(len(s)):
        if s[j]=="From":
            print(s[j+1])
            l1.append(s[j+1])
            count+=1


print(count)
print(dic.key(1))
f.close()


# In[63]:


# 1. avg 
# 2.pick your fav team and determine how many game they win and they lost
# 3.find the team that lost by thirty or more points the most times
# 4.find all the team that lost by 70 or points 
file = open("MVK/scores.txt")
x = file.readlines()
sum = 0
# l = len(x)*2
# for i in x:
#     d = i.split()
#     sum += int(d[2])+int(d[4])
# print("Task-1 avg of scores:",sum/l)

# Task-2
# fav = input("Enter your fav team: ")
# win,loss=0,0
# for i in x:
#     d = i.split()
#     if d[1]==fav:
#         if int(d[2])-int(d[4])>0:
#             win+=1
#         else:
#             loss+=1
#     elif d[3]==fav:
#         if int(d[4])-int(d[2])>0:
#             win+=1
#         else:
#             loss+=1
# print("Task-2 win:",win,"loss:",loss)
print("Task-3 team lost by 30 or more points:")
dif=0
dif2=0
l = []
for i in x:
    d = i.split()
    if int(d[2])-int(d[4])>=30:
        l.append(d[3])
    if int(d[4])-int(d[2])>=30:
        l.append(d[1])
print(l)
op = max(l)
print(op)


# In[11]:


file = open("file1.txt")
# to get the position of the pointer 
print(file.tell())
x = file.read()
print(file.tell())
# to move pointer to a position
c = file.seek(10)
print(file.tell())

# another way of opening a file
with open("file1.txt") as f:
    y = f.read()
    print(y)


# In[17]:


# NEW CHAPTER-7 
import Beck
print(Beck.a)
Beck.sum(39,20)


# In[19]:


# importing as a varibale 
import Beck as x
print(x.b)
x.product(2,4)


# In[33]:


# to import particular functions only
from Beck import product,b
print(b)
product(2,3)


# In[28]:


#  to import all the functions
from Beck import *
sum(2,3)
product(9,9)


# In[30]:


from Beck import a as d
print(d)


# In[41]:


# 1. To know current working dir 
import os
print(os.getcwd())
# 2. To create sub-dir in current working dir
# os.mkdir("Quinn") #ye naam ka folder ban jayega
# 3. To delete a folder(dir)
# os.rmdir("Quinn")
# 4. To delete a file 
# os.remove("h1.html")
# 5. To rename a file or folder
# os.rename("Beck.py","loveQuinn.py")
# 6. To get list(ls)
# print(os.listdir())


# In[1]:


import mortal123
str = input("Enter a string: ")
mortal123.u(str)
mortal123.l(str)
mortal123.t(str)
mortal123.s(str)
mortal123.cap(str)


# In[2]:


# try-except
try: 
    a = 20
    b = 0
    print(a/b)
except:
    print("ERROR")
# try-except-exception
try: 
    a = 20
    b = 0
    print(a/b)
except Exception as e:
    print(e)
    print(e.__class__)
# catching specific exception in python 
try: 
    a = int(input())
    b = int(input())
    a1 = [1,2,3]
    print(a1[3])
    print(a/b)
except IndexError:
    print("index error")
except ZeroDivisionError:
    print("not divisible by zero")


# In[9]:


#write a program to search a word  from a text file add which position type word is not found if word is not found
e=open("file1.txt",'r')
a=e.read()
f=a.split()
print(f)
char=input('enter char: ')
for i in f:
    if char==i:
        print('word is found: ',i)
        break;
    else:
        print('-1')
        break;


# In[ ]:




