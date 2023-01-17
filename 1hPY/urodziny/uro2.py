import datetime
import calendar


def translate_pl(day_name):
    match day_name:
        case 'Monday':
            return 'poniedzialek'
        case 'Tuesday':
            return 'wtorek'
        case 'Wednesday':
            return 'sroda'
        case 'Thursday':
            return 'czwartek'
        case 'Friday':
            return 'piatek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'

date_of_birth =  input('podaj date urodzin dzien-miesiac-rok')
day, month, year = date_of_birth.split('-')


date_of_birth = datetime.datetime(int(year), int(month), int(day))


day_name = calendar.day_name[date_of_birth.weekday()]
print(translate_pl(day_name))


