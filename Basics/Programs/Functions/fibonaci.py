#n-th Fibonacci number Using Dynamic Programming with Space Optimization


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
        print()

        return b


# Driver Program

print(fibonacci(9))

# def fibo(n):
#     a=0
#     b=1
#     c=a+b
#
#
#     if n==1:
#
#         print(a)
#
#     else:
#         print(a)
#         print(b)
#
#     for i in range(2,n):
#         c=a+b
#         #swap the numbers
#         a=b
#         b=c
#
#
#         print(c)
#
#
#
#
# fibo(-2)