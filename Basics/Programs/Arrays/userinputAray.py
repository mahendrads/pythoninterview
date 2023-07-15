from array import *

arr=array('i',[])

n=int(input("enter the length of the array "))

for x in range(n):
    y=int(input("enter the next value"))
    arr.append(y)
print(arr)

val=int(input("enter the value to search for "))

index_k=0
for e in arr:
    if e == val:
       #    print("val is ",val,"index is ",arr[val])
        print(index_k)

    index_k=index_k+1
print(arr.index(val))