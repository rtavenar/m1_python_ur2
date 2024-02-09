from abc import ABC, abstractmethod, abstractproperty

class CompteSimple:
    def __init__(self):
        self.solde = 0
    
    def __repr__(self):
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
    def __repr__(self):
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, v):
        raise NotImplementedError

class IntervalleOuvert(IntervalleAbstrait):
    def __repr__(self):
        return f"]{self.a}, {self.b}["

    def __contains__(self, v):
        return v > self.a and v < self.b

class IntervalleFerme(IntervalleAbstrait):
    def __repr__(self):
        return f"[{self.a}, {self.b}]"

    def __contains__(self, v):
        return v >= self.a and v <= self.b


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
