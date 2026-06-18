# Task 1: Create a Car Class
# Requirements:
# - Create a class named Car.
# - Add attributes: brand, color, model.
# - Create 2 objects.
# - Print the details of both cars.

class Car:
    brand = ""
    color = ""
    model = ""

# Creating first object
car1 = Car()
car1.brand = "Toyota"
car1.color = "Red"
car1.model = "Camry"

# Creating second object
car2 = Car()
car2.brand = "Ford"
car2.color = "Blue"
car2.model = "Mustang"

# Printing details of both cars
print("Car 1 Details:")
print("Brand:", car1.brand)
print("Color:", car1.color)
print("Model:", car1.model)
print()
print("Car 2 Details:")
print("Brand:", car2.brand)
print("Color:", car2.color)
print("Model:", car2.model)
