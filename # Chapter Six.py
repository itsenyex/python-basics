# Chapter Six
# #Understanding python Tupules

# creating empty tupules
Tuple1 =()
print("initial empty tuple:")
print (Tuple1)

#tuple with the use of string
Tuple1 =('micks', 'for')
print("\nTuple with the use of string:")
print(Tuple1)

#tuple with the use of list
list1 = [1,2,3,4,5,6]
print("\nTuple using list:")
print(tuple(list1))

#tuple with built-in fuctions
Tuple1 = tuple('micks')
print ("n\Tuple with the use of functions:")
print (Tuple1)

#tuple with mixed data types
Tuple1 = (5,'welcome',7,'micks')
print ("n\Tuple with mixed data types:")
print (Tuple1)

#tuple with nested turtle
Tuple1 = (0,1,2,3)
Tuple2 = ('python','mick')
Tuple3 = (Tuple1,Tuple2)
print ("n\Tuple with nested tuple:")
print (Tuple3)

#tuple with use of loop
Tuple1 = ('micks')
n = 5
print ("n\Tuple with the use of loop:")
for i in range(int(n)):
    Tuple1 =  (Tuple1)
    print (Tuple1)
