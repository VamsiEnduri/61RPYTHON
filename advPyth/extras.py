# lambda,map,filter,reduce,iterators, generators

# def a(x,y):
#     print(x+y)
# a(10,20)    

# lambda is a functions without a any name to it so it is called as anonymus function
# sytax :-- 

# lambda params: #code single line code
# abc=lambda x,y: print(x+y)
# abc(10,20)

# abc=lambda x:[print(i) for i in x]
# abc([1,2,3,4,5])

# abc=lambda x,y,z,a,b: print(x+y+z+a+b)
# abc(1,2,3,4,5)

# abc=lambda *a: [print(i) for i in a]
# abc(1,2,3,4,5)

# abc=lambda **a:[print(i) for i in a]
# abc(name="vamsi",age=27)

#1st way
# map(func()) #args
# salaries=[16000,8888,150000,35000]
# a=lambda x:x+5000
# map(func,iterable)
# res=list(map(a,salaries))

# #2nd way
# res=list(map(lambda x:x+5000,[16000,8888,150000,35000]))

# print(res)


# # filter:--
# a=lambda x:x%2==0
# nums=[1,2,3,4,5]
# # filter(func,iteraable)
# res=list(filter(a,nums))
# print(res)


# reduce :-- 
from functools import reduce 
def a(x,y):
    return x+y
# a=lambda x,y:x+y
nums=[1,2,3,4,5]

res=reduce(a,nums)
print(res)