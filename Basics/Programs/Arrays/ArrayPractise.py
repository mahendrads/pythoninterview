
from array import *
import array as arr

ar_i=arr.array('i',[1,2,4,6])

ar_d=arr.array('d',[23.4,21.6,54.3])

#arr_i vefor inserting new ele

print("befor insertions",end="")

for x in ar_i:
    print(x,end=" ")
print()

ar_i.insert(2,10)

print("after insertions",end="")

for y in ar_i:
    print(y,end=" ")
print()

"""
insert==>insert at a prticular position

append ==>it adds by dafault at the end of aarray

"""


print("befor append ",end="")

for x in range(len(ar_d)):

    print(ar_d[x],end=" ")
print()


print("after  append ",end="")
ar_d.append(143.143)
for y in range(len(ar_d)):
    print(ar_d[y],end=" ")
print()

#ar_i.insert(2,10)

#print("after insertions",end="")

# for y in ar_i:
#     print(y,end=" ")

###########################

"""
Removing Elements from the Array

Elements can be removed from the array by using built-in remove() 
                                                         -------   
function but an Error arises if element doesn’t exist in the set. 

Remove() method only removes one element at a time, 

pop() function can also be used to remove and return an element from the array,
 
   but by default it removes only the last element of the array, 

to remove element from a specific position of the array, 
 index of the element is passed as an argument to the pop() method.


"""

#using pop()
print("before popping ", ar_i)
ar_i.pop(2)

print("after popping ", ar_i)



# using remove() to remove 1st occurrence of 2
ar_i.remove(2)


print("remove the occurance of 2 ",ar_i)


""""
updating array
"""

ar_i[2]=10
#ar_i[4]=20
#ar_i[5]=30

print("after updation of ar_i ",ar_i,end="")