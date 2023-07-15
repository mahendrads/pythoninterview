

pos=-1
def search(lst,n):
       l=0
       u=len(lst)-1
       while l<=u:
       #for i in range(len(lst)):
           mid = (l + u) // 2  # inger division
       #while l <= u:
           if lst[mid] ==n:
               globals()['pos']=mid
               return True
           else:
               if lst[mid] < n:
                   l=mid
               else:
                    u=mid

lst=[1,4,3,5,6,7,8,9,19]
n=7
#n=int(input("enter the element to searching for "))


if search(lst,n):
    print("element",n," is found at",pos+1,"position")
else:
    print("element is not found")
