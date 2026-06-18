#make an object class

# class car:
#     cat =  "suv"
#     color = "red"
#     wheel = 4

# car1 = car()
# car2 = car()
# car3 = car()
# car4 = car()

# print(car1.cat)
# print(car1.color)

#methods

# class student():
#     name = "rahul"
#     age = 24
#     def studentDetails(self):
#         print("student name is", self.name , "age is ", self.age)

#     def viewInput(self, address, roll):
#         print("this is address",address,"this is the role",roll)


# s1=student()
# s1.studentDetails()
# s1.viewInput("bbsr",23)

# print(s1.age)

#constructor

# class citizen:
#     def __init__(self, adhar,phone,name, country="India"):
#         self.aadhar = adhar
#         self.phone = phone
#         self.name = name
#         self.country = country
        
#     def printcitizen(self):
#         print("aadhar is",self.aadhar,"phone is ",self.phone,"name is ",self.name, "country is",self.country)
        


# c1 = citizen("345678905679","8967564567", "wasimc" )
# c2 = citizen("345678905678","8967564566", "wasimc2" )
# c3 = citizen("345678905677","8967564565", "wasimc3" )


# # c1.printcitizen()
# # c2.printcitizen()
# c3.printcitizen()


class Building:
    country = "India"

    def __init__(self):
        self.location = input("enter the location:")
        self.floors = input("enter the number of floors:")
        self.pin = input("enter the pin code:")
        self.roomsInFloor = input("enter the rooms in each floor:")
        

    def printBuilding(self):
        print("location is", self.location)
        print("floors is", self.floors)
        print("pin is", self.pin)
        print("rooms in floor is", self.roomsInFloor)


building1 = Building()
building1.printBuilding()

