import random
from multiprocessing import Process
from multiprocessing import Event
from multiprocessing import Barrier
from multiprocessing import Lock
from multiprocessing import Queue

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
    
    def speed_up(self, stop_event, barrier, lock, queue):
        barrier.wait()
        while not stop_event.is_set():
            self.distance = self.distance + random.uniform(1,25)
            with lock:
                if self.distance >= 1000 and not stop_event.is_set():
                    stop_event.set()
                    queue.put(f'{self.name} wins')
                    break

# static method that adds a random distance to each distance attribute continually growing on itself


# main function that calls the 4 cattributes

def main(winner):
  
    print(winner)
    

if __name__ == "__main__":
    Juno = Cat("Juno")
    Henry = Cat("Henry")
    Rook = Cat("Rook")
    Phillip = Cat("Phillip")

    stop_event = Event()
    barrier = Barrier(4)
    lock = Lock()
    queue = Queue()

    
    
    
    p1 = Process(target=Juno.speed_up, args=[stop_event, barrier, lock, queue])
    p2 = Process(target=Henry.speed_up, args=[stop_event, barrier, lock, queue])
    p3  = Process(target=Rook.speed_up, args=[stop_event, barrier, lock, queue])
    p4 = Process(target=Phillip.speed_up, args=[stop_event, barrier, lock, queue])

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join() 
    p3.join()
    p4.join() 

    winner = queue.get()
    main(winner)