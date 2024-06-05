secret_word = "apple"

def check_guess(guess):
    """
    checks the guess from our variable (secret_word)

    also checks if it's within the alphabet (.isalpha)
    
    param a: guess
    type guess: str(string)

    using an if statement to iterate over the string assigned to variable

    len: length of single element in variable inputted

    return: checks the single alphabet within the secret_word to be valid or false
    """
    guess.lower() 
    if len(guess) == 1 and guess.isalpha():
        if guess in secret_word:
            # if in secret_word, prints out the correct guessed letter
            print(f"Good guess!{guess} is in secret word {secret_word}")
        else:
            # prints out false if entered incorrectly or letter not within the secret_word
            print(f"Sorry, {guess} is not in the word {secret_word}. Try again")

    
def ask_input(guess):
    """
    asks input from the user which then initialises the check_guess function

    calling out the check_guess function

    param1 = guess

    While = if true and is an alphabet , breaks the loop and returns the guess with a message

    else: if false, returns statement invalid
    """
    check_guess(guess)
while True:
    # player inputs a letter as a guess
    guess = input("Guess a letter: ")
    if guess.isalpha():
        print(guess)
        break
    else:
        print("invalid letter, Please, enter a single alphabetical character")

ask_input(guess)