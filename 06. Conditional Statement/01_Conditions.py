# In python we must execute the expressions in code when they magtch certain conditions given respectively 
# EXAMPLE :
age = int(input("Enter you age : "))

# If , elif , else ladder
if(age >= 18):
    print("You can now vote")
elif(age<0):
    print("You entered wrong age")
else:
    print("You cannot vote right now")

print("\nThis is end of Programme")

# ---------------------------------------------------------------------------

# if is used to test the first condition.
# elif is used to test additional conditions.
# else executes when all conditions are false.
# Only one block of the ladder executes at a time.
# It helps in handling multiple choices efficiently.

# if condition1:
#     # code block
# elif condition2:
#     # code block
# elif condition3:
#     # code block
# else:
#     # code block