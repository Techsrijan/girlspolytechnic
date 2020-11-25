class student:
    school="techsrijan"
    def student_info(self):
        print("This function will print student data")

    # __init__ is constructor
    def __init__(self):
        print("this will run when the object is created")

    def student_name(self,name):
        print(name,self.school)
# this line will create a object of class student
a=student()  # this will call constructor automatically
print(type(a))
b=student()   # this will call constructor automatically
student.student_info(a)
# here self means the object of class
a.student_info()
b.student_info()
c=student()
c.student_name("ram")
