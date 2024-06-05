class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("my name"+self.name)
       # print("my age"+self.age)
p1=person('akki',21)
p1.myfunc()