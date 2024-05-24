
import random

class Hangman:
    
    def __init__(self, word_list: list[str], num_lives=5) -> None:
            # Initializing the attributes as indicated in the docstring
            self.num_lives = num_lives
            self.word = random.choice(word_list) 
            print(f"This is the word: {self.word}")
            self.word_guessed = ['_'] * len(self.word) # 
            self.num_letters = len(set(self.word))
            print(f"This is the current state of the users guessed word: {self.word_guessed}")
            self.list_of_guesses = []

    def __check_guess(self, guess) -> None: 
        guess.lower() # converts capitals in word to lowercase
        if guess in self.word:
            print(f"Good guess!: {guess} is in secret word {self.word}")
            for char in range(len(self.word)): # guess (letter) Itirates over the index's with the length of the word
                if self.word[char] == guess:
                    self.word_guessed[char] = guess
            self.num_letters -=1
        else:
            print(f"Guess {guess} not is not in secret word {self.word}: ")   
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word,you have {self.num_lives} lives left.")
        print(self.word_guessed)
    
    def ask_letter(self):
        while True:
            letter = input("Enter your letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character: ")
                break
            elif letter in self.list_of_guesses:
                print(f"{letter} has already been tried.")
                break
            else: 
                self.list_of_guesses.append(letter)
                self.__check_guess(letter)
                break
