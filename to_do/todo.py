import sys
user_choice = -1
tasks = []

def show_tasks():
    task_index = 0
    if len(tasks) > 0:
        for task in tasks:
            print('[' + str(task_index) + '] ' + task)
            task_index += 1
def add_tasks():
    tasks.append(input('podaj tresc zadania: '))
def remove_task():
    task_index = 0
    if len(tasks) > 0:
        for task in tasks:
            print('[' + str(task_index) + '] ' + task)
            task_index += 1
    tasks.pop(int(input('podaj index do usuniecia')))
def save_to_file():
    file = open("zadania.txt", 'w')
    for task in tasks:
        file.write(task+'\n')
    file.close()
    print('zapisano')
def load_tasks_from_file():
    try:
        file = open('zadania.txt')
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return


load_tasks_from_file()
while user_choice != 5:
    if user_choice == 1:
        print(show_tasks())
    if user_choice == 2:
        print(add_tasks())
    if user_choice == 3:
        print(remove_task())
    if user_choice == 4:
        print(save_to_file())
    if user_choice == 5:
        sys.exit(0)

    print('1  pokaz zadania')
    print('2  dodaj zadanie')
    print('3  usun  zadanie')
    print('4  zapisz do pliku')
    print('5  wyjscie')

    user_choice = int(input("podaj numer "))





