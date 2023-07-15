

pos=-1
def search(lst,n):
    for i in range(len(lst)):
        if lst[i]==n:
            globals()['pos']=i
            return True
    return False


lst=[1,4,3,5,6,7,8,9,19]

n=int(input("enter the element to searching for "))


if search(lst,n):
    print("element",n," is found at",pos+1,"position")
else:
    print("element is not found")
