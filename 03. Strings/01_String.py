# String is sequence of characters.


a = 'Hello World'           #Single quoted string
b = "Hello World"           #Double quoted string
c = """Hello World"""       #Triple quoted string

str = "Happy"
str1 = str[0:3]         #Slicing of string from index 0 to 2 (3 is not included)
print(str1)

character = str[1]        #Accessing the first character of the string
print(character)

str2 = str[-4:-1]     #Slicing of string from index -4 to -2 (-1 is not included)
print(str2) 

print(str[ : 4])       #Slicing of string from index 0 to 3 (4 is not included)
print(str[2 : ])       #Slicing of string from index 2 to the end of the string
print(str[ : ])        #Slicing of string from index 0 to the end of the
print(str[-3 : ])      #Slicing of string from index -3 to the end of the string
print(str[ : -3])      #Slicing of string from index 0 to -4 (-3 is not included) 