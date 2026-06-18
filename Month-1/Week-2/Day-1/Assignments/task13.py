# Task 13: Create a Product Class
# Requirements:
# - Store: product name, category, price.
# - Use a constructor.
# - Create 3 product objects.

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def display(self):
        print(f"Product: {self.name} | Category: {self.category} | Price: Rs.{self.price}")

# Create 3 product objects
prod1 = Product("Laptop", "Electronics", 60000)
prod2 = Product("Running Shoes", "Footwear", 3500)
prod3 = Product("Coffee Mug", "Kitchenware", 450)

# Display details
print("Product Catalogue:")
prod1.display()
prod2.display()
prod3.display()
