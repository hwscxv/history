import sys

no_of_tries = 5
word = 'kamil'
user_word = []   #aktualny stan gry dla uzytwkonika
used_letters = []

def find_indexes(word, letter): #funkcja podajaca index w wyrazie
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
#------------------------------------------------------------

for _ in word:         #dla kazdej litery w slowie dodaj _
    user_word.append('_')

while True:
    letter = input('podaj litere: ') #podaj litere

    if len(letter) < 2:
        used_letters.append(letter)      #zapisz podana litere do listy
        found_indexes = find_indexes(word, letter)
        
        if len(found_indexes) == 0:
            print('nie ma takiej litery')
            no_of_tries -= 1
            print('pozostalo prob:', no_of_tries)

            if no_of_tries == 0:
                print('przepierdoliles mistrzu')
                sys.exit(0)
        
        else:
            for index in found_indexes:
                user_word[index] = letter
            print(user_word) 
            if "".join(user_word)== word:
                print('brawo wygrana')
                sys.exit(0)
        print('uzyte litery:', used_letters)
    else:
        print('podaj jedna litere')

