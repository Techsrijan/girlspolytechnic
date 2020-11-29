'''
Deriving a new class from the base class in knwon as inheritance

type of inheritnce
1. single level inheritance
2. multilevel inheritance
3. heirarchical inheritance
4. multiple inheritance
5. hybrid inheritance

it privides the concept of code reuseability.



'''
class Room:     # base class or parent class
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

class GuestRoom(Room):  # derived class or child class
    def msg(self):
        print("Guest Room")


class Home(GuestRoom):
    def msg2(self):
        print("home message")

#a=Room()
#a.area(20,10)
'''b=GuestRoom()
b.msg()
b.area(5,5)'''

c=Home()
c.msg()
c.msg2()
c.area(55,99)