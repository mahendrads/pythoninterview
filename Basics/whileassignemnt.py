#print all the numbers from 1to 100 and skip 3 and 5 multiplies

"""
i=1

while i in  range(100):
    # if i % 3==0 and i % 5==0:
    #   # i=i+1

    if i%3!=0 and i%5!=0:

        print(i, end=" ")
    i = i + 1
   """
"""
print the below pattern

    #####
    #####
    #####
    #####

"""

i=0

while i<=5 :
     print("#",end="") #end ="" print on the same line
     j = 1
     while j <=5:
         print("#",end="")
         j=j+1
     i=i+1
     print()