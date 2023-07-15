# import sys
#
# sys.setrecursionlimit(2000)
# print(sys.setrecursionlimit(2000))
# i=0
# def greet():
#   global i
#   i+=1
#   print("Hello",i)
#   greet()
#
#
# greet()


#using recursion fact

def fact(a):

 if a==0:
  return 1

 return a*fact(a-1)




res=fact(5)
print(res)