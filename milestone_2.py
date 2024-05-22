import random 

fav_fruits = ["Apple", "Kiwi", "Strawberry", "Banana", "Mango"]

word_list = (fav_fruits)

word = (random.choice(word_list))

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print(f"good guess")
else:
    print("oops! That is not a valid input")

print(word)

