class Car(object):
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}, Year: {self.year}")
class ElectricCar(Car):
    def __init__(self, model, color, year, battery_size):
        super().__init__(model, color, year)
        self.battery_size = battery_size

    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size} kWh")
MyCar = Car("Toyota Camry", "Blue", 2020)
MyCar.display_info()
MyElectricCar = ElectricCar("Tesla Model 3", "Red", 2021, 75)
MyElectricCar.display_info()
MyLatestCar = Car("Tata-Punch", "Black", "2023")
MyLatestCar.display_info()
