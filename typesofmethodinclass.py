'''
there are 3 types of method
1. instance method-self
2. class method -- cls
3. static method -- no argument  -neither cls nor self

'''


class student:
    school="techsrijan"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return((self.m1+self.m2+self.m3)/3)

    @classmethod
    def school_name(cls):
        print(student.school)

    @staticmethod
    def info():
        print("This is static method")


s1=student(10,20,30)

print(s1.avg())

student.school_name()
student.info()