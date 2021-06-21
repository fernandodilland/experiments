# Experiment programmed for practice by: Fernando Dilland Mireles Cisneros

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

Car1 = Car("Nissan", "Tiida", 2007)
Car

print(Car1.brand)
print(Car1.model)
print(Car1.year)
# dictionary
dictionary = {}
dictionary["Brand"]=Car1.brand

print(dictionary)