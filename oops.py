class employee:
    def fun1(self):
        print("hello")
    def fun2(self):
        print("welcome")
e1=employee()
e1.fun1()

class xyz:
    def detail(self,id,name):
        self.i=id
        self.n=name
        print(id)
        print(name)
    def show(self):
        print(self.i)
e1=xyz()
e1.detail(1,"abcd")

'''class person:
    @staticmethod
    def fun(a,b):
        print(a+b)
p=person()
p.fun(25,10)'''

class employee:
    course ="python"
    def fun1(self,name,age):
        self.n=name
        self.a=age
    def fun2(self):
        print("student name",self.n)
        print("student age",self.a)
        print("student course",employee.course)
    @classmethod
    def detail(cls):
        cls.course="java"
e=employee()
e.fun1("xyz",23)
employee.detail()
e.fun2()

