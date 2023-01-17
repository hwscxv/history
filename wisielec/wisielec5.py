import sys
word = 'sowa'
no_of_tries = 5
user_word= []
used_letters = []



def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter== letter_in_word:
            indexes.append(index)
    return indexes
def show_game_status():
    # print()
    print()
    print(user_word)
    print('uzyte litery:', used_letters)
    print('pozostalo zyc:', no_of_tries)
    print()







for _ in word:
    user_word.append('-')
#------------------------------------------------------------------------------------------------------------------------
while True:
    letter = input('podaj litere: ')
    if len(letter) < 2:

        used_letters.append(letter)
        found_indexes = find_indexes(word, letter)
        # print(found_indexes)

        if len(found_indexes) == 0:
            print('nie ma takiej litery, utrata zycia')
            no_of_tries -= 1

            if no_of_tries == 0:
                print('koniec gry')
                sys.exit(0)
        
        else:
            for index in found_indexes:
                user_word[index] = letter
            if "".join(user_word) == word:
                print()
                print('brawo wygrales')
                sys.exit(0)
    else:
        print('podaj jedna litere')

    show_game_status()

    # if "".join(user_word) == word:
    #     print('brawo wygrales')
    #     sys.exit(0)
