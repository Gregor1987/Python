class Person:
    def __init__(self, name, patronymic, family_name, age, height):
        self.name = name
        self.patronymic = patronymic
        self.family_name = family_name
        self.__age = age
        self.height = height

    def get_full_name(self):
        return f'{self.family_name} {self.name} {self.patronymic}'

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1
        return self.get_age()
