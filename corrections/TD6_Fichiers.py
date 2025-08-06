# Section 1 : Imports de module
import json
import os
import csv

#Section 2 : Définition de fonctions
def lecture_json(dossier, nom_fichier, encodage="utf-8"):
    nom_complet = os.path.join(dossier, nom_fichier)
    fp = open(nom_complet, "r", encoding=encodage)
    return json.load(fp)

def lexique_critere(liste_json, cle):
    liste_valeur = []
    for item in liste_json:
        liste_valeur.append(item[cle])
    return set(liste_valeur)

def restaurants_A(restaurants):
    liste_noms = []
    for restaurant in restaurants:
        for note in restaurant["grades"]:
            if note["grade"] == "A":
                liste_noms.append(restaurant["name"])
                break
    return liste_noms

def affiche_restaurants_S(restaurants):
    for restaurant in restaurants:
        if restaurant["name"].startswith("S"):
            print(f"{restaurant['name']} ({restaurant['borough']}) : {restaurant['cuisine']}")

def dates_notes(restaurants):
    liste_valeurs_dates= []
    for restaurant in restaurants:
        for note in restaurant["grades"]:
            liste_valeurs_dates.append(note["date"])
    return set(liste_valeurs_dates)

def restaurants_grades_a_plat(restaurants):
    for restaurant in restaurants:
        restaurant["n_grades"] = len(restaurant["grades"])
        del restaurant["grades"]
    return restaurants

def compte_par_cuisine(restaurants):
    compte = {}
    for restaurant in restaurants:
        cuisine = restaurant["cuisine"]
        if cuisine not in compte:
            compte[cuisine] = 0
        compte[cuisine] += 1
    return compte

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
print(len(restaurants))
# Q2
print(lexique_critere(restaurants, "cuisine"))
# Q3
print(restaurants_A(restaurants))
# Q4
affiche_restaurants_S(restaurants)
# Q5
n = 0
for resto in restaurants:
    if resto["address"]["zipcode"].startswith("10"):
        n += 1
print(f"Le nombre de restaurants dont le code postal commence par 10 est {n}")
# Q6
print(dates_notes(restaurants))
# Q7
print(compte_par_cuisine(restaurants))

# 3 Export au format CSV
# Q1
restaurants = restaurants_grades_a_plat(restaurants)
print(restaurants[:2])
# Q2
restaurants = restaurants_adresse_a_plat(restaurants)
print(restaurants[:2])
# Q3
export_json_to_csv(restaurants, "restaurants.csv")
