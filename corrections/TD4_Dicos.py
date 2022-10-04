# Section 1 : Imports de module

# Section 2 : Définition de fonctions
def normalise_texte(texte):
    dico_conversion_caracteres_speciaux = {"À": "A", "Â": "A", "Æ": "AE", "Ç": "C", "É": "E", "È": "E", "Ê": "E", "Ë": "E", "Î": "I", "Ï": "I", "Ô": "O", "Œ": "OE", "Ù": "U", "Û": "U", "Ü": "U", "à": "a", "â": "a", "æ": "ae", "ç": "c", "é": "e", "è": "e", "ê": "e", "ë": "e", "î": "i", "ï": "i", "ô": "o", "œ": "oe", "ù": "u", "û": "u", "ü": "u", "ÿ": "y"}
    texte_conv = ""
    for car in texte:
        if car in dico_conversion_caracteres_speciaux:
            texte_conv += dico_conversion_caracteres_speciaux[car]
        else:
            texte_conv += car
    return texte_conv

def occurence_mot(texte):
    liste_texte = texte.split()
    dico_occurence_mot = {}
    for mot in set(liste_texte):
        dico_occurence_mot[mot] = texte.count(mot)
    return dico_occurence_mot

def occurence_valeur_max(dico_valeur_occurence):
    occurence_max = 0
    valeur_max = None
    for valeur, occurence in dico_valeur_occurence.items():
        if occurence_max <= occurence:
            occurence_max = occurence
            valeur_max = valeur
    return valeur_max

def occurence_mot_max(texte):
    return occurence_valeur_max(occurence_mot(texte))

def total_ventes(ventes):
    total = 0
    for montant in ventes.values():
        total += montant
    return total

def vendeur_vente_max(ventes):
    return occurence_valeur_max(ventes)

def liste_triee_sans_doublon(l_entree):
    return sorted(list(set(l_entree)))

def nb_element_distinct(liste):
    return len(set(liste))

def pangramme(phrase):
    phrase_set = set(phrase.lower())
    return (len(phrase_set) == 26 and " " not in phrase_set) or (len(phrase_set) == 27 and " " in phrase_set)

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
#2 Les dictionnaires
#Q1
test_texte = "Dès Noël où un zéphyr haï me vêt de glaçons würmiens, je dîne d’exquis rôtis de bœuf au kir à l’aÿ d’âge mûr et cætera!"
print(normalise_texte(test_texte))

#Q2
test_texte = "Écrire une fonction qui à partir d’une chaîne de caractères passée en argument renvoie un dictionnaire associant chaque mot à son nombre d’occurrences dans la chaîne."
print(occurence_mot(test_texte))

#Q3
print(occurence_mot_max(test_texte))

#Q41
ventes = {"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}
print(total_ventes(ventes))

#Q42
print(vendeur_vente_max(ventes))

#3 Les sets
#Q1
print(liste_triee_sans_doublon([2, 5, 8, 3, 2, 4, 12, 7, 5]))

#Q2
print(nb_element_distinct([2, 5, 8, 3, 2, 4, 12, 7, 5]))

#Q3
phrase1 = "Portez ce vieux whisky au juge blond qui fume"
phrase2 = "J ai vu un punk afghan et deux clowns aux zygomatiques incroyables"
print(pangramme(phrase1))
print(pangramme(phrase2))
