    #Chapter One
print (False == 0)
print (True == 1)
print (True + False + True)
print (True + False + False)
print (True + True *  False)
print (None == 0)
print (None == [])

#showing logical operation 
# or (returns true)
print(True or False)
#showing logical operation
# and (returns false)
print (False and True)
#showing logical operation
# not (returns false)
print(not True)
# using "in" to check
if 's' in 'geeksforgeeks':
    print ("s is part of geeksforeeks")
else:
    print ("s is not part of geeksforgeeks")

for i in range (10):
    print(i, end=" ")
if i== 6:
    #in the book the next line should be break but isn't working.
 sys.exit()
print()

i= 0
while i < 10:
 # if i is equals to 6,
 # continue to next itration
 # without printing
    if i == 6:
        i += 1
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
        i += 1
