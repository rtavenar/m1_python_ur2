from graphh import GraphHopper
import json
import requests
import pprint

list_dept = [35, 22, 53, 56, 72]
url_pop = ("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/population-francaise-communes/records?" + 
           f"where=population_totale%20%3E%2020000%20AND%20code_departement%20IN%20({'%22' + '%22%2C%22'.join(map(str, list_dept)) + '%22'})%20" + 
           "&limit=20&refine=annee_recensement%3A%222016%22")
pop_brut = requests.get(url_pop)
communes = pop_brut.json()["results"]

url_gps = "https://www.data.gouv.fr/fr/datasets/r/521fe6f9-0f7f-4684-bb3f-7d3d88c581bb"
gps_brut = requests.get(url_gps)
gps_communes = gps_brut.json()["cities"]

# pprint.pprint(gps_communes["cities"][0])

gps_communes_formatte = {}
for gps_c in gps_communes:
    try:
        gps_communes_formatte[gps_c['insee_code']] = {"lat": float(gps_c['latitude']), "lon": float(gps_c['longitude'])}
    except:
        pass

populations = {}
for c in communes:
    populations[c['code_insee_commune']] = {
        "population": c['population_totale'],
        "nom": c['nom_de_la_commune'],
        "gps": gps_communes_formatte[c['code_insee_commune']]
    }

pprint.pprint(populations)