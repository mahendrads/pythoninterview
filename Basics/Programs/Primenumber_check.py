num=int(input("please enter a number "))

if num==1:
    print("1 is not either prime or composite number")
elif num > 1:
     for i in range(2,num):
        if num % i == 0:
            print(num," is not a prime number")
            print(i, "times", num // i, "is", num)
            break
     else:
        print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")


"""
2nd appraoch
============

for i in range(2,int(num/2)+1):
    # If num is divisible by any number between
    # 2 and n / 2, it is not prime
    if num%i == 0:
        print("it is not a prime number")
        break
    else:
        print("it is a prime ")
else:
 print("it is not a prime number")

"""