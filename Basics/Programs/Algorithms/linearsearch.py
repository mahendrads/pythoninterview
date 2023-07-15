
pos =-1
def search(lst,n):

    i=1
    while i<len(lst):
        if lst[i] == n:
            globals()['pos']=i
            return True
        i=i+1
    return False

lst=[20,13,14,156,65,87]
n=156

if search(lst,n):

     print("elelment " ,n,"is found","in the",pos+1 ,"th position ")
else:
    print("elelment " ,n,"is not found")
