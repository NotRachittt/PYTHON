# Write a programme to find out wheather a student has passed or failed if required a total of 40 % and at least 33% in each subject to pass. Assume 3 subjects and take markss as input from user.

s1 = int(input("Enter your marks in subject 1 : "))
s2 = int(input("Enter your marks in subject 2 : "))
s3 = int(input("Enter your marks in subject 3 : "))

perc = ((s1 + s2 + s3) / 300) * 100

if perc >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33:
    print("Congratulations! You've passed the exam.")
elif s1 < 33:
    print("Sorry! You've failed in subject 1.")
elif s2 < 33:
    print("Sorry! You've failed in subject 2.")
elif s3 < 33:
    print("Sorry! You've failed in subject 3.")
else:
    print("Sorry! You've failed because your percentage is below 40%.")