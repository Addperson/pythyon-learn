def makeBold(fn):
   
    print("---正在装饰1---")
    def wrapped():
        print("正在加粗")
        return "<b>"+fn()+"</b>"
    return wrapped

def makeItalic(fn):

    print("---正在装饰2---")
    def wrapped():
        print("正在加斜体")
        return "<i>"+fn()+"</i>"
    return wrapped

@makeBold
@makeItalic
def test():
    print("---执行函数---")
    return"hello,world"
ret=test()
print(ret)
