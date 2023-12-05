class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.running = False
    
    def start(self):
        self.running = True
        print(f"The {self.year} {self.brand} {self.model} started.")
    
    def stop(self):
        self.running = False
        print(f"The {self.year} {self.brand} {self.model} stopped.")

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model S", 2022)

# Using methods of the Car class
car1.start()
car2.start()
car1.stop()
