def test(func):

    def inner():

        print("---进行身份验证---")
        func()
    return inner
def f1():
    print("---f1---")
def f2():
    print("---f2---")

f1=test(f1)
 
f1()
