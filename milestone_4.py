
import random

class Hangman:

    def __init__(self, word_list: list[str], num_lives=5) -> None:
            self.num_lives = num_lives
            self.word = random.choice(word_list)# TODO 2: Initialize the attributes as indicated in the docstring
            print(f"This is the word: {self.word}")
            self.word_guessed = ['_'] * len(self.word)
            self.num_letters = len(set(self.word))
            print(f"This is the current state of the users guessed word: {self.word_guessed}")
            self.list_of_guesses = []

    def check_guess(self, guess) -> None:
        guess.lower()
        if guess in self.word:
            print(f"Good guess!: {guess} is in secret word {self.word}")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
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
                self.check_guess(letter)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    print(f"The mystery word has {str(game.num_letters)} characters")
    print(''.join(game.word_guessed))
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        if '_' not in game.word_guessed or game.word_guessed == game.word:
            print("Congratulations! You Won! ")
            break
        else:
            game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)