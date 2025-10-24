class Car:
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane:
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat:
    def move(self):
        print("⛵ The boat is sailing on the water.")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
