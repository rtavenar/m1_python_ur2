---
title : "TD2 : Les fonctions"
language: fr
author: "Xavier André & Romain Tavenard"
rights: "Creative Commons CC BY-NC-SA"
---

# Préambule

Comme pour le TD précédent, et comme pour tous les TD ce semestre, votre code pour ce TD devra se trouver dans un seul fichier, cette fois nommé `TD2_Fonctions.py` et stocké dans le même répertoire `M1_S1_Python`.
La structure de ce fichier devra être la suivante :

```python
# Section 1 : Imports de module

# Section 2 : Définition de fonctions

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
```

# Exercices indépendants

1. Écrire une fonction `table_multiplication` qui prenne pour argument une base, un multiplicateur de début et un autre de fin et affiche la table de multiplication de cette base entre les deux bornes fournies. Par exemple `table_multiplication(5, 4, 7)` affichera une sortie de la forme :

```
5*4=20
5*5=25
5*6=30
5*7=35
```

> L'écrivain arabe Asaphad rapporte, en effet, que Sessa, fils de Daher, imagina le jeu des échecs, où le roi, quoique la pièce la plus importante, ne peut faire un pas sans le secours de ses sujets les pions, dans le but de rappeler au monarque indien Scheran les principes de justice et d'équité avec lesquels il devait gouverner. Scheran, enchanté d'une leçon donnée d'une manière si ingénieuse, promit à l'inventeur de lui donner tout ce qu'il voudrait pour sa récompense. Celui-ci répondit : "Que Votre Majesté daigne me donner un grain de blé pour la première case de l'échiquier, deux pour la seconde, quatre pour la troisième, et ainsi de suite, en doublant jusqu'à la soixante-quatrième case."
> 
> Édouard Lucas, L'arithmétique amusante, Blanchard 1974

2. Écrire une fonction permettant de calculer le nombre d'années de production qu'il faudrait pour garnir l'échiquier (Indications : Masse d'un grain = 0,035 g ;  Production annuelle = 650 millions de tonnes). Les noms des variables doivent être parlants et vous devrez conserver la trace du test de votre fonction dans votre script.

3. Écrire une fonction qui prend en entrée trois entiers format une date : `jour`, `mois` et `annee` et qui retourne la date du lendemain sous la forme de trois entiers. Vous pourrez réutiliser des fonctions définies dans le TD1 : pour cela, copiez-collez le code de ces fonctions (mais pas les tests correspondants).

# Du cas général au cas particulier

1. **En utilisant la fonction codée à la première question de ce TD**, écrire une fonction `table_multiplication_usuelle` qui prenne pour argument une base et affiche la table de multiplication de cette base (pour des multiplicateurs allant donc de 1 à 10). 
Par exemple `table_multiplication_usuelle(5)` affichera la table de 5, soit une sortie de la forme :

```
5*1=5
5*2=10
[...]
5*10=50
```

2. Écrire une fonction qui prend en argument une chaîne de caractères `s` et une lettre `let` et retourne le nombre d'occurrences de la lettre `let` **en majuscule** dans `s`.

3. **En utilisant la fonction codée à la question précédente**, écrire une fonction qui retourne le nombre d'occurrences du caractère `"A"` dans une chaîne de caractères passée en argument.