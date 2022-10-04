# Section 1 : Imports de module
import numpy as np

# Section 2 : Définition de fonctions

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
# 2 Définition de structures numpy
#Q1
v = np.zeros(4)
print(v)
#Q2
I_4 = np.eye(4)
print(I_4)
#Q3
M = np.reshape(range(12), (3, 4))
print(M)
#Q4
print(np.transpose(M))
#Q6
M2 = np.ones((10, 10))
M2[1:9, 1:9] = 0
print(M2)
#Q7 => pourquoi standardiser ? ce n'est pas la fonction uniform ?
M3 = np.random.uniform(size=(10, 10))
print(M3)

# 3 Calculs
#Q1
print(M)
print(I_4)
print(M @ I_4)
print(v)
print(M @ I_4 + v)
#Q2
print(np.sum(M, axis=1))

#Q3
x = np.array([0.1, 0.2, 0.4])
y = np.array([1., 2., 8.])
print(x.reshape((3,1)), y.reshape((1,3)))
C = 1/(x.reshape((3,1)) - y.reshape((1,3)))
print(C)

#Q4 => Avec une matrice pas carrée c'est plus facile de se repérer ; j'avais commencé par faire la moyenne des colonnes avec un axis=0
M4 = np.random.uniform(size=(10, 3))
print(M4.shape)
print(np.mean(M4, axis=1).shape)
M4 = M4 - np.mean(M4, axis=1).reshape(10, 1)
print(M4)
print(np.mean(M4, axis=1))

# 4 Exercice de synthèse
#Q1
notes = np.array(
    [[10, 12],
    [15, 16],
    [18, 12]]
    )
print(notes)
moyennes = np.mean(notes, axis=0)
print(moyennes)
#Q2
notes_sup_douze = np.sum(notes > 12)
print(notes_sup_douze)