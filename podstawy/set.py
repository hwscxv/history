#bez zduplikowanych wartosci
#nieuporzadkowana
# niemutowalne (?)

names_set1= {'kamil1', 'mariusz1'}
names_set2 = set()
names_set2.add('kamil') #dodawanie
names_set2.add('mariusz')
names_set2.add('adam')

print(names_set1)
print(names_set2)

names_set2.remove('kamil')#usuwanie z setu
names_set2.discard('adam')#rozncia = jak nie ma danych nie wywala bledu

names_set2.add('a')
names_set2.add('b')

names_list = []
names_touple = ()
# names_set.add(names_list)
names_set2.add(names_touple)
print()
#-----------------------------------------------------------------------

names_set3= {'dominik', 'pawel'}
names_set4 = set()
names_set4.add('kamil') #dodawanie
names_set4.add('mariusz')

names_set5 = names_set3.union(names_set4)# Dodawanie dwoch setow(unia) + iteracja po nowym
for names in names_set5:
    print(names)
print()
print()
print()

#-----------------------------------------------------------------------
names_set6 = {"monika", 'jan'}
names_set7 = {"ola", 'pawel'}

names_set6.update(names_set7) #update dodaje + zmienia glowny set
print(names_set6)
print('')

#-------------------

names_set8 =  {"mikolaj",'piotr', "andrzej", "ola"}
names_set9= {"ola", 'jan'}

names_set10= names_set8.difference(names_set9) #difference = od setu8 odejmuje set 9
for name in names_set10:                       # zwraca do nowej stalej set10
    print(name)

print('---------------------------------------------------')

#_-------------------------------------------------------------------------

names_set11 = names_set8.intersection(names_set9) #interssection - czesci wsplone dla setow
print(names_set11)

names_set12 = names_set8.symmetric_difference(names_set9) #czesci setu  niewspolne
print(len(names_set12))
print((names_set12))

#-----------------------------------------------------------

names_list1 = ['artur', 'rafal']

names_list1.extend(names_set12) #lista +  set
print(names_list1)