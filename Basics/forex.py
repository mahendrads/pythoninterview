# for x in range(100):
#     if x%3==0 or x%5==0:
#         continue
#     print(x,end=" ")
# print("Bye")
#

for x in range(10,51):

    if x %2!=0:
        continue
    else:
        print(x)

"""      

The pass statement in Python is used when a statement 
   
   is required syntactically but you do not want any command or code to execute. 
   It is like null operation

# Python program to demonstrate
# pass statement


s = "geeks"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'k':
		print('Pass executed')
		pass
	print(i)


"""