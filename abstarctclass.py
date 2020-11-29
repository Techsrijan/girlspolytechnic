from abc import ABC,abstractmethod

# a class which contains atlest one abstract method is called
# abstract class
# we can not create the object of abstract class
class Car(ABC):   # this is helper class
    @abstractmethod
    def engine(self):
        pass

class Maruti(Car):
    def engine(self):
        print("has powerful engine")

'''c=Car()
c.engine()'''

m=Maruti()
m.engine()
