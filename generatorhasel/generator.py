import string
import sys
import random
password = []
characters_left = -1

def update_characters_left(numer_of_characters):
    global characters_left
    if numer_of_characters < 0 or  numer_of_characters > characters_left:
        print('liczba znakow spoza przedzialu 0,', characters_left)
        sys.exit(0)
    else:
        characters_left -= numer_of_characters 
        print('pozostalo znakow:', characters_left)



password_length = int(input('jak dlugie ma byc haslo'))

if password_length < 5:
    print('haslo musi miec minimum 5 znakow sprobuj ponownie')
    sys.exit(0)
else:
    characters_left = password_length





lowercaseletters = int(input('ile malych liter ma miec haslo'))
update_characters_left(lowercaseletters)

uppercaseletters = int(input('ile duzych liter ma miec haslo'))
update_characters_left(uppercaseletters)

special_characters = int(input('ile znakow specialnych ma miec haslo'))
update_characters_left(special_characters)

digits = int(input('ile cyfr ma miec haslo'))
update_characters_left(digits)


if characters_left > 0:
    print('nie wszystkie znaki zostaly wykorzystane, haslo zostanie uzupelnione malymi literami')
    lowercaseletters += characters_left 
print()
print('dlugosc hasla:', password_length)
print('male litery:', lowercaseletters)
print('duze litery:', uppercaseletters)
print('znaki specialne:', special_characters)
print('cyfry:', digits)


for _ in range(password_length):
    if lowercaseletters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercaseletters -= 1
    if uppercaseletters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercaseletters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
 
random.shuffle(password)
print('wygnenerowane haslo:', "".join(password))
