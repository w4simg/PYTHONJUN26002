# Task 7: Create a Building Class
# Requirements:
# - Take input from the user inside the constructor.
# - Accept: building name, location, number of floors.
# - Create a method to display building information.

class Building:
    def __init__(self):
        self.name = input("Enter building name: ")
        self.location = input("Enter location: ")
        self.floors = input("Enter number of floors: ")

    def display_info(self):
        print("\nBuilding Information:")
        print("Name:", self.name)
        print("Location:", self.location)
        print("Floors:", self.floors)

# Create object (will trigger input prompt)
my_building = Building()

# Display details
my_building.display_info()
