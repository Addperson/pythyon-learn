def func_arg(arg):

    def func(functionName):
        
        def func_in():

            print("---正在记录---arg=%s---"%(arg))

            functionName()

        return func_in
    
    return func

@func_arg("heihei")
def test():
    print("---test---")
test()

@func_arg("haha")
def test2():
    print("---test2---")

test2()

