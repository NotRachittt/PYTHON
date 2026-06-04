# A spam comment is defined as text containing following keywords' "Make a lot of money", "Buy now", "Subscribe this", "Click this". Write a programme to detect these spams
spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe now"
spam4 = "click this"
word = input("Type your word to check spam comment : ")

if ((spam1 in word) or (spam2 in word) or (spam3 in word) or (spam4 in word)):
    print("Spam detected")
else:
    print("No spam detected")