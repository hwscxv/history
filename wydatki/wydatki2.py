expenses = []
expense_amount = 0

def add_expense(month):
    expense_amount = int(input('podaj kwote wydatku: '))
    expense_type = input('podaj typ wydatku (jedzenie, dom, rozrywka, inny) ')
    expense = (expense_amount, expense_type, month)
    expenses.append(expense)
def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')
def show_stats(month):
    total_monthly = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)

while True:
    month = int(input('podaj miesiac (0 - 12) '))
    if month > 12:
        print('podano niewlasciwa wartosc, sprobuj ponownie')
    else:
        while True:
            print('0. Powrot')
            print('1. Dodaj wydatek')
            print('2. Wszystkie wydaki w tym miesiacu')
            print('3. Statystyki')
            choice = int(input('Wybierz opcje: '))

            if choice > 3:
                print('podano niewlasciwa wartosc, sprobuj ponownie')
            else:
                if choice == 0:
                    break
                if choice == 1:
                    add_expense(month)
                if choice == 2:
                    show_expenses(month)