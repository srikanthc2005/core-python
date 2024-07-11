import math

class basic_calc:

    def __init__(self):
        self.ans = 0

    def add(self, *n):
        self.ans = sum(n)
        print(self.ans)
    def subtract(self, n1,*n):
        self.ans = n1 - sum(n)
        print(self.ans)
    def multiply(self, *n):
        self.ans = math.prod(n)
        print(self.ans)
    def divide(self, n1, n2):
        if n2 != 0:
            self.ans = n1/n2
        else:
            self.ans = math.inf
        print(self.ans)
    def remainder(self, n1, n2):
        if n2 != 0:
            self.ans = n1%n2
        else:
            self.ans = math.inf
        print(self.ans)
    def factorial(self, n):
        self.ans = 1
        for i in range(1,n+1):
            self.ans *= i
        print(self.ans)
    def reciprocal(self, n):
        self.ans = self.divide(1,n)
        print(self.ans)
        

class scientific_calc(basic_calc):

    def __init__(self):
        super().__init__()

    def square(self, n):
        self.ans = n**2
        print(self.ans)
    def cube(self, n):
        self.ans = n**3
        print(self.ans)
    def power(self, n1,n2):
        self.ans = n1**n2
        print(self.ans)
        
    def factorial(self, n):
        self.ans = math.factorial(n)
        print(self.ans)
    def square_root(self, n):
        self.ans = math.sqrt(n)
        print(f'{self.ans:.4f}')
    def cube_root(self, n):
        self.ans = math.cbrt(n)
        print(f'{self.ans:.4f}')

    def e_n(self, n):
        self.ans = math.e**n
        print(self.ans)
    def log_base_e(self, n):
        self.ans = math.log(n)
        print(self.ans)
    def log_base_10(self, n):
        self.ans = math.log(n)/math.log(10)
        print(self.ans)
    def log_base_2(self, n):
        self.ans = math.log(n)/math.log(2)
        print(self.ans)
        
    def sin_in_radians(self, n):
        self.ans = math.sin(n)
        if abs(self.ans) < 1e-5:
            self.ans = 0
        print(self.ans)
    def sin_in_degrees(self,n):
        self.ans = math.sin(n*math.pi/180)
        if abs(self.ans) < 1e-5:
            self.ans = 0
        print(self.ans)
        
    def cos_in_radians(self, n):
        self.ans = math.cos(n)
        if abs(self.ans) < 1e-5:
            self.ans = 0
        print(self.ans)
    def cos_in_degrees(self,n):
        self.ans = math.cos(n*math.pi/180)
        if abs(self.ans) < 1e-5:
            self.ans = 0
        print(self.ans)
        
    def tan_in_radians(self, n):
        self.ans = math.tan(n)
        if self.ans > 1e10:
            self.ans = math.inf
        elif self.ans < 1e-10:
            self.ans = -math.inf
        print(self.ans)
    def tan_in_degrees(self,n):
        self.ans = math.tan(n*math.pi/180)
        if self.ans > 1e10:
            self.ans = math.inf
        elif self.ans < 1e-10:
            self.ans = -math.inf
        print(self.ans)
    
    
    
    






#to run
c = scientific_calc()

c.add(6,8,3,2)
c.subtract(10,1,2,3,4)
c.multiply(6,8,9)
c.divide(5,2)
c.divide(5,0)
c.remainder(7,3)
c.remainder(7,0)
c.factorial(4)
c.reciprocal(5)
print()
c.square(4)
c.cube(2)
c.power(5,2)
c.factorial(6)
c.square_root(5)
c.cube_root(125)
c.e_n(3)
c.log_base_e(3)
c.log_base_10(2)
c.log_base_2(8)
c.sin_in_radians(math.pi/2)
c.sin_in_degrees(90)
c.cos_in_radians(math.pi/2)
c.cos_in_degrees(90)
c.tan_in_radians(math.pi/4)
c.tan_in_degrees(45)



