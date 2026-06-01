# What will be the length of following sets
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))
# This will give length as 2 even if datatypes are int, floaitng , string because In Python, 1 == 1.0 is True because Python compares their numeric values, not just their types.