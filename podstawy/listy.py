#mozna modyfikowac
#ten sam typ
names_list = []
names_list.append('kamil')
names_list.append('mariusz')
names_list.reverse() #odwrot listy

names_list2 = ['kamil', 'mariusz', 'adam', 'kamil']
names_list2.sort() #sort listy

print(names_list,'names list')
print()
print(names_list2, 'names list2')
print()

for name in names_list2: #iteracja listy
    print(name, '       names list 2')

print()
print()


print(names_list2[2]) #wybor z listy
print(names_list2.count('adam')) #ile w liscie
print(len(names_list)) #dlugosc listy
print()
print(names_list2.pop(3)) #usuwa z listy i zwraca
print()
names_list2.remove('kamil') #usuwa pozcyje z listy
print(names_list2, 'names list2')

names_list2.clear() #zeruje liste



# names_list1.extend(names_set12) #lista +  set
# print(names_list1)