#Python Sets
 #Creating a set
set1 = set()
print("initial blank set:")
print(set1)

#set with the useof a string

set1 = set("micksformicks")
print("\nSet with the use of a string:")
print(set1)

#set with the use of a constructor
#(using the objects to store string)

string = 'micksformicks'
set1 = set(string)
print("\nSet with the use of an objet:")
print (set1)

#set with the use of a list

set1 = set(["micks", "for", "micks"])
print("\nSet with the use of a list")
print(set1)

#Set with a list of numbers with duplicate values

set1 = set([1,2,4,4,3,3,3,6,5])
print("\nSet with the use of numbers:")
print(set1)

#set with a mixed value (nubers and strings)
set1 = set([1,2,'micks',4,'for',6,'micks'])
print("\nSet with a mixed value")
print(set1)

#Addition of elements in a set

set1 =set()
print ("initial blank set:")
print (set1)
# adding elements and tuple
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after addition of elements:")
print(set1)

#using Remove() method
set1.remove(8)
set1.remove(9)
print(set1)

