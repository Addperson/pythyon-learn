def test(func):

    def inner():

        print("---进行身份验证---")
        func()
    return inner

#f1=test(f1)
@test
def f1():
    print("---f1---")
def f2():
    print("---f2---")

 
f1()
