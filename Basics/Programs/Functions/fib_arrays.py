def fib(n):

    if n<=0:
        return "invalid input"

    data=[0,1]

    if n>2:
        for i in range(2,n):

            data.append(data[i-1]+data[i-2])
        return data[n-1]
print(fib(9))