
# For better understanding look at this string for reference
# ------------------------------------------------------------------------------
WORD = "0123456789"
print(WORD[1:8:3]) 
# First it will resolve [1:8] which will give us "1234567" and then it will go to every next 3rd index in new string "147" 
# index in "1234567" are 0,1,2,3,1,2,3 and so on
# -----------------------------------------------------------------------------
alpha = "abcdefghijklmnopqrstuvwxyz"
print(alpha[0:8:2])
# First it will resolve [0:8] which will give us "abcdefgh" and then it will go to every next 2nd index in new string "aceg"
# Index in "abcdefgh" are 0,1,2,1,2,1,2,1 and so on
# ------------------------------------------------------------------------------
word = "amazing"

print(word[1:4:2])   #Slicing of string from index 1 to 3 with a step of 2 (4 and 5 are not included)
# First it will resolve [1:4] which will give us "maz" and then it will go to every next 2nd index in new string "mz"
# index in "maz" are 0,1,2 and so on 
# ------------------------------------------------------------------------------