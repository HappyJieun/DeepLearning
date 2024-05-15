class Cals:
    def __init__ (self):
        self.x=0
        self.y=0
        self.result=0

    def add(self,x,y):
        self.x=x
        self.y=y
        self.result=self.x+self.y
        
    def equal(self):
        print(self.x, '+', self.y,'=', self.result)
class Cals2(Cals):
    def minus(self,x,y):
        self.x=x
        self.y=y
        self.result=self.x-self.y
        
    def equal2(self):
        print(self.x, '+', self.y,'=', self.result)
        
        
Calculator = Cals()
Calculator.equal()
print(Calculator.x, '+', Calculator.y,'=', Calculator.result)
print("+++++")
Calculator.add(3,2)
Calculator.equal()
print("+++++")
Calculator.result=100
Calculator.equal() # result값이 변경됨
print("#########################")

Calculator2 = Cals2()

Calculator2.add(3,2)
Calculator2.equal()

Calculator2.minus(3,2)
Calculator2.equal2()


class block_factory:
    def __init__(self, company='none'):
        self.company=company
        print(self.company)
block1=block_factory()
block2=block_factory('gole')
