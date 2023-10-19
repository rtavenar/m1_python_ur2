---
title : "Projet Cluedo"
language: fr
author: "Xavier André & Romain Tavenard"
rights: "Creative Commons CC BY-NC-SA"
---

# Préambule

Pour ce projet, vous devrez travailler par groupes de 2 ou 3 et votre rendu se fera sous la forme d'un fichier Python.
Ce fichier devra être nommé `P02.py` et contenir, sous la forme de commentaires dans l'en-tête du fichier :

* les noms et numéros étudiant de tous les membres du groupe ;
* en cas d'usage de ChatGPT ou d'un autre assistant, un lien vers la session utilisée pour s'aider (lien "Share Chat" en haut à droite de la fenêtre ChatGPT)

comme dans l'exemple suivant :

```python
# 22000002 Paul Machin
# 22000227 Yolène Truc
# ChatGPT https://chat.openai.com/share/04760567-235e-40a4-b60d-330877b57e

# Section 1 : les imports
# [...]
```

La date limite de rendu est indiquée sur CURSUS dans l'espace de dépôt.
Les fichiers déposés sur CURSUS ne devront **surtout pas** contenir votre clé d'API GraphHopper. 
Celle-ci devra être lue par votre programme dans un fichier `credentials.json` (que vous ne fournirez pas pour ne pas divulguer votre clé d'API) au format :

```json
{
  "graphhopper": {
    "API_KEY": "..."
  }
}
```

# L'enquête

Le 16 Octobre 2023, à 16h23, un crime a été commis à l'UFR Sciences Sociales de l'Université de Rennes 2.
Trois suspects ont été ciblés grâce aux premiers éléments de l'enquête.
Votre rôle sera de déterminer si leur activité sur les reseaux sociaux est cohérente ou non avec leur présence sur les lieux du crime à l'heure dite.

Concrètement, votre programme devra afficher, pour chaque suspect listé dans le fichier [`suspects.csv`](https://raw.githubusercontent.com/rtavenar/m1_python_ur2/main/modules_fournis/suspects.csv), son `ID`, son adresse e-mail et s'il est possible ou non, d'après les traces laissées sur les réseaux sociaux, qu'il ait commis le crime.

Pour mener à bien votre mission, vous pourrez utiliser (outre votre intelligence) :

* le _package_ `graphh` pour calculer des temps de trajet théoriques (notez qu'on ne sait pas si les suspects se sont déplacés à pied, en vélo ou encore en voiture : il vous faudra envisager toutes les possibilités),
* le _package_ `datetime` pour la gestion des dates et des temps écoulés entre deux dates (un chapitre y est dédié dans le poly, n'hésitez pas à vous y référer).

De plus, pour simuler les posts Twitter et Snapchat, vous utiliserez les données disponibles à ces adresses :

* <https://my-json-server.typicode.com/rtavenar/fake_api/twitter_posts>
* <https://my-json-server.typicode.com/rtavenar/fake_api/snapchat_posts>
