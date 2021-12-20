# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width
    


# Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def test(self):
        print(self.max_speed, self.mileage)
        


# Create a Vehicle class without any variables and methods.
class Vehicle:
    pass



# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass