---
title : "TD4 : Les dictionnaires et les _sets_"
language: fr
author: "Xavier André & Romain Tavenard"
rights: "Creative Commons CC BY-NC-SA"
---

# Préambule

Comme pour tous les TD ce semestre, votre code pour ce TD devra se trouver dans un seul fichier, cette fois nommé `TD4_Dicos.py` et stocké dans le même répertoire `M1_S1_Python`.
La structure de ce fichier devra être la suivante :

```python
# Section 1 : Imports de module

# Section 2 : Définition de fonctions

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
```

# Les dictionnaires

1. Écrire une fonction `normalise_texte` qui retourne la chaîne minuscule du texte passé en paramètre, avec ses lettres accentuées ou cédillées converties en lettres normales et les ligatures séparées (`"ZÈBRE"` $\Rightarrow$ `"zebre"` , `"bœuf"` $\Rightarrow$ `"boeuf"`).
Voici la liste des caractères spéciaux en français :


    ```python
    "À", "Â", "Æ", "Ç", "É", "È", "Ê", "Ë", "Î", "Ï", "Ô", "Œ", "Ù", "Û", "Ü", "Ÿ", "à", "â", "æ", "ç", "é", "è", "ê", "ë", "î", "ï", "ô", "œ", "ù", "û", "ü", "ÿ"
    ```

    Tester votre fonction avec la chaîne suivante : "Dès Noël où un zéphyr haï me vêt de glaçons würmiens, je dîne d'exquis rôtis de bœuf au kir à l'aÿ d'âge mûr et cætera !"

2. Écrire une fonction qui à partir d'une chaîne de caractères passée en argument renvoie un dictionnaire associant chaque mot à son nombre d'occurrences dans la chaîne.

3. En utilisant la fonction codée à la question précédente, écrire une fonction qui à partir d'une chaîne de caractères passée en argument retourne le mot le plus fréquent dans cette chaîne.

4. On dispose d’un dictionnaire associant à des noms de commerciaux d'une société le nombre de ventes qu'ils/elles ont réalisées. Par exemple :

    ```python
    ventes={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}
    ```

    * Écrivez une fonction qui prend en entrée un tel dictionnaire et renvoie le nombre total de ventes dans la société.
    * Écrivez une fonction qui prend en entrée un tel dictionnaire et renvoie le nom du vendeur ayant réalisé le plus de ventes. Si plusieurs vendeurs sont ex-æquo sur ce critère, la fonction devra retourner le nom de l'un d’entre eux.

# Les _sets_

1. Reprendre la question 6. du TD précédent et implémenter une nouvelle fonction `liste_triee_sans_doublon` qui utilisera, cette fois, la fonction `set()`.

2. Écrire une fonction qui prend en entrée une liste et retourne le nombre d'éléments distincts de cette liste (BONUS si votre fonction tient en une ligne).

3. Un pangramme est une phrase qui comporte les 26 lettres de l'alphabet, comme :

    * `"Portez ce vieux whisky au juge blond qui fume"` ;
    * `"J'ai vu un punk afghan et deux clowns aux zygomatiques incroyables"`

    Écrire une fonction `pangramme` qui, à partir d'une phrase passée en paramètre, retourne un booléen indiquant si cette phrase est un pangramme.