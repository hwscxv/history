import sys
import random
import string  


password = []
characters_left = -1

def update_characters_left(no_of_characters):
    global characters_left
    if no_of_characters < 0 or no_of_characters > characters_left:
        print('podaj liczbe od 0 do', characters_left)
        sys.exit(0)
    else:
        characters_left -= no_of_characters
        print('pozostalo znakow:', characters_left)

password_length = int(input('podaj dlugosc hasla'))

if password_length < 5:
    print('minimalna dlugosc hasla to 5 znakow')
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = int(input('podaj liczbe malych liter '))
update_characters_left(lowercase_letters)

uppercase_letters = int(input('podaj duzych malych liter '))
update_characters_left(uppercase_letters)

special_characters = int(input('podaj liczbe znakow specialnych '))
update_characters_left(special_characters)

digits = int(input('podaj liczbe cyfr '))
update_characters_left(digits)

if characters_left > 0:
    lowercase_letters += characters_left
    print('nie wykorzystano wszystkich znakow, pozostale znaki uzupelniono malymi literami')

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print('wygnererowane haslo to ',"".join(password))




