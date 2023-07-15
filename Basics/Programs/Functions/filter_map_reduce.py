#filter gives us the sequence


def even_fun(n):
    return n%2==0

lst=[2,4,5,6,7,8.10,12,23]

"""
    filter takes fucnion and uterables as args
"""
evens=list(filter(even_fun,lst))

print(evens)

"""
the above can be optimized using anonymous(lambda) functions like below 
"""

res_with_lambda=list(filter(lambda n:n%2==0 ,lst))
print("res with anonymous function",res_with_lambda)

###############################################################


"""
Map 
"""
def doubles(n):
    return n*2


"""
  map(func, *iterables) --> map object
"""

res_map=list(map(doubles,evens))

print(res_map)

"""
the above can be optimized using anonymous 
"""

doubles=list(map(lambda x:x*2,evens))
print("with anonymous func ",doubles)


##############Reduce #####

from functools import reduce

def red(a,b):
    return a+b

res_red=reduce(red,doubles)

print(res_red)



res_red_anonymous=reduce(lambda x,y:x+y,doubles)
print("res_red_anonymous ==> ",res_red_anonymous)