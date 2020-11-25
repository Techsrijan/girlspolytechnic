class A:
    def msg(self):
        print("this is class a msg")

class B(A):
    def msg2(self):
        print("this is class B msg")

x=B()
x.msg2()
x.msg()
