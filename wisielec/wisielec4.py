import sys
no_of_tries = 5    
word = 'kamil'
used_letters = []
user_word = []

for _ in word:
    user_word.append('_')

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes 

def show_state_of_game():
    print()
    print(user_word)
    print('pozostalo prob:', no_of_tries)
    print('uzyte litery:', used_letters)
    print()


while True:
    letter = input('podaj litere: ')
    used_letters.append(letter)
    # print('uzyte litery', used_letters)
    found_indexes = find_indexes(word, letter) 

    if len(found_indexes) == 0:
        print('litera nie pasuje!')
        no_of_tries -= 1
        # print('pozostalo prob', no_of_tries)
        if no_of_tries == 0:
            print('koniec gry')
            sys.exit()
    else:
        for index in found_indexes: 
            user_word[index] = letter
        # print(user_word)
    if "".join(user_word) == word:
        print('brawo wygrałes!')
        sys.exit()
    show_state_of_game()