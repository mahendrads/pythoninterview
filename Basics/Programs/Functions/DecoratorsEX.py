###
def div(a,b):
    return a/b

def modifydiv(func):
 #function inside another function
 #modifying logic has to write here
    def innerfunc(a,b):
            if a < b:
                a,b=b,a
            return func(a,b)
    return innerfunc

div=modifydiv(div)

#res=div(2,4)
print(div(2,4))

"""
Decorators are a very powerful and useful tool in Python
since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

"""