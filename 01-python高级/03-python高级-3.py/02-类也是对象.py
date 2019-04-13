def printNum(self):

    print("---num---%s---"%self.num)

test=type("test",(),{"printNum":printNum})

p1=test()

p1.num=100

p1.printNum()

