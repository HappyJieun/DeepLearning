class Cals:
    def __init__ (self):
        self.__x=0
        self.__y=0
        self.__result=0

    def add(self,x,y):
        self.__x=x
        self.__y=y
        self.__result=self.__x+self.__y
        
    def equal(self):
        print(self.__x, '+', self.__y,'=', self.__result)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_result(self):
        return self.__result

## main ##        
Calculator = Cals()
print(Calculator.get_x(), '+', Calculator.get_y(),'=', Calculator.get_result())
print("+++++")
Calculator.add(3,2)
Calculator.equal()
print("+++++")
print(Calculator.get_x(), '+', Calculator.get_y(),'=', Calculator.get_result())
