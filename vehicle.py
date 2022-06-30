class Vehicle():
    vehicle_id = 1
    
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
        self.id = Vehicle.vehicle_id
        Vehicle.vehicle_id += 1
    
    def start(self):
        self.running = True
    
    def stop(self):
        self.running = False
    
    def __str__(self):
        return f'Vehicle VIN({self.vin}) is a {self.make} {self.model}'
    
    @classmethod
    def get_total_vehicles(cls):
        return f'There are currently {cls.vehicle_id-1} vehicle objects'

myCar = Vehicle('14', 'Dodge', 'Hellcat')
print(myCar.vin, myCar.make, myCar.model)
print(myCar)
print('') # Spacing

# Running...?
myCar.start()
print(myCar.__dict__)
myCar.stop()
print(myCar.__dict__)

print('') # Spacing

car = Vehicle('TS123', 'Tesla', 'Model S')
print(car.__dict__)

plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.__dict__)

super_bike = Vehicle('xyz-456', 'BMW', 's1000rr')
print(super_bike.__dict__)

print('\n' + Vehicle.get_total_vehicles() + '\n')