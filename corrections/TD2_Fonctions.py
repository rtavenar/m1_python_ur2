# Section 1 : Imports de module

# Section 2 : Définition de fonctions
def compte_mots(chaine):
    les_mots = chaine.split()
    return len(les_mots)


def est_un_fichier_texte(nom_fichier):
    return (nom_fichier.endswith(".txt") or 
            nom_fichier.endswith(".csv") or 
            nom_fichier.endswith(".json"))
    

def table_multiplication(base, mult_debut, mult_fin):
    for i in range(mult_debut, mult_fin + 1):
        print(f"{base}*{i}={base*i}")

    
def annees_production():
    n_grains = 0
    for i in range(64):
        n_grains += 2 ** i
    
    masse_annuelle = 650 * 10 ** 6 * 10 ** 6
    n_grains_par_an = masse_annuelle / 0.035
    
    return n_grains / n_grains_par_an


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


def date_lendemain(jour, mois, annee):
    if jour == nombre_jours(mois, annee):
        if mois == 12:
            return 1, 1, annee + 1
        else:
            return 1, mois + 1, annee
    else:
        return jour + 1, mois, annee


def table_multiplication_usuelle(base):
    table_multiplication(base, mult_debut=1, mult_fin=10)
    

def occurrences_majuscule(s, let):
    return s.count(let.upper())
    

def occurrences_A_majuscule(s):
    return occurrences_majuscule(s, "a")
    
# Section 3 : Tests de fonctions définies et manipulations en mode "script"

# Exercices indépendants
# 1.
print(compte_mots("la vie est belle"))

# 2.
print(est_un_fichier_texte("truc.csv"))
print(est_un_fichier_texte("truc.xls"))

# 3.
table_multiplication(5, 4, 7)

# 4.
print(annees_production())

# 5.
print(date_lendemain(8, 4, 1983))
print(date_lendemain(31, 12, 1983))
print(date_lendemain(30, 11, 1983))

# Du cas général au cas particulier
# 1.
table_multiplication_usuelle(5)

# 2.
print(occurrences_majuscule("La vie est belle", "l"))

# 3.
print(occurrences_A_majuscule("LA vie est belle Ah ah ah"))

