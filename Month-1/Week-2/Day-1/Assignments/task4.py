# Task 4: Create a Mobile Class
# Requirements:
# - Use a constructor.
# - Accept: brand, RAM, storage, price.
# - Create a method to display mobile information.

class Mobile:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display_info(self):
        print("Mobile Specification:")
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)

# Create object
my_mobile = Mobile("Samsung", "8GB", "128GB", 45000)

# Display information
my_mobile.display_info()
