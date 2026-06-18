# Task 8: Create a Citizen Class
# Requirements:
# - Create a class variable called country = "India".
# - Use a constructor to accept: Aadhaar Number, Phone Number, Name.
# - Create a method to print all details.

class Citizen:
    # Class variable
    country = "India"

    def __init__(self, aadhaar, phone, name):
        self.aadhaar = aadhaar
        self.phone = phone
        self.name = name

    def display_details(self):
        print("Citizen Details:")
        print("Name:", self.name)
        print("Aadhaar Number:", self.aadhaar)
        print("Phone Number:", self.phone)
        print("Country:", self.country)

# Create object
citizen = Citizen("1234-5678-9012", "9876543210", "Amit Patel")

# Print details
citizen.display_details()
