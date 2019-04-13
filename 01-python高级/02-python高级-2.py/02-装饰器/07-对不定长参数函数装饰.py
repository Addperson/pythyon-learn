def func(functionName):

    print("---func_1---")
    
    def func_in(*args,**kwargs):

        print("---func_in_1---")

        functionName(*args,**kwargs)

        print("---func_in_2---")

    
    print("---func_2---")

    return func_in
@func
def test(x,y):
    print("---test---x=%s,y=%s"%(x,y))
@func
def test2(x,y,z):
    print("---test---x=%s,y=%s,z=%s"%(x,y,z))
test(10,30)
test2(1,2,3)
