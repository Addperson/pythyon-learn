def func(functionName):

    print("---func_1---")
    
    def func_in(*args,**kwargs):

        print("---func_in_1---")

        ret=functionName(*args,**kwargs)

        return ret

        print("---func_in_2---")

    
    print("---func_2---")

    return func_in
@func
def test1():
    print("---test1---")
@func
def test2():
    print("---test2---")
    return "hh"
@func
def test3(x,y):
    print("x=%s,y=%s"%(x,y))

test1()
ret=test2()
print(ret)
test3(10,20)








