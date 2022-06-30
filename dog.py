class Dog():
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{self.name} says woof!')
    
    def __str__(self):
        return f'Dog named {self.name} is {self.age} years old'

spot = Dog('Spot', 8)
print(spot)
print(spot.name, spot.age)
spot.bark()

dog = Dog('Lassie')
print(dog.name, dog.age)