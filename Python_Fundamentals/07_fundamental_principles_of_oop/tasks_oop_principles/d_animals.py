from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, type, name, age, gender):
        self.type = type
        self.name = name
        self.age = int(age)
        self.gender = gender

    @abstractmethod
    def produce_sound(self):
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception('Invalid input!')
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if self.type == 'Tomcat':
            self.__gender = 'Male'
        elif self.type == 'Kitten':
            self.__gender = 'Female'
        else:
            self.__gender = gender


class Dog(Animal):
    def __init__(self, type, name, age, gender):
        Animal.__init__(self, type, name, age, gender)

    def produce_sound(self):
        return 'Woof!'

    def __str__(self):
        return f'Dog\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}'


class Cat(Animal):
    def __init__(self, type, name, age, gender):
        Animal.__init__(self, type, name, age, gender)

    def produce_sound(self):
        if self.type!='Cat':
            if self.gender == "Male":
                return 'MEOW'
            else:
                return 'Meow'
        else:
            return 'Meow meow'

    def __str__(self):
        return f'{self.type}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}'


class Frog(Animal):
    def __init__(self, type, name, age, gender):
        Animal.__init__(self, type, name, age, gender)

    def produce_sound(self):
        return 'Ribbit'

    def __str__(self):
        return f'Frog\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}'


animals = ''

while True:

    first_line = input()
    if first_line == 'Beast!':
        break

    name, age, gender = input().split()
    try:
        if first_line == 'Dog':
            animals = Dog(first_line, name, age, gender)
        elif first_line == 'Cat' or first_line == 'Tomcat' or first_line == 'Kitten':
            animals = Cat(first_line, name, age, gender)
        elif first_line == 'Frog':
            animals = Frog(first_line, name, age, gender)
        else:
            print('Invalid input!')
            continue

        print(animals)
    except Exception as exe:
        print(exe)
