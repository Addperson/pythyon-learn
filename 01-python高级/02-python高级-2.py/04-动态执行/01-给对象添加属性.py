class Person(object):
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge

laowang=Person("老王",10)

laowang.addr="江西"

print("---%s---"%laowang.addr)

