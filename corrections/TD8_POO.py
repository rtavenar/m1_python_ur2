from abc import ABC, abstractmethod, abstractproperty
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    
    def __str__(self):
        return f'Point(x={self.x},y={self.y})'
    
    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

class Intervalle:
    def __init__(self, a, b):
        self.a, self.b = a, b
        
    def __contains__(self, v):
        return v >= self.a and v <= self.b
    
class Fraction:
    def __init__(self, num=1, den=1, signe=1):
        self.num = num
        self.den = den
        self.signe = signe
    
    def __str__(self):
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

class CompteSimple:
    def __init__(self):
        self.solde = 0
    
    def __str__(self):
        return f"Le solde du compte est de {self.solde} Euro(s)"
    
    def enregistrerOperation(self, op):
        self.solde += op

class CompteCourant(CompteSimple):
    def __init__(self):
        self.operations = []
        
    @property
    def solde(self):
        return sum(self.operations)
    
    @property
    def releveDebits(self):
        return [op for op in self.operations if op < 0]
    
    @property
    def releveCredits(self):
        return [op for op in self.operations if op >= 0]
        
    def enregistrerOperation(self, op):
        self.operations.append(op)
    
    def afficherReleve(self):
        print("Relevé de compte :")
        for op in self.operations:
            print(f"* {op}")
    
    def afficherReleveCredits(self):
        print("Relevé de crédits :")
        for op in self.releveCredits:
            print(f"* {op}")
    
    def afficherReleveDebits(self):
        print("Relevé de débits :")
        for op in self.releveDebits:
            print(f"* {op}")
    

class IntervalleAbstrait(ABC):
    def __init__(self, a, b):
        self.a, self.b = a, b
        
    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, v):
        raise NotImplementedError

class IntervalleOuvert(IntervalleAbstrait):
    def __str__(self):
        return f"]{self.a}, {self.b}["

    def __contains__(self, v):
        return v > self.a and v < self.b

class IntervalleFerme(IntervalleAbstrait):
    def __str__(self):
        return f"[{self.a}, {self.b}]"

    def __contains__(self, v):
        return v >= self.a and v <= self.b



p0 = Point(0, 1)
p1 = Point(0, 0)
print(Point.distance(p0, p1))

print(15 in Intervalle(10, 20))

f0 = Fraction(1, 5)
f1 = Fraction(2, 3)
print(f0 * f1)
print(f0 - f1)

c = CompteSimple()
c.enregistrerOperation(100)
c.enregistrerOperation(-32)
print(c)

cc = CompteCourant()
cc.enregistrerOperation(100)
cc.enregistrerOperation(-32)
cc.afficherReleve()
cc.afficherReleveCredits()
cc.afficherReleveDebits()
print(cc.solde)

print(10 in IntervalleOuvert(10, 20))
print(10 in IntervalleFerme(10, 20))
