import random
import json

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    @property
    def valeur_numerique(self):
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 
                "Valet", "Dame", "Roi", 1].index(self.valeur)

# !!!
# Compléter le code ici

# Tests
jeu = EnsembleDe32Cartes()
print(f"Jeu de {len(jeu)} cartes")
# Sortie : Jeu de 32 cartes
jeu.melanger()
# la méthode piocher retourne une liste d'objets Carte :
print(jeu.piocher(n_cartes=3))
# Sortie : [1 de Carreau, 8 de Pique, Valet de Trèfle]

mes_cartes = jeu.piocher(n_cartes=5)
print(sorted(mes_cartes))
# Sortie : [7 de Carreau, 9 de Carreau, Dame de Coeur, Roi de Pique, 1 de Trèfle]

autre_jeu = EnsembleDeCartesPersonnalise("cartes.json")
print(f"Jeu de {len(autre_jeu)} cartes")
# Sortie : Jeu de 6 cartes
print(autre_jeu.piocher(n_cartes=len(autre_jeu)))
# Sortie : [8 de Carreau, 7 de Carreau, 5 de Carreau, 2 de Trèfle, 8 de Trèfle, 3 de Trèfle]

dernier_jeu = EnsembleDeCartesPersonnaliseAPI("https://raw.githubusercontent.com/rtavenar/m1_python_ur2/main/modules_fournis/cartes.json")
print(f"Jeu de {len(dernier_jeu)} cartes")
# Sortie : Jeu de 6 cartes
print(dernier_jeu.piocher(n_cartes=len(dernier_jeu)))
# Sortie : [8 de Coeur, 7 de Coeur, 5 de Coeur, 2 de Trèfle, 8 de Trèfle, 3 de Trèfle]