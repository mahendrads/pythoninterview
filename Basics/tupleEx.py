tup_ex=(21,11,31,4,5)

#print(tup_ex[3])

#tup_ex[4]=12

#print(tup_ex)


"""
Sets


it won't maintain sequence
and not allows duplicate values


s={}  ##representatiom

not follows a sequence  

it usess hash inside sets to get the  much perforamnce


"""

s={21,13,34,54,98,56}  #{1 st out put 56, 21, 13, 54}
                       #{34, 98, 21, 54, 56, 13}

print(s)
"""

can we change the value of a set ?


No beacause 'set' object does not support item assignment 



it won't maintain seq
and not allows duplicate values
"""


# s[4]=23
#
#
# print(s)

"""
ERROR::TypeError: 'set' object does not support item assignment

"""


print(s[4])


