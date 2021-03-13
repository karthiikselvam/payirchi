class A: 
    def __init__(self, a): 
        self.a = a 
  
    # adding two objects  
    def __add__(self, o): 
        return self.a * o.a * 100  
ob1 = A(1) 
ob2 = A(2) 

  
print(ob1 + ob2)