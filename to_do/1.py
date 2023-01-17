userchoice = -1
tasks = []


def add_task():
    tasks.append(input("podaj tresc zadania"))
    print('dodano')

def remove_task():
    if len(tasks) > 0:
            show_tasks()
            x = int(input("podaj numer zadania do usuniecia"))
            tasks.pop(x-1)
    else:
        print('brak zadan')

def show_tasks():
    if len(tasks) > 0:
        for i, task in enumerate(tasks):
            print('[' + str(i) + ']', task)
            # i+= 1
    else:
        print('brak zadan')

def load_from_file():
    try: 
        file = open('tasks.txt')
        
        for i, line in enumerate(file.readlines()):
            print('[' + str(i) + ']', line)
            
        file.close()

    except FileNotFoundError:
        return



def save_to_file():
    file = open('tasks.txt', 'w')
    for task in tasks:
        file.write(task + '\n')
    file.close()



while userchoice != 5:
    load_from_file()
    if userchoice == 1:
        add_task()
    if userchoice == 2:
        remove_task()
    if userchoice == 3:
        show_tasks()
    if userchoice == 4:
        save_to_file()

    # if len(tasks) > 0: show_tasks()
    print('---------------------------------')
    print('1 add task')
    print('2 remove task')
    print('3 show task')
    print('4 save to file')
    print('5 exit')
    print('---------------------------------')
    userchoice = int(input('choose number'))

