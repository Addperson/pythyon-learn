class Test(object):
    def __init__(self):
        self.__num=100
    def setNum(self,num):
        print("----setter")
        self.__num=num
    def getNum(self):
        print("----getter")
        return self.__num
    num=property(getNum,setNum)
t=Test()
#print(t.getNum())
#t.setNum(50)
#print(t.getNum())
t.num=50
print(t.num)
