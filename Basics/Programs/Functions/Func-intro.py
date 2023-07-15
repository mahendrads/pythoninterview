def greet():

    print("fist calling")
    print("second calling")

#greet()

def mul(x,y):

    z=x*y
    y=x-y

    return z,y
greet()
res1,res2=mul(100,21)

print(res1,res2)