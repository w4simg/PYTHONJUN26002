# Task 9: Create a Laptop Class
# Requirements:
# - Create a constructor.
# - Accept: brand, processor, RAM, price.
# - Create 3 laptop objects.
# - Display all laptop details.

class Laptop:
    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price

    def display(self):
        print(f"Brand: {self.brand} | Processor: {self.processor} | RAM: {self.ram} | Price: Rs.{self.price}")

# Create 3 laptop objects
laptop1 = Laptop("Dell", "Intel i5", "8GB", 55000)
laptop2 = Laptop("HP", "AMD Ryzen 5", "16GB", 62000)
laptop3 = Laptop("Lenovo", "Intel i7", "16GB", 78000)

# Display details
print("Laptop Specifications:")
laptop1.display()
laptop2.display()
laptop3.display()
