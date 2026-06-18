# Task 12: Create a Hospital Class
# Requirements:
# - Use a constructor.
# - Accept: hospital name, doctor count, city.
# - Create a display method.

class Hospital:
    def __init__(self, hospital_name, doctor_count, city):
        self.hospital_name = hospital_name
        self.doctor_count = doctor_count
        self.city = city

    def display(self):
        print("Hospital Information:")
        print("Hospital Name:", self.hospital_name)
        print("Doctor Count:", self.doctor_count)
        print("City:", self.city)

# Create object
hospital1 = Hospital("Apollo Hospital", 150, "Bhubaneswar")

# Display info
hospital1.display()
