import types
class Person(object):
    def __init__(self,newName,newAge):
        self.name=newName
        self.age=newAge

def run(self):
    print("--%s再跑--"%self.name)
laowang=Person("老王",10)

laowang.addr="江西"

print("---%s---"%laowang.addr)

laowang.run=types.MethodType(run,laowang)
laowang.run()

