def func(functionName):

    print("---func_1---")
    
    def func_in(aa,bb):

        print("---func_in_1---")

        ret=functionName(aa,bb)

        print("---func_in_2---")
        
        return ret
    
    print("---func_2---")

    return func_in
@func
def test(x,y):
    print("---test---x=%s,y=%s"%(x,y))
    return "haha"
ret= test(10,20)

print(ret)
