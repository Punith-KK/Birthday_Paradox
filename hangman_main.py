import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list
def hangman_all():
    chosen_word = random.choice(word_list)
    lives = 6

    print(f'Pssst, the solution is {chosen_word}.')
    print(logo)
    print("You have 6 lives left.")
    display = []
    for letter in chosen_word:
        display.append('_')
    while '_' in display:
        guess = input("Guess a letter: ").upper()

        if guess in display:
            print(f"Hmmm, I think you already guessed the letter '{guess}' ...")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        if not guess in chosen_word:
            print( f"Ooops o_O that letter is not in the word, you lose a life ...{lives-1} lives left ")
            lives -= 1
            print(stages[lives])
        if lives == 0:
            print('You lose')
            break
        print(f"{' '.join(display)}")
    if lives != 0:
        print('You win!')
