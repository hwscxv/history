import sys
import random
import string


password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left: 
        print('pozostalo ', characters_left, 'znakow. Sprobuj ponownie')
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print('pozostalo znakow:', characters_left)


#---------------------------------------------------------------------------
password_length = int(input('jak dlugie ma byc haslo'))

if password_length < 5:
    print('haslo musi miec minimum 5 znakow, sprobuj ponownie')
    sys.exit(0)
else: 
    characters_left = password_length




lower_case_letters = int(input('ile malych liter ma miec haslo '))
update_characters_left(lower_case_letters)



uppercase_letters = int(input('ile duzych liter ma miec haslo '))
update_characters_left(uppercase_letters)



special_characters = int(input('ile znakow specialnych ma miec haslo '))
update_characters_left(special_characters)



digits = int(input('ile cyfr ma miec haslo '))
update_characters_left(digits)


if characters_left > 0:
    print('nie wszystkie znaki zostaly wykorzystane. Haslo zostanie uzupelnione malymi literami')
    lower_case_letters += characters_left


print()
print('dlugosc hasla', password_length)
print('male litery:', lower_case_letters)
print('duze litery:', uppercase_letters)
print('specialne znaki:', special_characters)
print('cyfry', digits)

for i in range(password_length): #generowanie hasla - 
    if lower_case_letters > 0: #mala litera losowana z bibl. random 
        password.append(random.choice(string.ascii_lowercase)) # + litery z bibl. string
        lower_case_letters -= 1
                                 
    if uppercase_letters > 0: #mala litera losowana z bibl. random 
        password.append(random.choice(string.ascii_uppercase)) # + litery z bibl. string
        uppercase_letters -= 1
                                 
    if special_characters > 0: #mala litera losowana z bibl. random 
        password.append(random.choice(string.punctuation)) # + litery z bibl. string
        special_characters -= 1
                                 
    if digits > 0: #mala litera losowana z bibl. random         
        password.append(random.choice(string.digits)) # + litery z bibl. string
        digits -= 1
random.shuffle(password)
print('wygenerowane haslo:', "".join(password))