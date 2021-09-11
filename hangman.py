import random
from words import words
import string


# In order to test the word list do
# print(words) which will print out all the imported words, allowing you to check for errors.

def get_valid_word(words):  # Defining a function to make sure only valid words are used in our game.
    word = random.choice(words)  # this line will randomly choose a word from the imported word list.
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


# user_input = input('Type anything:')
# print(user_input)
# ^ Making sure my way of collecting user input works.

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # imports all uppercase characters in english
    used_letters = set()  # stores what the user has guessed

    lives = 7

    # getting user input here
    while len(word_letters) > 0 and lives > 0:  # Loop to keep user playing until game ends.
        print('You have', lives, 'lives left. You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()  # the .upper() makes all characters appear in uppercase.
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # add the guessed letter to used letters.
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # each time user guesses correctly word_letters decreases.

            else:
                lives = lives - 1  # takes away a life if wrong.
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')
    # when len word letters = 0 or lives = 0, the loop ends and game is over\
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You have guessed the word', word, '!')


hangman()
