class Test(object):

    def __init__(self,func):
        print("开始装饰---")

        self.__func=func

    def __call__(self):
        
        print("---装饰器执行的功能---")

        self.__func()
@Test
def test():

    print("---test---")

test()

