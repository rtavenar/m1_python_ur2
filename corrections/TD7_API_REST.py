# Imports
import requests
import json
from graphh import GraphHopper
from pprint import pprint


# Fonctions
def api_position_bus(url):
    http_headers = {'User-Agent': "Mozilla/5.0"}
    contenu_brut = requests.get(url, headers=http_headers)
    contenu_json = contenu_brut.json()
    return contenu_json

def bus_en_service():
    url = "https://data.explore.star.fr/api/explore/v2.1/catalog/datasets/tco-bus-vehicules-position-tr/records?limit=-1&refine=etat%3AEn%20ligne"
    les_bus = api_position_bus(url)
    liste_pos = []
    for bus in les_bus["results"]:
        d = {}
        for cle in ["numerobus", "nomcourtligne", "destination", "ecartsecondes", "position"]:
            d[cle] = bus[cle]
        liste_pos.append(d)
    return liste_pos

def nb_bus_en_avance(bus_en_ligne):
    nombre_bus_en_avance = 0
    for bus in bus_en_ligne:
        if bus["ecartsecondes"] > 0:
            nombre_bus_en_avance+=1
    return nombre_bus_en_avance

def ligne_de_bus_ecartensecondes(les_bus):
    dico_ligne_de_bus_ecartensecondes = {}
    for bus in les_bus:
        nomcourtligne = bus["nomcourtligne"]
        ecartensecondes = bus["ecartsecondes"]
        if nomcourtligne not in dico_ligne_de_bus_ecartensecondes.keys():
            dico_ligne_de_bus_ecartensecondes[nomcourtligne] = [ecartensecondes]
        else:
            dico_ligne_de_bus_ecartensecondes[nomcourtligne].append(ecartensecondes)
    return dico_ligne_de_bus_ecartensecondes

def lecture_fichier_json(nom_fic):
    with open(nom_fic, 'rt', encoding='utf8') as obj_fic:
        return json.load(obj_fic)

def recherche_bus(les_bus, numero_bus):
    for bus in les_bus['results']:
        if bus["numerobus"] == numero_bus:
            return bus

def adresse_bus(numero_bus, client_graphhopper):
    url = "https://data.explore.star.fr/api/explore/v2.1/catalog/datasets/tco-bus-vehicules-position-tr/records?limit=-1&refine=etat%3AEn%20ligne"
    bus_en_ligne = api_position_bus(url)
    bus = recherche_bus(bus_en_ligne, numero_bus)
    coord = bus["coordonnees"]
    return client_graphhopper.latlong_to_address(
            (coord["lat"], coord["lon"])
        )


# Tests
url = "https://data.explore.star.fr/api/explore/v2.1/catalog/datasets/tco-bus-vehicules-position-tr/records?limit=-1&refine=etat%3AEn%20ligne"
bus_en_ligne = api_position_bus(url)
# pprint(bus_en_ligne)
print(len(bus_en_ligne["results"]))
print(bus_en_ligne["total_count"])

print(nb_bus_en_avance(bus_en_ligne["results"]))
pprint(ligne_de_bus_ecartensecondes(bus_en_ligne["results"]))

credentials = lecture_fichier_json("credentials.json")
gh_client = GraphHopper(api_key=credentials['clef_GH'])
print(adresse_bus(-1792824428, gh_client))
