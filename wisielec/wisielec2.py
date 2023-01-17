import sys
#gra wisielec - sprawdzanie kazdej litery w slowie


no_of_tries = 5  #ilosc zyc
word = 'kamila'   #slowo klucz
user_word = []
used_letters = []    #slowa uzyte przez gracza

def find_indexes(word, letter): #petla szukajaca litery w slowie klucz
    indexes = []                #index  
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


########

for _ in word: #podkreslenia wedlug dlugosci slowa klucz
    user_word.append('_')  
while True: #PETLA NIESKONCZONA
    letter = input('podaj litere: ')
    used_letters.append(letter)
    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print('nie ma takiej litery')
        no_of_tries -= 1

        if no_of_tries == 0:
            print('Przegrałes! słowo to:', word)
            sys.exit(0)
            
    else:
        for index in found_indexes:
            user_word[index] = letter

        if ''.join(user_word) == word:
            print('brawo poprawne slowo')
            sys.exit(0)
    show_state_of_game()