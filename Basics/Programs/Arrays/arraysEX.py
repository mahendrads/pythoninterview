from array import  *

vals=array('i',[10,20,-12,34])

# i meeans allows negaive also

print(vals)

print(vals.typecode)
#print("reverse array :",vals.reverse())

print(vals)

#iterating


#print(vals.buffer_info()) #gives the size of the array
#(2727117226480, 4)
#1 --<>address 2->size

#dyna,ic appraoch
for i in range(len(vals)):
    print(vals[i])

#still the below is also works
for e in vals:
    print(e)


#vals2=array('u',['a','e','i','o'])
newar=array(vals.typecode,(a for a in vals))

for i in range(len(newar)):
    print(newar[i])