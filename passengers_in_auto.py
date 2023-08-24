#Оголосимо створення двох класів – авто й людини:
class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

#додаємо метод додавання пасажирів
    def add_passengers(self, human):
        self.passengers.append(human)

#Додаємо метод, що виводить список пасажирів

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

#Створюємо об’єкти двох людей та авто, після чого викличемо методи
# реєстрації пасажирів та виведення їхніх імен
nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")

car.add_passengers(nick)
car.add_passengers(kate)
car.print_passengers_names()