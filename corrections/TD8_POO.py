from abc import ABC, abstractmethod, abstractproperty
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    
    def __repr__(self):
        return f'Point(x={self.x},y={self.y})'
    
    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)

class Intervalle:
    def __init__(self, a, b):
        self.a, self.b = a, b
        
    def __contains__(self, v):
        return v >= self.a and v <= self.b

class Fraction:
    def __init__(self, num=1, den=1):
        self.num = abs(num)
        self.den = abs(den)
        if num * den >= 0:
            self.signe = 1
        else:
            self.signe = -1
    
    def __repr__(self):
        if self.signe > 0:
            return f"({self.num}/{self.den})"
        else:
            return f"(-{self.num}/{self.den})"
    
    def __neg__(self):
        return Fraction(-1 * self.signe * self.num, self.den)
    
    def __add__(self, other):
        return Fraction(self.signe * other.signe * (self.num * other.den + other.num * self.den), self.den * other.den)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        return Fraction(self.signe * other.signe * self.num * other.num, self.den * other.den)
    
class Fraction:
    def __init__(self, num=1, den=1, signe=1):
        self.num = num
        self.den = den
        self.signe = signe
    
    def __repr__(self):
        if self.signe > 0:
            return f"({self.num}/{self.den})"
        else:
            return f"(-{self.num}/{self.den})"
    
    def __neg__(self):
        return Fraction(self.num, self.den, -1 * self.signe)
    
    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den, self.signe * other.signe)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den, self.signe * other.signe)



p0 = Point(0, 1)
p1 = Point(0, 0)
print(p0.distance(p1))

print(15 in Intervalle(10, 20))

f0 = Fraction(1, 5)
f1 = Fraction(2, 3)
print(f0 * f1)
print(f0 - f1)
