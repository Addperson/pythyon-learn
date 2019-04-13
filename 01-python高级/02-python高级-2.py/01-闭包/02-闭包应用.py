def test(a,b):
    
    def line(x):
        print(a*x+b)

    return line

line_1=test(1,1)

line_1(2)

line_2=test(4,5)

line_2(2)
