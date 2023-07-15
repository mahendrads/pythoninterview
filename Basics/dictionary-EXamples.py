
dict1={1:"mahendra",
       2:"nali",
         6:"indra"}


print("dictionary is printed as :",dict1)

print("retriving values based on a key which is  present ::",dict1[2])


#print("retriving values based on a key which is not present ::",dict[4]) #KeyError: 4


#print("retriving values based on a key which is not present ::",dict[4]) #KeyError: 4

"""
using dict.get()  method

if key is not present in dict it won;t throw any error 

returns NONE
"""

print("Get() method returns :",dict1.get(4))

print("Get() method returns  custom values:",dict1.get(4,"KeyNotFound"))

"""
Python zip() method takes iterable containers and returns a single iterator object,
 
It is used to map the similar index of multiple containers so that they can be used just using a single entity. 

Syntax :  zip(*iterators) 

Parameters : Python iterables or containers ( list, string etc ) 
------------------------------------------------------------------
Return Value : Returns a single iterator object.

"""
keys=['mahendra','nali','loves','python']
values=[1,3,4,5]

#merge two lists with ZIP() and convert to DICTIONARY using dict
dict_com=dict(zip(keys,values))

print(dict_com)

dict_com['newkey']='newvalue'


print("after updation:",dict_com)


prg={ 'pyhon':["pycharm","VSS","Sublime","IDE"], 'java':{'J2EE':'eclipse','j2se':'netbeans'}}

print("prg dict contains",prg['java']) #prg dict contains {'J2EE': 'eclipse', 'j2se': 'netbeans'}

print("prg java  dict contains ::",prg['java']['j2se']) #prg java  dict contains netbeans



print("prg Python  dict contains ::",prg['pyhon']) #prg Python  dict contains :: ['pycharm', 'VSS', 'Sublime', 'IDE']


print("prg Python  dict contains ::",prg['pyhon'][1]) #prg Python  dict contains :: VSS

 ###
 #As it is a list we can use index

###