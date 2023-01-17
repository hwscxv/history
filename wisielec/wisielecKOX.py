import sys 

word = 'sowa'
used_letters = []
user_word = []
no_of_tries = 5


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter_in_word == letter:
            indexes.append(index)
    return indexes

def show_stats():
    print()
    print('uzyte litery:', ", ".join(used_letters))
    print('haslo:', user_word)
    print('pozostalo zyc:', no_of_tries)
    print()


for _ in word:
    user_word.append('_')



while True:
    print()
    letter = input('podaj litere ')
    print()


    if len(letter) < 2:
        used_letters.append(letter)
        found_indexes = find_indexes(word, letter)
        # print('uzyte litery:', used_letters)

        if len(found_indexes) == 0:
            no_of_tries -= 1
            # print('utrata zycia, pozostalo:', no_of_tries)
            # print(user_word)

            if no_of_tries == 0:
                print('koniec zyc, przegrana')
                sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter
            # print(user_word)

            if "".join(user_word) == word:
                print()
                print('brawo wygrales, slowo klucz to:', word)
                sys.exit(0)
        show_stats()
        


            




