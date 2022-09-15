import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)


def make_blobs(n_samples, centers, cluster_std):
    # Version simplifiée de la fonction `make_blobs` de scikit-learn
    centers = np.array(centers)
    n_features = centers.shape[1]
    n_centers = centers.shape[0]

    X = []
    y = []

    n_samples_per_center = [int(n_samples // n_centers)] * n_centers
    for i in range(n_samples % n_centers):
        n_samples_per_center[i] += 1

    for i, (n, std) in enumerate(zip(n_samples_per_center, cluster_std)):
        X.append(np.random.normal(loc=centers[i], scale=std,
                                  size=(n, n_features)))
        y += [i] * n

    X = np.concatenate(X)
    y = np.array(y)

    return X, y


def lire_donnees(n_individus):
    # Moyennes issues de https://liguecontrelobesite.org/actualite/taille-poids-et-tour-de-taille-photographie-2020-des-francais/
    X, y = make_blobs(n_samples=n_individus,
                      centers=[[164, 64], [177, 79]],
                      cluster_std=[[20, 5], [20, 5]])
    y_str = np.empty(y.shape, dtype=str)
    y_str[y == 0] = "F"
    y_str[y == 1] = "H"
    return X, y_str


def visualiser_donnees(X, y, X_test=None, nom_fichier=None):
    plt.figure()
    for sexe in ["F", "H"]:
        plt.scatter(X[y == sexe, 0], X[y == sexe, 1], label=sexe)
    if X_test is not None:
        plt.scatter(X_test[:, 0], X_test[:, 1], marker="x", color="k")
    plt.xlabel("Taille")
    plt.ylabel("Poids")
    plt.legend(loc="upper left")
    if nom_fichier is not None:
        plt.savefig(nom_fichier)
    else:
        plt.show()


if __name__ == "__main__":
    X_train, y_train = lire_donnees(100)
    X_test, y_test = lire_donnees(10)
    visualiser_donnees(X_train, y_train, X_test, "dataset.pdf")
    