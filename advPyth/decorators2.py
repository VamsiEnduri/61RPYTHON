# # decorator is a func which takes another function as arg and returns new function 
# def abc():
#     print("abc")
# def dec(a):
#     def xyz():
#         a()
#         print("hlo")
#     return xyz 
# r=dec(abc)  
# r()  

# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
#     return c
# abcdef=add()    
# print(abcdef)

# callback function :
# def login():
#     print("successful")

# def loginDecorator(a):
#     a()

# loginDecorator(login)

# loginDecorator is decorator function which takes login function as arg and retruns details function and in that details function we call arg function along with other logics
def login():
    user_name="v"
    password="v"
    un=input("enter username :-- ")
    pswd=input("enter pswd here :-- ")
    if un==user_name and pswd==password:
        print("login successful")

def loginDecorator(a):
    def details():
        def begoreLogin():
            print("before logging") # 7:20
        begoreLogin()    
        a() # working
        def logout(msg): # 5:30
            print(msg)
        logout("logged in happended and done")
    return details        
res=loginDecorator(login)
res()