'''
there are 2 type of variable in a class
1. instance variable  -- variable declared inside method
2. class  variable -- varable declared inside class

'''

class Car:
    wheel=4 # wheel is class variable
    def config(self):
        self.comp="Maruti"  # comp and mil are instance variable
        self.mil=25
        print(self.comp,self.mil)


c1=Car()

c2=Car()

c1.config()
print(c1.comp)
c2.config()
c1.comp="Toyta"
print(c1.comp,c1.wheel)
c1.config()
print(c2.comp,c2.wheel)
print(Car.wheel)
Car.wheel=8
print(c1.wheel,c2.wheel)
c1.wheel=5
print(c1.wheel,c2.wheel)
print(c1.print_info())
