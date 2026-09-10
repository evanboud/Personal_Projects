import random

# overall Cat class that takes a name and distance attribute 
class Cat:
    def __init__(self, name, distance=0):
        self.distance = distance
        self.name = name

    def __str__(self): 
        ...
    @property
    def distance(self):
        return self._distance 
    @distance.setter
    def distance(self, distance):
        if distance < 0:
            raise ValueError
        self._distance = distance
    
    



# static method that adds a random distance to each distance attribute continually growing on itself


# main function that calls the 4 cattributes
Juno = Cat("Juno")
Henry = Cat("Henry")
Rook = Cat("Rook")
Phillip = Cat("Phillip")
cats = [Juno, Henry, Phillip, Rook]
def main():
   winner = race()
   print(winner)
def race():
    while True:
        for cat in cats:
            cat.distance = cat.distance + random.uniform(1, 25)
            if cat.distance > 1000:
                return cat.name

#animation 
pygame.display.set_mode()



    

if __name__ == "__main__":
    main()
    
