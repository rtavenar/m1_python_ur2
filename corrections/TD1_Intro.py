# Section 1 : Imports de module
import random
import math
import datetime

# Section 2 : Définition de fonctions
def est_un_palindrome(chaine):
    palindrome = True
    for i in range(len(chaine)):
        if chaine[i] != chaine[-i-1]:
            palindrome = False
            break
    return palindrome


def est_bissextile(annee):
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    if annee % 400 == 0:
        return True
    return False


def nombre_jours(mois, annee):
    if mois == 2:
        if est_bissextile(annee):
            return 29
        else:
            return 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mois in [4, 6, 9, 11]:
        return 30
    else:
        return 0


def affiche_multiple(nom, nombre):
    for i in range(nombre):
        print(nom)
        
        
def age(jour, mois, annee):
    date_naissance = datetime.datetime(year=annee, month=mois, day=jour)
    duree = (datetime.datetime.now() - date_naissance).total_seconds()
    return duree // (3600 * 24 * 365.25)

# Section 3 : Tests de fonctions définies et manipulations en mode "script"

# Partie "Types et fonctions de base"
# 1.
print('3' * 10)
print(3 * 10)
# print('3' * 10.0)  # Erreur : la multiplication d'une chaîne par un flottant n'est pas définie en Python
print('3' + '3')
print(3 + 3)
# print('3' + 3)  # Erreur : la concaténation (opération '+') d'une chaîne et d'un entier n'est pas définie en Python

# 2.
chaine = "kayak2"
palindrome = True
for i in range(len(chaine)):
    if chaine[i] != chaine[-i-1]:
        palindrome = False
        break
print(palindrome)

# 3.
print(est_un_palindrome("kayak"))
print(est_un_palindrome("kayak2"))

# 4.
print(nombre_jours(2, 2004))
print(nombre_jours(9, 2022))

# 5.
# Attention : cet appel est différent des autres car la fonction ne retourne rien !!!
affiche_multiple("Romain", 3)

# Partie "Focus sur les chaînes de caractères"
# 1.
replique_1_2 = "Je ne vous jette pas la pierre, Pierre,"
replique_2_2 = "mais j'étais à deux doigts de m'agacer"
replique_entiere = replique_1_2 + replique_2_2
print(len(replique_entiere))

# 2. 
replique_minuscules = replique_entiere.lower()
position = replique_minuscules.find("jette")
print(position)

# 3. 
print(replique_minuscules.replace("agacer", "énerver"))

# 4.
print(replique_minuscules.count("pierre"))

# Partie "Modules de base"
# 1.
random.seed(0)
print(random.uniform(0, 1))

# 2.
angle_degres = 45
print(math.sin(angle_degres / 180 * math.pi))

# 3.
print(age(8, 4, 1983))
print(age(12, 1, 2000))
