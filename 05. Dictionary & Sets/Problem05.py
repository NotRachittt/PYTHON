# Create a empty dictionary. Allow 4 firends to enter their favourite languages as value and use key as their names. Assume that the names are unique.

d = {}
 
name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite language : ")
d.update({name : lang})

print(d)