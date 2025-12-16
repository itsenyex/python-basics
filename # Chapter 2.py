# Chapter 2

name = input("what is your name?\n and phone number ")
print (name)
#\n means new line in the output of the code. codewars.com

num = input ("Enter Number :")
print (num)
name1 = input ("Enter Name :")
print (name1)

#CountDown time.
import time 

count_seconds = 60
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print (i, end= '>>>')
        time.sleep(1)
    else:
        print ('start')