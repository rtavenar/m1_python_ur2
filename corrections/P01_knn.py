import math
import numpy as np
from scipy.spatial.distance import cdist

from P01_utils import lire_donnees


def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=seq.__getitem__)


def dist(Xi, Xj):
    d = len(Xi)
    assert d == len(Xj)
    s = 0.
    for di in range(d):
        s += (Xi[di] - Xj[di]) ** 2
    return math.sqrt(s)


def indice_k_plus_proches(Xi, X, k):
    distances = [dist(Xi, Xj) for Xj in X]
    indices = argsort(distances)
    return indices[:k]


def plus_frequent(liste):
    dico_valeurs = {}
    for v in liste:
        dico_valeurs[v] = dico_valeurs.get(v, 0) + 1
    valeur_max_freq = None
    max_freq = -1
    for val, count in dico_valeurs.items():
        if count > max_freq:
            max_freq = count
            valeur_max_freq = val
    return valeur_max_freq


def k_plus_proches_voisins_list(X_train, y_train, X_test, k=1):
    predicted_labels = []
    for Xi in X_test:
        indices = indice_k_plus_proches(Xi, X_train, k)
        liste_labels = [y_train[i] for i in indices]
        predicted_labels.append(plus_frequent(liste_labels))
    return predicted_labels


def k_plus_proches_voisins_npy(X_train, y_train, X_test, k=1):
    all_distances = cdist(X_test, X_train)
    all_knn_indices = np.argsort(all_distances, axis=1)[:, :k]
    all_knn_labels = y_train[all_knn_indices]
    count_F = np.sum(all_knn_labels == "F", axis=1)
    predicted_labels = np.empty(count_F.shape, dtype=y_train.dtype)
    predicted_labels[count_F > k / 2] = "F"
    predicted_labels[count_F <= k / 2] = "H"
    return predicted_labels


# Données
X_train, y_train = lire_donnees(100)
X_test, y_test = lire_donnees(10)

# Version 1 : pur python
y_pred_list = k_plus_proches_voisins_list(X_train, y_train, X_test, k=3)

# Version 2 : numpy
y_pred_npy = k_plus_proches_voisins_npy(X_train, y_train, X_test, k=3)

# Affichage
for yi, yi_pred_list, yi_pred_npy in zip(y_test, y_pred_list, y_pred_npy):
    print(f"Vraie classe : {yi}, classe prédite (version liste) : {yi_pred_list}, classe prédite (version numpy): {yi_pred_npy}")
