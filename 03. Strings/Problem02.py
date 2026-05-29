# Write a program to fill in a letter template in given below with name and date
'''
Dear <|Name|>
You are selected
<|Date|>            '''

name = input("Enter your name : ")
date = input("Enter Date : ")

print(f"Dear {name}\nYou are selected\n{date}")