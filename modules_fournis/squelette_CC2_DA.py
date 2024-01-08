import json
import datetime

# !!!
# Compléter le code ici

ev = Evenement(
    titre="Exam",
    lieu="B204",
    debut="2024-01-11T13:15",
    fin="2024-01-11T14:45"
)
print(ev)
# Sortie : <Exam | B204 | 2024-01-11 13:15:00-2024-01-11 14:45:00>
print(ev.duree)
# Sortie : 1:30:00
ma_date = datetime.datetime(2024, 1, 11, 14, 00)
print(ma_date in ev)
# Sortie : True
autre_date = datetime.datetime(2024, 1, 12, 14, 00)
print(autre_date in ev)
# Sortie : False

d = {
    "titre": "Exam (bis)",
    "lieu": "B204",
    "debut": "2024-01-31T13:15",
    "fin": "2024-01-31T14:45"
}
ev2 = EvenementDictionnaire(d)
print(ev2)
# Sortie : <Exam (bis) | B204 | 2024-01-31 13:15:00-2024-01-31 14:45:00>

a = Agenda(liste_evenements=[ev, ev2])
print(a)
# Sortie (ne pas se soucier de l'indentation, elle est mise là juste pour la lisibilité) :
# [
#    "<Exam | B204 | 2024-01-11 13:15:00-2024-01-11 14:45:00>", 
#    "<Exam (bis) | B204 | 2024-01-31 13:15:00-2024-01-31 14:45:00>"
# ]
print(a.libre(ma_date))
# Sortie: False
a01 = AgendaJSON("cal01.json")
a02 = AgendaJSON("cal02.json")
a_ensemble = a01 + a02
print(a_ensemble)
# Sortie (ne pas se soucier de l'indentation, elle est mise là juste pour la lisibilité) :
# [
#   "<CM Python | A023 | 2024-01-29 09:15:00-2024-01-29 10:15:00>",
#   "<CM Bases de données | A023 | 2024-01-29 08:15:00-2024-01-29 09:15:00>",
#   "<Cours éventuel place Hoche |  | 2024-01-29 13:45:00-2024-01-29 15:45:00>",
#   "<CM Python | A023 | 2024-01-29 09:15:00-2024-01-29 10:15:00>",
#   "<TD Python | B204 | 2024-01-29 10:30:00-2024-01-29 11:30:00>",
#   "<TD Python | B206 | 2024-01-29 11:30:00-2024-01-29 12:30:00>"
# ]