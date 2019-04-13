def test(number):

    print(number)
    print("---1---")

    def test_in(number_in):
        print("---2---")
        print(number+number_in)

    print("---3---")

    return test_in

ret=test(100)

print("_"*30)

ret(50)
