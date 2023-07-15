###Squrre  4*4

# for i in range(4):
#     for j in range(4):
#         print("#",end="")
#     print()

"""
output

####
####
####
####

"""

###traingle

for i in range(4):
   for j in range(4):
       if i>=j:
           print("#",end="")
   print()


"""

#
##
###
####
"""


#2nd approach


for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print()


"""
####
##
###
#
"""

#print the above pattern

for i in range(4):
    for j in range(4-i):
            print("#",end="")
    print()