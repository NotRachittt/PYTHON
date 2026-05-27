# type() function is used to find the type of a variable or value. It returns the type of the object passed as an argument.

a = 5
print(type(a))

b = "Hello"
print(type(b))

c = 5.0
print(type(c))

d = True
print(type(d))

e = [1, 2, 3]
print(type(e))

f = (4, 5, 6)
print(type(f))

g = {"name": "Riya", "age": 30}
print(type(g))


#typecasting is the process of converting a variable from one type to another. In Python, you can use the following functions for typecasting:
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string
# Example of typecasting
x = 5
y = float(x)  # converting integer to float
print(y)  # Output: 5.0

z = str(x)  # converting integer to string
print(z)  # Output: '5'