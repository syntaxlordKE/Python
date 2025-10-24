# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.__storage = storage        # private attribute (encapsulation)
        self.__battery = battery

    # Getter method (encapsulation)
    def get_storage(self):
        return self.__storage

    # Setter method (encapsulation)
    def upgrade_storage(self, new_storage):
        if new_storage > self.__storage:
            self.__storage = new_storage
            print(f"Storage upgraded to {self.__storage}GB ✅")
        else:
            print("Upgrade failed: New storage must be larger!")

    def charge(self):
        print(f"{self.device_info()} is charging 🔋")

    def specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.__storage}GB, Battery: {self.__battery}mAh"


# Example Usage
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 5000)
print(phone1.specs())
phone1.charge()
phone1.upgrade_storage(256)
print(phone1.get_storage())
