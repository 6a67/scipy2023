# the class Animal
class Animal:
    def is_living(self):
        return True

# The class LandAnimal inherits the functions from Animal.    
class LandAnimal(Animal):
    def __init__(self):
        self.has_legs = True
        
    def walk(self):
        return "tap tap"

# create the class SeaAnimal according to LandAnimal
class SeaAnimal(LandAnimal):
    def __init__(self):
        self.has_legs = False
        self.has_flippers = True
    
    def swim(self):
        return "shuh shuh"

# to test if your class is working
if __name__ == "__main__":
    animal = SeaAnimal()
    animal.is_living()
    animal.has_flippers
    animal.swim()