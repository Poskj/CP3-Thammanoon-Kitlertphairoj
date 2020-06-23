class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estate(Vehicle):
    pass

car = Car()
car.turnOnAirConditioner()
pickUp = PickUp()
pickUp.turnOnAirConditioner()
van = Van()
van.turnOnAirConditioner()
estate = Estate()
estate.turnOnAirConditioner()
