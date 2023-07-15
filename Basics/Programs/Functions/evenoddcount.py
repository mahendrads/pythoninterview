#count the no of even numbers and odd numbers in a list

def lstcount(lst):
    even=0
    odd=0

    for i in lst:

        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd



lst=[1,2,3,4,6,5,78,9,10,11,13,15]
e,o=lstcount(lst)
print("even :{} ,odd is :{}".format(e,o))