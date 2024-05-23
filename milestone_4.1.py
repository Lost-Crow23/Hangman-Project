
import random

# word_to_guess = random.choice(word_list)
class Hangman:

    def __init__(self, word_list: list[str], num_lives=5):
            self.word = random.choice(word_list)# TODO 2: Initialize the attributes as indicated in the docstring
            print(f"this is the word: {self.word}")
            self.word_guessed = ['_'] * len(self.word)
            self.word_len = len(set(self.word))
            print(f"This is the current state of the users guessed word: {self.word_guessed}")
            self.list_of_guesses = []

    def check_guess(self, letter) -> None:
        letter.lower
        for index, char in enumerate(self.word):
             if char == letter:
                self.word_guessed[index] == letter 
                self.word_len.discard(letter)
             print(f"Good guess {letter} is in the word")
        else:
             if letter != self.word: 
                num_lives -=1
             print(f"Sorry, {letter} is not in the word,you have {num_lives} lives left.")
    
    def ask_letter(self):
        while True:
              letter = input("Enter your letter")
              if len(letter) != 1 or ~letter.isalpha():
                   print("Please, enter just one character ")
              elif letter in self.list_of_guesses:
                   print(f"{letter} has already been tried.")
              else: 
                   self.list_of_guesses.append(letter)
                   return self.check_guess(letter)

    def play_game(word_list):
        game = Hangman(word_list, num_lives=5)
        print(f"The mystery word has {game.word_len()} characters")
        while True:
             if game.num_lives == 0:
                print(f"You lost! The word was {game.self.word}")
                break
             
        result = game.ask_letter()
        print(result)


if __name__ == '__main__':
    #  print(f"The mystery word has {self.word_len()} characters")
     word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
     play_game(word_list)
    #  word_to_guess = random.choice(word_list) 