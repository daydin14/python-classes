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

class ShowDog(Dog):
    def __init__(self, name, age = 0, total_earnings = 0):
        Dog.__init__(self,name,age)
        self.total_earnings = total_earnings
    
    def add_prize_money(self, amount):
        self.total_earnings += amount

winky = ShowDog('Winky', 3, 1000)
print(winky) # Yay, inherited the overriden __str__
winky.bark() # Yay, inherited the bark method
print(winky.total_earnings) # -> 1000
winky.add_prize_money(500) # New method that 'Dogs' don't have
print(winky.total_earnings) # -> 1500