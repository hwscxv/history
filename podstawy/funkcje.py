c_inf = {}
c_inf['polska'] = ('warszawa', 12)
c_inf['niemcy'] = ('berlin', 32)
c_inf['rosja'] = ('moskwa', 122)

def show_country_info(country):
    country_info = c_inf.get(country)
    print()
    print(country)
    print('-------------')
    print("stolica: " + country_info[0])
    print('liczba mieszkancow: ' + str(country_info[1]))

for country in c_inf.keys():
    print(country)

country = input('podaj kraj ')  

show_country_info(country)
