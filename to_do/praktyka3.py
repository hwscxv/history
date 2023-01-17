tasks = []
user_choice = -1


def showtasks():
    nr_zad = 0
    for task in tasks:
        print('[' + str(nr_zad) + '] ' + task)
        nr_zad += 1
def addtasks():
    tasks.append(input('podaj tresc zadania '))
def removetask():
    print()
    showtasks()
    tasks.pop(int(input('podaj indeks zadania do usuniecia ')))
def savetofile():
    file = open('tasks.txt', 'w')
    for task in tasks:
        file.write(task + "\n")
    file.close
def readfromfile():
    file = open("tasks.txt")

    for line in file.readlines():
        tasks.append(line.strip())

    file.close



readfromfile()
while user_choice != 5:  
    print('')
    print('________________________________')
    print('1. wyswietl zadania')
    print('2. dodaj zadanie')
    print('3. usun zadanie')
    print('4. zapisz zmiany do pliku')
    print('5. Exit')
    print('________________________________')

    user_choice = int(input('podaj numer '))
    if user_choice == 1:
        showtasks()
    if user_choice == 2:
        addtasks()
    if user_choice == 3:
        removetask()
    if user_choice == 4:
        savetofile()
    # if user_choice == 1:
    #     showtasks()
