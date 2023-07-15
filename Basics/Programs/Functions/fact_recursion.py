#using recursion


def fact(x):

  if x<0:
      return "notvalid"
  elif x==1:

      return 1

  elif x > 0:
      return (x * fact(x-1))




res=fact(4)
print("using recusrion function the factorrial is :",res)