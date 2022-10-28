# Section 1 : Imports de module
import json
import os
import csv

#Section 2 : Définition de fonctions
def lecture_json(dossier, nom_fichier, encodage="utf-8"):
    nom_complet = os.path.join(dossier, nom_fichier)
    fp = open(nom_complet, "r", encoding=encodage)
    return json.load(fp)

def comptage_critere(liste_json, cle, valeur):
    effectif = 0
    for item in liste_json:
        if item[cle] == valeur:
            effectif+=1
    return effectif

def lexique_critere(liste_json, cle):
    liste_valeur = []
    for item in liste_json:
        liste_valeur.append(item[cle])
    return set(liste_valeur)

def filtrage_restaurant(restaurants, quartier):
    for restaurant in restaurants:
        if restaurant["borough"] == quartier:
            print(f'{restaurant["name"]}: {restaurant["address"]["building"]}, {restaurant["address"]["street"]}, {restaurant["address"]["zipcode"]} New York, USA')

def comptage_notes(restaurants):
    effectif = 0
    for restaurant in restaurants:
        effectif += len(restaurant["grades"])
    return effectif

def valeurs_possibles_notes(restaurants):
    liste_valeurs_notes= []
    for restaurant in restaurants:
        for note in restaurant["grades"]:
            liste_valeurs_notes.append(note["grade"])
    return set(liste_valeurs_notes)

def restaurants_grades_a_plat(restaurants):
    for restaurant in restaurants:
        restaurant["n_grades"] = len(restaurant["grades"])
        del restaurant["grades"]
    return restaurants

def restaurants_adresse_a_plat(restaurants):
    for restaurant in restaurants:
        restaurant["latitude"] = restaurant["address"]["loc"]["coordinates"][0]
        restaurant["longitude"] = restaurant["address"]["loc"]["coordinates"][1]
        del restaurant["address"]
    return restaurants

def export_json_to_csv(restaurants, nom_fichier_csv):
    with open(nom_fichier_csv, "w", encoding="utf-8", newline="\n") as fp:
        csvfp = csv.DictWriter(fp,
            fieldnames=restaurants[0].keys(),
            delimiter=";")
        csvfp.writeheader()
        for r in restaurants:
            csvfp.writerow(r)

# Section 3 : Tests de fonctions définies et manipulations en mode "script"

# 2 Extraction d’informations élémentaires
# Q1
dossier = "data"
nom_fichier = "NYfood.json"
restaurants = lecture_json(dossier, nom_fichier)
# Q2
print(len(restaurants)) #142
# Q3
print(comptage_critere(restaurants, "borough", "Manhattan")) #59
# Q4
print(lexique_critere(restaurants, "borough")) #{'Queens', 'Staten Island', 'Brooklyn', 'Bronx', 'Manhattan'}
# Q5
filtrage_restaurant(restaurants, "Manhattan")
# Q6
print(comptage_notes(restaurants)) #523
# Q7
print(valeurs_possibles_notes(restaurants)) #{'B', 'Z', 'C', 'A', 'P', 'Not Yet Graded'}

# 3 Export au format CSV
# Q1
restaurants = restaurants_grades_a_plat(restaurants)
print(restaurants[:2])
# Q2
restaurants = restaurants_adresse_a_plat(restaurants)
print(restaurants[:2])
# Q3
export_json_to_csv(restaurants, "restaurants.csv")
