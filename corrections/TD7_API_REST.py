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

def nb_bus_en_avance(les_bus):
    nombre_bus_en_avance = 0
    for bus in les_bus['records']:
        if bus["fields"]["ecartsecondes"] > 0:
            nombre_bus_en_avance+=1
    return nombre_bus_en_avance

def ligne_de_bus_ecartensecondes(les_bus):
    dico_ligne_de_bus_ecartensecondes = {}
    for bus in les_bus['records']:
        nomcourtligne = bus["fields"]["nomcourtligne"]
        ecartensecondes = bus["fields"]["ecartsecondes"]
        if nomcourtligne not in dico_ligne_de_bus_ecartensecondes.keys():
            dico_ligne_de_bus_ecartensecondes[nomcourtligne] = [ecartensecondes]
        else:
            dico_ligne_de_bus_ecartensecondes[nomcourtligne].append(ecartensecondes)
    return dico_ligne_de_bus_ecartensecondes

def lecture_fichier_json(nom_fic):
    with open(nom_fic, 'rt', encoding='utf8') as obj_fic:
        return json.load(obj_fic)

def recherche_bus(les_bus, numero_bus):
    for bus in les_bus['records']:
        if bus["fields"]["numerobus"] == numero_bus:
            return bus

def adresse_bus(numero_bus, client_graphhopper):
    url = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-vehicules-position-tr&q=&rows=-1&facet=numerobus&facet=nomcourtligne&facet=destination&facet=ecartsecondes&refine.etat=En+ligne"
    bus_en_ligne = api_position_bus(url)
    bus = recherche_bus(bus_en_ligne, numero_bus)
    coord = bus["geometry"]["coordinates"]
    return client_graphhopper.latlong_to_address(coord[::-1])


# Tests
url = "https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-vehicules-position-tr&q=&rows=-1&facet=numerobus&facet=nomcourtligne&facet=destination&facet=ecartsecondes&refine.etat=En+ligne"
bus_en_ligne = api_position_bus(url)
#pprint(bus_en_ligne)

print(nb_bus_en_avance(bus_en_ligne))
pprint(ligne_de_bus_ecartensecondes(bus_en_ligne))

credentials = lecture_fichier_json("credentials.json")
gh_client = GraphHopper(api_key=credentials['clef_GH'])
print(adresse_bus(-1951987696, gh_client))
