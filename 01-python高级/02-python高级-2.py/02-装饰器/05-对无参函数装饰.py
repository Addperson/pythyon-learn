def func(functionName):

    print("---func_1---")
    
    def func_in():

        print("---func_in_1---")

        functionName()

        print("---func_in_2---")

    
    print("---func_2---")

    return func_in
@func
def test():
    print("---test---")

test()
