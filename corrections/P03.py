from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def forward(self, x):
        raise NotImplementedError
    
    @abstractmethod
    def grad(self, x):
        raise NotImplementedError
    
    def __add__(self, other):
        return Add(self, other)
    
    def __mul__(self, other):
        return Mul(self, other)
    
    def __pow__(self, p):
        if not isinstance(p, int):
            raise NotImplementedError
        return Pow(self, p)

class Constante(Expression):
    def __init__(self, valeur):
        self.valeur = valeur
    
    def forward(self, x):
        return self.valeur
    
    def grad(self, x):
        return 0
    
    def __str__(self):
        return f"{self.valeur}"

class Variable(Expression):
    def forward(self, x):
        return x
    
    def grad(self, x):
        return 1
    
    def __str__(self):
        return "x"

class Add(Expression):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def forward(self, x):
        return self.a.forward(x) + self.b.forward(x)
    
    def grad(self, x):
        return self.a.grad(x) + self.b.grad(x)
    
    def __str__(self):
        return f"{self.a} + {self.b}"

class Mul(Expression):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def forward(self, x):
        return self.a.forward(x) * self.b.forward(x)
    
    def grad(self, x):
        return self.a.grad(x) * self.b.forward(x) + self.b.grad(x) * self.a.forward(x)
    
    def __str__(self):
        return f"({self.a}) * ({self.b})"

class Pow(Expression):
    def __init__(self, a, p):
        self.a = a
        self.p = p
    
    def forward(self, x):
        return self.a.forward(x) ** self.p
    
    def grad(self, x):
        return self.p * self.a.grad(x) * self.a.forward(x) ** (self.p - 1)
    
    def __str__(self):
        return f"({self.a}) ** {self.p}"


def descente_gradient(expr, x_0, rho):
    x_t = x_0
    for i in range(20):
        print(f"Iteration {i:02d}, x={x_t:.3f}, f(x)={expr.forward(x_t):.3f}")
        x_t -= rho * expr.grad(x_t)
    return x_t

x = Variable()
c_3 = Constante(3)

expr = ((x + c_3) ** 2)
print(expr)

print(expr.forward(0))
print(expr.grad(0))

descente_gradient(expr, x_0=0., rho=0.1)
