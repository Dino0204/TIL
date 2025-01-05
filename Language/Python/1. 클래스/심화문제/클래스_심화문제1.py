class Vehicle:
  def __init__ (self,brand,model,year):
    self.brand = brand
    self.model = model
    self.year = year
  def drive (self):
    return f"{self.brand} {self.model} is now driving."

class Car(Vehicle):
  def __init__(self,brand,model,year,fuel_type):
    super().__init__(brand,model,year)
    self.fuel_type = fuel_type
  def refuel(self):
    return f"{self.brand} {self.model} is refueling with {self.fuel_type}"

class ElectricCar(Vehicle):
  def __init__(self,brand,model,year, battery_capacity):
    super().__init__(brand,model,year)
    self.battery_capacity = battery_capacity
  def charge(self):
    return f"{self.brand} {self.model} is charging with {self.battery_capacity} k/w battery."

class Garage:
  def __init__(self,capacity):
    self.capacity = capacity
    self.cars = []
  
  def add_vehicle(self,car):
    if len(self.cars) == self.capacity:
      return "Garage is full, cannot add more vehicles."
    self.cars.append(car)
    return f"{car.brand} {car.model} has been added to the garage."
  
  def remove_vehicle(self,car):
    self.cars.remove(car)
    return f"{car.brand} {car.model} has been removed from the garage."
  
  def list_vehicles(self):
    return "\n".join([f"{car.brand} {car.model}" for car in self.cars])


car = Car("Toyota","Carmy",2020,"Gasoline")
electric_car = ElectricCar("Tesla","Model S",2021,100)
garage = Garage(2)

print(car.drive())
print(car.refuel())

print(electric_car.charge())

print(garage.add_vehicle(car))
print(garage.add_vehicle(electric_car))
print(garage.list_vehicles())

print(garage.remove_vehicle(car))
print(garage.list_vehicles())

print(garage.add_vehicle(electric_car))
print(garage.add_vehicle(car))