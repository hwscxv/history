class Person():

    def __init__(self,name) -> None:
        self.name= name
        self.surname = 'kwiatkowski'
        self.age = 25

class Employee(Person):

    def __init__(self,name,position) -> None:
        super().__init__(name)
        self.position= position
        self.specialization = 'python'


class Client(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.ordered = 'websites'

pracownik = Employee('kamil','programist')
print(pracownik.name)
print(pracownik.position)

pracownik2 = Employee('piotr','designer')
print(pracownik2.name)
print(pracownik2.position)

klient = Client('marta')
print(klient.name)
print(klient.ordered)

klient2 = Client('kamila')
print(klient2.name)
print(klient2.ordered)