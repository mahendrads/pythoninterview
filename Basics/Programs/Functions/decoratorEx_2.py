

#<!--Example 1: Treating the functions as objects. -->

def func(text):
    return text.upper()

print(func('Hello'))

objectEx=func
print(objectEx("Function as object"))

""""

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …

"""


#passing fucntion as arhuments

def func(text):
    return text.upper()
def func2(text):
    return text.lower()

def func3(funasvariable):
    #storing function as a variablke
    func3=funasvariable("from func3 funtion as argument")

    print(func3)

func3(func)
func3(func2)



#Example 3: Returning functions from another function.

def adder(x):
    def inner(y):
        #logic to modify
       return (x+y)
    return inner

add_15=adder(15)

print(add_15(10))



