class Car:
    def __init__(self, make, model, speed, year):
        self.__make = make
        self.__model = model
        self.__speed = speed
        self.__year = year

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model         
    
    def get_speed(self):
        return self.__speed
    
    def get_year(self):
        return self.__year
    
    def accelerate(self):
        self.__speed += 10
    
    def brake(self):
        self.__speed -= 10
        
    def display_speed(self):
        print(f"The current speed of the car is {self.__speed} mph")

    def __str__(self):
        return f"Car(make={self.__make}, model={self.__model}, speed={self.__speed}, year={self.__year})"
    
    def __repr__(self):
        return f"Car(make={self.__make}, model={self.__model}, speed={self.__speed}, year={self.__year})"       

# Create a car instance
my_car = Car("Toyota", "Camry", 60, 2023)

# Display initial car details
print("Initial car details:")
print(my_car)
print()

# Demonstrate speed changes
print("Speed operations:")
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.accelerate()
my_car.display_speed()
my_car.brake()
my_car.display_speed()
print()

# Display final car details
print("Final car details:")
print(f"Make: {my_car.get_make()}")
print(f"Model: {my_car.get_model()}")
print(f"Year: {my_car.get_year()}")
print(f"Current Speed: {my_car.get_speed()}")
        
