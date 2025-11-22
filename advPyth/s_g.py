class Bank:
    def __init__(self):
        self.__bal=10000

    # def get_bal(self): # getter
    #     return self.__bal
    # def set_bal(self,x): # setter
    #     self.__bal+=x
    #     print(self.__bal)
    @property
    def bal(self): # getter
        return self.__bal

    @bal.setter    
    def bal(self,x): # setter
        self.__bal+=x
        print(self.__bal)

obj=Bank()
# a=obj.get_bal()
# print(a)
# obj.set_bal(2000)

print(obj.bal) # getter
obj.bal=1000 # stter function