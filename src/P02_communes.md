---
title : "Projet Week-end"
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

# Le problème

Des amis souhaitent se retrouver pour passer un week-end ensemble. 
Ils comptent pour cela louer un gîte mais, n'habitant pas tous au même endroit, se demandent dans quelle commune louer ce gîte.
Vous devez écrire un programme Python qui leur permette de se décider sur le lieu de location, en respectant les contraintes suivantes :

* le gîte devra se trouver sur une commune de plus de 20 000 habitants ;
* le gîte devra se trouver dans l'un des départements suivants : Ille-et-Vilaine (35), Mayenne (53), Côtes-d'Armor (22), Sarthe (72) ou Morbihan (56) ;
* les adresses des amis peuvent être obtenues via une API dont l'URL est la suivante : <https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis>.

Les amis, soucieux de l'avenir de leur planète, se sont mis d'accord pour utiliser le vélo comme unique moyen de transport entre leur domicile et le gîte.
Ils se sont aussi mis d'accord pour choisir un gîte qui minimise le temps de trajet maximal, c'est-à-dire le temps de trajet de l'ami qui devra passer le plus de temps sur son vélo pour aller de chez lui au gîte.

Vous ne devrez pas vous assurer de l'existence d'un gîte sur la commune que vous aurez sélectionnée : il s'agit donc uniquement de trouver la commune, parmi celles qui vérifient les contraintes ci-dessus, qui minimise le critère énoncé ci-dessus.

Il vous revient de trouver les sources de données _Open Data_ nécessaires à la réalisation de ce projet, sachant que ces sources de données doivent pouvoir s'interroger via une API, pour que le rendu du script Python seul suffise à l'exécution de votre programme (pas de dépôt de fichier de données supplémentaire autorisé).