sets = {1,2,4,3,4,5,5,6,4,5,7,8,8,9}
print(type(sets))
print(sets)     

# add() function adds new value unique value to sets
sets.add(10)
print(sets)

print(len(sets))            # Prints length of sets


sets.discard(100)  # No error even if 100 is not present
sets.remove(8)       # remove() function removes the subsequent value from sets
print(sets)

sets.pop()          # pop method removes any random element from sets. Often, with small integer sets, it may appear to remove the smallest element, but you should not rely on that behavior.
print(sets)

sets.clear()            # clear() empties the set 
print(sets)


# -----------------------------------------------------------------------

s1 = {1,2,3,5,9,12}
s2 = {1,2,6,5,4,12}

# Union of sets
print(s1.union(s2))

# intersection of sets
print(s1.intersection(s2))