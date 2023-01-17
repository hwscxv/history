from random import randint

los = randint(1,10)
answer = -1
no_of_tries = 0

print('minigra podaj liczbe z przedzialu 1-10')
 
while answer != los:
    no_of_tries += 1
    answer = int(input('podaj liczbe: '))

    if answer > los:
        print('wylosowana liczba jest mnijesza od podanej')
    elif answer < los:
        print('wylosowana liczba jest wieksza od podanej')
print('brawo wygrales, liczba prob', f'{no_of_tries}')
    