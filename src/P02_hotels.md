---
title : "Projet Week-end"
language: fr
author: "Xavier André & Romain Tavenard"
rights: "Creative Commons CC BY-NC-SA"
---

# Préambule

Pour ce projet, vous devrez travailler par groupes de 2 ou 3 et votre rendu se fera sous la forme d'un fichier Python.
Ce fichier devra être nommé `P02.py` et contenir, sous la forme de commentaires dans l'en-tête du fichier les noms et numéros étudiant de tous les membres du groupe comme dans l'exemple suivant :

```python
# 22000002 Paul Machin
# 22000227 Yolène Truc

# Section 1 : les imports
# [...]
```

La date limite de rendu est indiquée sur CURSUS dans l'espace de dépôt.

# Le problème

Des amis souhaitent se retrouver pour passer un week-end ensemble. 
Ils comptent se retrouver dans la ville de l'un d'entre eux.
Chacun disposant de logement trop petit, les autres amis devront louer des chambres d'hôtel dans cette ville.
Vous devez écrire un programme Python qui leur permette de lister les hôtels existants, en utilisant les ressources suivantes :

* les adresses des amis peuvent être obtenues via une API dont l'URL est la suivante : <https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis> ;
* les hôtels peuvent être obtenus via l'API `data.gouv.fr` via le lien <https://tabular-api.data.gouv.fr/api/resources/3ce290bf-07ec-4d63-b12b-d0496193a535/data/>.
Le programme devra afficher la liste des hôtels disponibles dans la ville de chacun des amis, en indiquant pour chaque hôtel son nom, son adresse et son nombre d'étoiles.