
class Car:

    #class variable , doesn belong to individual object
    amount_cars = 0

    def __init__(self, maker, model, hp):
        self.maker = maker
        self.model = model
        self.hp    = hp
        Car.amount_cars += 1


    def print_info(self):
        print(f"manufecture: {self.maker} & model: {self.model}")


    def print_hp(self):
        print(self.hp)


    def print_car_amount(self):
        print(f"total of cars so far {Car.amount_cars}")

    def has_trailer(self):
        print("no trailer")


    #def __del__(self):
      #  print("objects it is o be deleted")
       ## Car.amount_cars -= 1


Car1 = Car("Ferrari","Enzo", 400)
Car2 = Car("BMW","M5 Cs", 730)
Car3 = Car("Mercedez", "AMG GT", 560)

Car3.print_info()
Car2.print_car_amount()
print(Car2.model)


class Truck(Car):
    truck_total = 0

    def __init__(self, maker,model, hp, speed):
        super(Truck, self).__init__(maker, model, hp)
        self.speed = speed
        Truck.truck_total += 1

    def print_num_trucks(self):
        print(f"total number of trucks so far : {self.truck_total}")

    # method over-writting
    def has_trailer(self):
        print("Yes , it has a trailer")

    def print_all(self):
        print(f"Maker : {self.maker} , hp : {self.hp} ,speed : {self.speed}")


myTruck = Truck("Reanult","EX344" ,3000, 130)
myTruck2 = Truck("Benz","W88" , 4444, 200)
myTruck3 = Truck("Reanult B", "electric", 600, 180)
myTruck4 = Truck("Benz Y","zoro", 3324, 120)

print("-------------------------------------------")
myTruck.print_all()
print(Truck.truck_total)
print(myTruck4.maker)
myTruck.print_num_trucks()
