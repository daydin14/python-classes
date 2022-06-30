class Vehicle():
    """" Could be done like this too:
        def __init__(self, vin, make, model):
            self.vin = vin
            self.make = make
            self.model = model
            self.running = False
    """

    def __init__(self, vin, make, model, running=False):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = running
    
    def start(self):
        self.running = True
    
    def stop(self):
        self.running = False
    
    def __str__(self):
        return f'Vehicle VIN({self.vin}) is a {self.make} {self.model}'

myCar = Vehicle('14', 'Dodge', 'Hellcat')
print(myCar.vin, myCar.make, myCar.model)
print(myCar)

car = Vehicle('TS123', 'Tesla', 'Model S')
print(car.running) # -> False
car.start()
print(car.running) # -> True
plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.vin, plane.make, plane.model)