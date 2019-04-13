def test1():
    while True:
        print("---1---")
        yield None

def test2():
    while True:
        print("---2---")
        yield None

test1=test1()
test2=test2()
while True:
    test1.__next__()
    test2.__next__()
