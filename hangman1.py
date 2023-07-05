import random
import string

words = ['borel', 'holler', 'cutinio']

def hangman():
    word = random.choice(words)  
    word_letter = set(word)
    used_letters = set()
    live = 4
    while len(word_letter) > 0 and live != 0:
        print('Used letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('curent word:', ' '.join(word_list))
                             
        user_letter = input('Enter letter : ').lower()
        used_letters.add(user_letter)
        if user_letter in string.ascii_letters:
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                live = live - 1         
        else:
            print('invalid charactere')        
        print('\n')  
    if live == 0:
        print('You died, You made 4 wrong entries \n\n')
    else:         
        print(f"Nice you guessed the word: {word.upper()}!!! \n\n")                    
    
hangman()
