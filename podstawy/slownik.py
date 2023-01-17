cap = {'poland':'warsaw', "germany":'berlin'}
#        key   : value
cap['Czechia'] = 'prague' #dodawanie wartosci ['klucz] = 'wartosc

# print(cap)

for countries in cap.keys(): #klucze KEYS
    print(countries)

for capitals in cap.values():  #wartosci VALUES
    print(capitals)
print()
print()


for country, capital in cap.items(): #dwie zmienne dla key i value 
    print(country+ ' - ' + capital)  # ITEMS()
print()
print()

# print(cap['usa']) blad
print(cap.get('usa')) #wartosc none

print()
print()

print(cap.setdefault('usa', 'washington DC'))
print(cap)
print()
print()

# cap.pop('poland')  #usuwa klucz
# print(cap)
# print()
# print()

cap.popitem() #usuwa ostatnio dodany klucz
print(cap)


if "warsaw" in cap.values():
    print('znaleziono')
else:
    print('nie znaleziono')

print('warsaw' in cap.values())
