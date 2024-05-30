import random

class Hangman:
    """
     A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    num_lives: int
        The number of lives the player has
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    
    
    """


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
        """
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter, thus reducing the num_letters variable by 1.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        (' __ ' = private methods cannot be accessed directly from outside the class, but used within class/subclass)

        guess: str
            The letter to be checked

        """
        # converts capitals in word to lowercase
        guess.lower() 
        if guess in self.word:
            print(f"Good guess!: {guess} is in secret word {self.word}")
            # guess (letter) Itirates over the index's with the length of the word
            for char in range(len(self.word)):
                if self.word[char] == guess:
                    self.word_guessed[char] = guess
            self.num_letters -=1
        else:
            print(f"Guess {guess} not is not in secret word {self.word}: ")   
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word,you have {self.num_lives} lives left.")
        print(self.word_guessed)
    
    def ask_letter(self):
        """

        Asks the user for a letter and checks two things:
        1. If the character is a single character and within the alphabet
        2. If the letter has already been tried and within the list of guesses
        3. Appends the letter into the list of guesses tried
        If it passes both checks, it calls the check_letter method.
        
        
        """

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

def play_game(word_list):
    """

    1. Initializes as an hint of unique characters within the word
    2. Iteratively asks the user for a letter until the user guesses the word or runs out of lives
    # If the user runs out of lives, prints "You lost! The word was {word}"
    # If the user guesses the word, prints "Congratulations! You won!"
    3. If everything is false, calls the function of {ask_letter}

    Parameters
    ----------

    word_list 
        passes the word list as a variable to play the game 

    """
    game = Hangman(word_list, num_lives=5)

    """
    game = Instance of the class, which passes and equals to the class 
    """
    print(f"The mystery word has {str(game.num_letters)} unique characters")
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
    """
    # __name__ = __main__ if this file is imported as a module, code would not run
    # ensures it executes only when the file is run directly as a script
    1. {Word_list} to be passed 
    2. Call the function play game
    
    Returns 
    -------
    Mystery word with the visual users "guessed so far" list
    word_list may be edited or improved to enhance the game or offer a variety of words
    """
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)