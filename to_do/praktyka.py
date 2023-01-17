user_choice = -1 

tasks = []
done_tasks = []

def show_tasks():
   for i, task in enumerate(tasks):
    print('[' + str(i) + ']', task)
def add_task():
    task = input('wpisz tresc zadania ')
    tasks.append(task)
    print("dodano zadanie! " + task)
def delete_task():
    show_tasks()
    x = int(input("podaj numer zadania do usuniecia"))
    tasks.pop(x-1)
    print('usunieto zadanie!')
def save_tasks_to_file():
    file = open('tasks.txt', "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()
    print('zapisano!')
def load_tasks_from_file():
    try:
        file = open('tasks.txt')

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return
def task_done():
    show_tasks()
    task_index = int(input('podaj indeks wykonanego zadania '))

    if task_index < 0 or task_index > len(tasks) - 1:
        print('bledny indeks zadania')
        return 
    removed_task = tasks.pop(task_index)

    file = open('done_tasks.txt', "w")
    file.write(removed_task+"\n")
    file.close()
def load_done_tasks():
    try:
        file = open('done_tasks.txt')

        for i, line in enumerate(file.readlines()):
            print('[' + str(i) + ']', line)
            
        file.close()
        
    except FileNotFoundError:
        return
def remove_done_tasks():
    done_tasks.clear()
    print('wykonane zadania zostaly wyczyszczone')
    
load_tasks_from_file()

while user_choice != 8:
    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        task_done()
    if user_choice == 3:
        add_task()
    if user_choice == 4:
        delete_task()
    if user_choice == 5:
        save_tasks_to_file()
    if user_choice == 6:
        load_done_tasks()
    if user_choice == 7:
        remove_done_tasks()

    print()
    print("1. pokaz zadania")
    print("2. zadanie wykonane")
    print("3. dodaj zadanie")
    print("4. usun zadanie")
    print("5. zapisz zmiany do pliku")
    print("6. pokaz wykonane zadania")
    print("7. wyczysc wykonane zadania")
    print("8. wyjdz")
    print()

    user_choice = int(input("wybierz liczbe "))
    print()