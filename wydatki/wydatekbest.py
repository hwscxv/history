expenses = []

mnth = {1:'styczen', 2:'luty', 3:'marzec', 4:'kwiecien', 5:'maj', 6:'czerwiec', 7:'lipiec', 8:'sierpien', 9:'wrzesien', 10:'pazdziernik', 11:'listipad', 12:'grudzien'}
expense_type = ['dom', 'rozrywka', 'jedzenie', 'inny']


def show_expenses(month):
    if len(expenses) == 0:
        print('brak wydatkow do wyswietlenia')
    else:
        for expense_amount, expense_type, expense_month in expenses:
            if expense_month == month:
                print(f'{expense_amount} - {expense_type}')

def add_expense(month):
    
    print()
    expense_amount = int(input('podaj kwote wydatku '))#kwota wydatku
    for index, i in enumerate(expense_type):
        print(index, i)
        index += 1
    exp_type_user = int(input('wybierz typ wydatku '))

    
    
    expense = (expense_amount, expense_type[exp_type_user], month) #krotka wydatek + typ + msc 
    expenses.append(expense) #krotka wydatek do listy wydatkow

def show_stats(month):
    total_amount_this_month= sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)    
    total_amount_all = sum(expense_amount for expense_amount, _, _, in expenses)
    number_of_expenses_this_month= sum(1 for _, _, expense_month in expenses if expense_month == month)

    if number_of_expenses_this_month > 0:
        average_expense_this_month = total_amount_this_month / number_of_expenses_this_month
    else:
        average_expense_this_month = 0

    if len(expenses) > 0:
        average_expense_all = total_amount_all / len(expenses)
    else:
        average_expense_all = 0
    




    
    print()
    print('statystyki')
    print('wszystkie wydatki w tym miesiacu:', total_amount_this_month)
    print('wszystkie wydatki:', total_amount_all)
    print('sredni wydatek w tym miesiacu:', average_expense_this_month)
    print('sredni wydatek:', average_expense_all)
    
def add_expese_type():
    expense_type.append(input('podaj nowy typ wydatku'))



  
while True:
    try:
        month = int(input('wybierz miesiac [1-12]'))
        print('miesiac:', mnth[month])

        if month > 12 or month < 1:
            print('wpisz poprawna cyfre')
            continue

        if month == 0:
            break

    except ValueError:
            print('podaj cyfre')
            continue
    
    while True:
        print()
        print('0. powrot do wyboru miesiaca')
        print('1. wyswietl wszystkie wydatki')
        print('2. dodaj wydatek')
        print('3. nowy typ wydatku')
        print('4. statystyki wydatkow')
        try:
            choice = int(input('wybierz opcje'))

            if choice == 0:
                break
            if choice == 1:
                show_expenses(month)
            if choice == 2:
                add_expense(month)
            if choice == 3:
                add_expese_type()
            if choice == 4:
                show_stats(month)
            if choice > 4 or month < 0:
                print('wpisz poprawna cyfre')
                continue

        except ValueError:
            print('podaj cyfre')
            continue
    