word = "EXCELLENT WORK BY JJ"

print(len(word))        # len() function is used to find length of a string

print(word.endswith("ENT"))     # endswith() function is used to check if the string ends with the specified suffix "ENT" or not. It returns True if the string ends with the specified suffix, otherwise it returns False.

print(word.startswith("EXE"))   # startswith() function is used to check if the string starts with the specified prefix "EXC" or not. It returns True if the string starts with the specified prefix, otherwise it returns False.

print(word.capitalize())     # capitalize() function is used to convert the first character of the string to uppercase and the rest of the characters to lowercase.

print(word.title())         # title() function is used to make first letter of every word capital.

print(word.find("BY"))          # str.find() function tells the world on which index it is at... ie 14 for space and word on 15

print(word.replace("WORK" , "EFFORT"))      # str.replace() function replaces the word by another word.