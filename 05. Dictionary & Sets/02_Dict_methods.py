marks = {
    "rachit" : 100,
    "shreya" : 86,
    "riya" : 94,
    "tushar" : 90
}

print(len(marks))

print(marks.items())        # items() function returns a list of (key,value) tuples.

print(marks.keys())         # keys() function prints all the keys for corresponding value pairs.

print(marks.values())        # values() function prints all the values for corresponding key pairs.

marks.update({"rachit" : 99, "shivam" : 92})       # update() function updates the past value of key pair.
print(marks)

# You might think these two methods are same but 
# print(marks["riya01"])                      this gives you error. 
# print(marks.get("riya01"))                this gives you none.

print(marks["riya"])
print(marks.get("riya"))