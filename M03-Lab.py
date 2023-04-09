class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type,year,make,model,doors,roof):
        Vehicle.__init__(self,vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return "Vehicle type is: " + self.vehicle_type + "\nYear: " + self.year +" \nMake: " + self.make +"\nModel: " + self.model + "\nNumber of doors: " + self.doors + "\nType of roof: " + self.roof
    
if __name__ == "__main__":
    year = input("Enter Year: ")
    make = input("Enter Make: ")
    model = input("Enter Model: ")
    doors = input("Enter Doors: ")
    roof = input("Enter Roof: ")
    
    carObj = Automobile("car", year,make,model,doors,roof)

    print(carObj)