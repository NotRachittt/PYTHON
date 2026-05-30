mobile = ["Apple", "Samsung", "Realme", "Oppo", "Vivo", "iqoo"]
# You can store any kinda datatype item in List
print(mobile[0])
print(mobile[3])
# This prints item on given index

# Unlike strings List can be changed (mutable).
mobile[4] = "Redmi"
print(mobile[4])
print(mobile[1:4])

# append() function add new item at end of list
mobile.append("Nokia")
print(mobile)

# insert() function adds item at given index
numbers = [1,5,56,4,8,65,15,2]
numbers.insert(2,69)
print(numbers)

# pop() function will delete item at given index
numbers.pop(0)
print(numbers)

# remove() function will delete that value in a list
numbers.remove(5)
print(numbers)

# sort() function sorts the items in given list
numbers.sort()
print(numbers)
#OR
alphas = ['a','d','t','e','p','u','o','g','c','x','z']
alphas.sort()
print(alphas)
#OR
mobile.sort()
print(mobile)

# reverse() function reverse the sorting way of items
alphas.reverse()
print(alphas)