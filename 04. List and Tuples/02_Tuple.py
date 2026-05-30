# A tuple is an immutable data typein python. It is similiar to list but its just immutable 

# Empty Tuple
a = ()
print(type(a))

# Single Element Tuple
a = (1)
print(type(a))              # Then it will be considered as int

x = (1,)
print(type(x))

# ----------------------------------------------------------------------------------------

# Elements of tuple can't be changed if
# name = (1, 64, 'r', "Rachit", "Shreya")
# name[2] = "Sonam"
# This is will give error

# count() function counts how many times a element is in a tupple
name = (1, 64, 'r', "Rachit", "Shreya",64)
count = name.count(64)
print(count)

# index() function tells that item is on which index
i = name.index('Rachit')
print(i)
