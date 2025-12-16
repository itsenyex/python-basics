# Creating a list
list = []
print ("initial blank list")
print(list)

# Creating a list with the use of multipe values
list = ["Michaelmick"]
print("\nList with the use of string: ")
print (list) 

# Creating a list with the use of multiple values
list = ["micheal", "mick"]
print("\nlist containing multiple values: ")
print (list[0])
print (list[1])

# List of numbers
list = [1, 2, 3, 4]
print("n\List if numbers:")
print(list)

# List for strings using NEGATIVE < index.
list = [1, 2, "meeks", 4, "for", 6, "meeks"]
print("\nList items:")
print (list[-2])
print (list[-6])
print (list[-7])
print (list[-5])
print (list[-1])



# Getting the size of a list
list1=[10, 20, 30]
print (len(list1)) 

# Adding to a list with the append function
list= [1, 2, 3, 4,]
list1 = ('hello')
list.append (list1)
print(list)

# Insert function
list = [1, 2, 3, 4,]
list.insert(8, 'micks')
print (list)

#reversing a list
mylist = [1, 2, 3, 'mick', 'fick', 'python']
mylist.reverse()
print(mylist)

#demonstrating list comphrension 
# for square of odd numbers between 1-11 
odd_square = [x ** 2 for x in range (1, 11) if x % 2 ==1]
print (odd_square)
