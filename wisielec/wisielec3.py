import sys

word = 'sowa'
used_letters = []
user_word = []
no_of_tries = 5

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
def show_state_of_game():
    print()
    print(user_word)
    print('pozostało prob:', no_of_tries)
    print('uzyte litery', used_letters)
    print()


#___________________________________________________________________
for _ in word:
    user_word.append("_")

while True:
    letter = input('podaj litere: ')
    
    if len(letter) < 2:
        used_letters.append(letter)
        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            no_of_tries -= 1
            print('nie ma takiej litery\nutrata zycia')

            if no_of_tries == 0:
                print('przegrana! koniec zyc')
                sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print('brawo wygrana')
                sys.exit(0)
        
    else:
        print('podaj jedna litere')

    show_state_of_game()
