# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42

class City:

    def population(self):
        return 100500


class Person:
    def __init__(self):
        self.room = Room()
        self.city = City()

    def get_person_room(self):
        return self.room.get_name()

    def get_city_population(self):
        return self.city.population()


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

pp = Person()
print(pp.get_person_room())
print(pp.get_city_population())
