name=['hola','muy','bien']

num=[10,30,50]

mix=['cincenta',50,'ocho',8,4.6,'cuatroseis']

res_cb=[name,mix,num]

#print(res_cb)

####list operationss #####
res_cb.append(40)
print(res_cb )   #by default it adds end of list
#[['hola', 'muy', 'bien'], ['cincenta', 50, 'ocho', 8, 4.6, 'cuatroseis'], [10, 30, 50], 40]

print(res_cb.count(50))   ##50 how many times there   ---0

res_cb.insert(3,40)
print(res_cb)


#Example 2: Inserting a Tuple (as an Element) to the List

tuple_ex=(2,3)

res_cb.insert(2,tuple_ex)

print('inserted tiuple at 2nd position :',res_cb)

#The extend() method adds all the elements of an iterable
# (list, tuple, string etc.) to the end of the list.


# create a list
prime_numbers = [2, 3, 5]

# create another list
numbers = [1, 4,444]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5]

#Syntax for extend is

#list1.extend(iterable)


languages = ['French', 'English']

languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language

languages1.extend(languages)

languages1.remove('Spanish')

print('after removing spanish :',languages1)


print('using pop method :',res_cb.pop())

del res_cb[2:]

print(res_cb)






