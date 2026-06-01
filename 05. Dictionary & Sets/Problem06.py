# Can you change values inside a list which is contained in set s
# s = { 8, 15, 12, "Rachit", [1,2] }

s = { 8, 15, 12, "Rachit", [1,2] }

# You can't index the set
# Firstly you can't include list in a set S because set require all the elements to be immutable ad hashable . List are mutable and not hashable. 

# OR

# A set can only contain hashable (immutable) elements.
# Lists are mutable, so they are not hashable.
# Therefore, a list cannot be an element of a set.