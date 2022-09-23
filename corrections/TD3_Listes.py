# Section 1 : Imports de module
import math
# Section 2 : Définition de fonctions
def print_sinus():
    for angle in range(360):
        angle_radian = angle*2*math.pi/360
        print(angle_radian, math.sin(angle_radian))

def table_mutliplication(base):
    table = []
    for mult in range(1, 11):
        table.append(mult*base)
    return table

def plusieurs_tables(liste_base):
    tables = []
    for base in liste_base:
        tables.append(table_mutliplication(base))
    return tables

def elevation_puissance(borne_inf, borne_sup, puissance):
    liste_elevation_puissance = []
    for entier in range(borne_inf, borne_sup+1):
        liste_elevation_puissance.append(entier**puissance)
    return liste_elevation_puissance

def elevation_carre(borne_inf, borne_sup):
    return elevation_puissance(borne_inf, borne_sup, 2)

def len_list_str(l_chaines):
    liste_len = []
    for chaine in l_chaines:
        liste_len.append(len(chaine))
    return liste_len

def liste_triee_sans_doublon(l_entree):
    l_sortie = []
    for entier in l_entree:
        if entier not in l_sortie:
            l_sortie.append(entier)
    l_sortie.sort()
    return l_sortie

def mot_plus_long(chaine):
    mot_long = ''
    for mot in chaine.split():
        if len(mot) >= len(mot_long):
            mot_long = mot
    return mot_long

def liste_entiers_pairs(l_entier):
    l_entier_pair = []
    for entier in l_entier:
        if entier%2 == 0:
            l_entier_pair.append(entier)
    return l_entier_pair

def liste_plus_trois(l_entree):
    return [entier + 3 for entier in l_entree]

def liste_chaine_vers_reel(chaine):
    return [float(chaine_reel) for chaine_reel in chaine.split()]

# Section 3 : Tests de fonctions définies et manipulations en mode "script"

print_sinus()
print(plusieurs_tables([2, 5]))

print(elevation_puissance(2, 17, 2))
print(elevation_puissance(-2, 20, 3))

print(elevation_carre(2, 17))

print(len_list_str(['Toto', 'Super toto', 'Super Toto est super fort']))

print(liste_triee_sans_doublon([2, 5, 8, 3, 2, 4, 12, 7, 5]))

print(mot_plus_long('Super toto est super fort'))

print(liste_entiers_pairs([2, 5, 7, 6]))

print(liste_plus_trois([2, 5, 7, 6]))

print(liste_chaine_vers_reel("1.0 3.14 7 8.4 0.0"))
