import math
import  math as m


"""
The sine function is math.sin(), and the arc sine function is math.asin().

Here's an example of finding the sine of 30 degrees. 

Use math.radians() to convert degrees to radians.
    ===========================================   

"""

print(m.sin(m.radians(30)))

print(m.asin(m.radians(30)))  #sin inverse


"""
print('{:.3}'.format(sin30))
print(type('{:.3}'.format(sin30)))
# 0.5
# <class 'str'>

print(format(sin30, '.3'))
print(type(format(sin30, '.3')))
# 0.5

"""
#using round()

print(round(m.sin(m.radians(30)),3))   #round(sin(30),3)
#usinif format()


print('{:.3}'.format(m.sin(m.radians(30))))


#format fiunction

print(format(m.sin(m.radians(30)),'.4'))


#
# print(m.cos(m.radians(30)))
# print(m.tan(m.radians(30)))