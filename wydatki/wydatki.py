expenses= [] 
expense_amount = 0 
month_number = {}
month_number[1] = ('styczen', 30)
month_number[2] = ('luty', 30)
month_number[3] = ('marzec', 30)
month_number[4] = ('kwiecien', 30)
month_number[5] = ('maj', 30)
month_number[6] = ('czerwiec', 30)
month_number[7] = ('lipiec', 30)
month_number[8] = ('sierpien', 30)
month_number[9] = ('wrzesien', 30)
month_number[10] = ('pazdziernik', 30)
month_number[11] = ('listopad', 30)
month_number[12] = ('grudzien', 30)


def add_expense(month):
    print()
    expense_amount = int(input('podaj kwote [zl] '))
    expense_type = input('podaj typ wydatku (jedzenie, rozrywka, dom, inny) ')

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)
def show_expenses(month):
       for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')    
def show_stats(month):
    global month_number
    total_amonth_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)

    total_amonth_all = sum(expense_amount for expense_amount, _, _ in expenses)
    # average_expense_all = total_amonth_all / number_of_expenses_all

    if number_of_expenses_this_month == 0:
        average_expense_this_month = 0
    else:
        average_expense_this_month = total_amonth_this_month / number_of_expenses_this_month

    print()
    print('statystyki')
    print('wszystkie wydatki w tym miesiacu', total_amonth_this_month)
    print('sredni wydatek w tym miesiacu', average_expense_this_month)
    # print('sredni wydatek: ', average_expense_all)s
    print('wszystkie wydatki:', total_amonth_all)

while True:
    print()
    month = int(input('wybierz miesiac [1-12]: '))
    month_info = month_number.get(month)
    
    if month > 12:
        print('niepoprawna wartosc miesiaca, sprobuj ponownie')
    else:
        while True:
            print()
            print('miesiac:', month_info[0])
            print("0. Powrot")
            print("1. wyswietl wszystkie wydatki")
            print("2. Dodaj wydatek")
            print("3. statystyki")
            
            
            choice = int(input('wybierz opcje: '))
            if choice > 3:
                print('niepoprawna wartosc, sprobuj ponownie')
            else:
                if choice == 0: 
                    break
                if choice == 1:
                    show_expenses(month)
                if choice == 2:
                    add_expense(month)
                if choice == 3:
                    show_stats(month)
