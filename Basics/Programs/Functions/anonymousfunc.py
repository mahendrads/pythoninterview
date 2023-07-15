def square(n):
    a=n*n
    return a

res=square(10)
#print(res)


"""
the above code can be optimized using Anonymous finction

A function without a name ==> Anonymous function
"""

f=lambda a:a*a  #as in python everything is a form of object we should assign to some other variable
res=f(20)
print(res)


n=lambda x,y:x+y
res1=n(2,3)
print(res1)