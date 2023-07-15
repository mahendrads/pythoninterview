





"""
Test whether Tuples are Memory Efficient

"""


"""

When to Use Tuples Over Lists?
In Python, tuples and lists are both used to store collections of data,
 but they have some important differences. Here are some situations where you might want to use tuples instead of lists – 

Immutable Data –   
==============

        Tuples are immutable, thus once they are generated, their contents cannot be changed. 
        This makes tuples a suitable option for storing information that shouldn’t change,
         such as setup settings, constant values, or other information that should stay the same while your programme is running.


Performance – Tuples are more lightweight than lists
              and might be quicker to 
                                   generate, 
                                   access, and iterate 
               through since they are immutable.
               Using a tuple can be more effective than using a list if you have a huge collection of data that you need to store, retrieve, and use regularly and that data does not need to be altered.

Data integrity – By ensuring that the data’s structure and contents stay consistent, tuples can be utilised to ensure data integrity. To make sure the caller is aware of how much data to expect, for instance, if a function returns a set amount of values, you might want to return them as a tuple rather than a list.

"""
"""
import sys
a_list = []
a_tuple = ()
a_list = ["Geeks", "For", "Geeks"]
a_tuple = ("Geeks", "For", "Geeks")
#print(sys.getsizeof(a_list))  #88
#print(sys.getsizeof(a_tuple)) #64

#so tuple is memory efficient
"""
"""
As tuples are stored in a single memory block
therefore they don’t require extra space for new objects

whereas the lists are allocated in two blocks,
 first the fixed one with all the Python object information and
 second a variable-sized block for the data.

"""
"""

Test whether the implication of iterations is comparatively faster in Tuples

As tuples are stored in a single memory block, therefore, 
they don’t require extra space for new objects as they are immutable 
whereas the lists are allocated in two blocks, first the fixed one with all the Python object information and 
second a variable-sized block for the data which makes them even faster.
import sys, platform
import time

l = list(range(100000001))
t = tuple(range(100000001))

start = time.time_ns()
for i in range(len(t)):
    a = t[i]
end = time.time_ns()
#print("Total lookup time for Tuple: ", end - start)   #11665649300

start = time.time_ns()
for i in range(len(l)):
    a = l[i]
end = time.time_ns()
#print("Total lookup time for LIST: ", end - start)  #15418586500

"""

"""
indexing 
-------

 Both lists and tuples allow you to access individual elements using their index, starting from 0.
 
 EX:
 my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
 
print(my_list[0]) # Output: 1
print(my_tuple[1]) # Output: 5



Python Slicing
-------------

Both lists and tuples allow you to extract a subset of elements using slicing.



"""


my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)

print('list slicing  ::: ',my_list[1:3])
print('tuple slicing::::',my_tuple[1:3])



"""

Python Concatenation
==============

Both lists and tuples can be concatenated using the “+” operator.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (7, 8, 9)
tuple2 = (10, 11, 12)
 
print(list1 + list2) # Output: [1, 2, 3, 4, 5, 6]
print(tuple1 + tuple2) # Output: (7, 8, 9, 10, 11, 12)


Note – However, there are some operations that are available only for lists, due to their mutability. 


tuple1=(1,2,3)

print(tuple1.append(23))
print(tuple1.append(2))


AttributeError: 'tuple' object has no attribute 'append'


But list allows append
"""


"""

Python Extend
============
Lists can also be extended with another list using the extend() method.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) # Output: [1, 2, 3, 4, 5, 6]


Python Remove
Lists can have elements removed using the remove() method. 

my_list = [1, 2, 3, 4]
my_list.remove(2)
print(my_list) # Output: [1, 3, 4]


"""

