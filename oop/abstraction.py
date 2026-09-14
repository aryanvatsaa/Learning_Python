# ABSTRACTION : - HELPS IN HIDING THE COMPLEXITY OF A SYSTEM AND EXPOSING ONLY THE ESSENTIAL FEATURES OR BEHAVIORS TO THE USER. IT ALLOWS PROGRAMMERS TO FOCUS ON WHAT AN OBJECT DOES RATHER THAN HOW IT DOES IT. ABSTRACTION IS ACHIEVED THROUGH ABSTRACT CLASSES AND INTERFACES, WHICH DEFINE A CONTRACT FOR SUBCLASSES TO IMPLEMENT.

# ABSTRACTION EXAMPLE : -

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def start(self):
        print(f"{self.name} {self.model} is starting...")

    def stop(self):
        print(f"{self.name} {self.model} is stopping...")

print("Getting My Bike ...")
my_bike = Bike("Yamaha", "R15")
my_bike.start()
my_bike.stop()

