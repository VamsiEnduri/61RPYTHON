#  decorator is a function which takes another function as arg and return new function


def add():
    a=10
    b=20
    c=a+b
    print(c)

def dec(param):
    def abc():
        param()
    return abc    


a=dec(add) 
a()   