user_choice = -1
tasks = []
def show_tasks():
    task_index = 0
    for task in tasks:
        print('[' + str(task_index) + '] ' + task)
        task_index += 1
def add_task():
    tasks.append(input('Podaj zadanie '))
    print('dodano')
def remove_task():
    task_index = 0
    print()
    for task in tasks:
        print('[' + str(task_index) + '] ' + task)
        task_index += 1
    tasks.pop(int(input("podaj index zadania do usuniecia ")))
    print('usunieto')
    print()
def save_to_file():
    file = open('zadania.txt', "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()
    print('zapisano!')
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
            show_tasks()
        if user_choice == 2:
            add_task()
        if user_choice == 3:
            remove_task()
        if user_choice == 4:
            save_to_file()
        # if user_choice == 1:
        #     print(tasks)

        print()
        print('1. Pokaz zadania')
        print('2. Dodaj zadanie')
        print('3. Usun zadanie')
        print('4. Zapisz zmiany do pliku')
        print('5. Wyjdz')
        print()

        user_choice = int(input("wybierz liczbe "))