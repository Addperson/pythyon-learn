def upper_attr(future_class_name,future_class_parents,future_class_attr):

    newAttr={}

    for name,value in future_class_attr.items():

        if not name.startswith("__"):
            
           newAttr[ name.upper()]=value

    return type(future_class_name,future_class_parents,newAttr)

class Foo(object):

    __metaclass__=upper_attr#python2用

    bar='bip'

p=Foo()

print(hasattr(p,'bar'))

