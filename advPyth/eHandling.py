# # # a=100
# # # b=0
# # # c=a/b # 100 / 0
# # # print(c)
# # # print("vamsi")
# # # print(10)
a=100
b=10
try:
    c=a/b 
    d=int(input("enter a value here :--- ")) # 'vamsi' :-- int
    try:
        e=d # 1
        v=[1]
        print(v[10])
        abc=e+"vamsi" # 1+"vamsi"
        print(abc)
    except IndexError:
        print("perform any opeartions b.w same type of data")    
    except TypeError:
        pass

except IndentationError:
    print("give indentation")    
except IndexError:
    print("you are trying to access items out of range")
except ZeroDivisionError:
    print("you cant divide numerator with o value in denominator")
except ValueError:
    print("enter proper values to have smoooth execution")    
finally:
    print("finally executed")
print("vamsi")
print(10)        

# # try:
# #     pass
# # except:
# #     pass
# # finally:
# #     print("vamsi")        


try:
    print(10/10)
finally:
    print(10)    

try:
except :
    except:
finally :  

ind 
val 
type 
ZeroDivisionError
attr 
key
name
syntax
indentation 