"""
formal
actual
default
keyword
varaible length

"""
#variable length arguments


# *b means we can assign multiple values
def sum(a,*b):

    #a int and b is a tuple
    print(type(a))
    print(type(b))

    c=a

    for i in b:
        c=c+i

    print("varable legth arg with in is (12,12,13,14): ",c )


sum(12,12,13,14)


"""
keyword arguments
==================


"""


def kwargsex(name,**data):
    for i,j in data.items():
        print(i,j)

kwargsex(name="mahe",city='mumbai',age=20)

