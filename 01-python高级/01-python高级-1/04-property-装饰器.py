class Test(object):
    def __init__(self):
        self.__num=100
    @property
    def num(self):
        print("----getter")
        return self.__num
    @num.setter
    def num(self,num):
        print("----setter")
        self.__num=num
t=Test()
#print(t.getNum())
#t.setNum(50)
#print(t.getNum())
t.num=50
print(t.num)
