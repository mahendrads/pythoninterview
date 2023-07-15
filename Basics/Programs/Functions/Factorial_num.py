def fact(n):
    f=1

    if n <0:
        return "not a valid"
    elif n==0:
        return 1
    else:
        for i in range(1,n+1):

            f= f*i

        return fact

res=fact(4)

print(res)