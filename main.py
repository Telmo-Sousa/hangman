import random
from collections import Counter

words = '''apple linux windows python computer gaming programming coding copilot github
           vim cpp vue banana orange mango guava grapes strawberry raspberry
           blueberry blackberry raspberry watermelon pineapple papaya
           engine driveshaft transmission differential suspension
           steering brakes wheels tires exhaust intake turbocharger
           food drinks snacks breakfast lunch dinner supper'''

words = words.split()
secret_word = random.choice(words)

def display_current_progress(secret_word, guessed_letters):
    display = ' '.join([char if char in guessed_letters else '_' for char in secret_word])
    print(display)

if __name__ == '__main__':
    print('Guess the word!')

    display_current_progress(secret_word, [])
    attempts_remaining = len(secret_word) + 3
    guessed_letters = set()
    word_guessed = False

    while attempts_remaining > 0 and not word_guessed:
        print(f'\nAttempts remaining: {attempts_remaining}')
        guess = input('Enter a letter to guess: ').lower()

        if not guess.isalpha() or len(guess) != 1:
            print('Enter a single letter.')
            continue
        elif guess in guessed_letters:
            print('You have already guessed that letter.')
            continue

        guessed_letters.add(guess)
        if guess in secret_word:
            if all(char in guessed_letters for char in secret_word):
                word_guessed = True
        else:
            attempts_remaining -= 1

        display_current_progress(secret_word, guessed_letters)

    if word_guessed:
        print(f'\nCongratulations, You won! The word is: {secret_word}')
    else:
        print(f'\nYou lost! The word was {secret_word}. Try again.')
