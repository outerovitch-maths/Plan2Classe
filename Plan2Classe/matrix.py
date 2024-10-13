from disposition import Bloc, Dispo


class Matrice:
    def __init__(self, disposition: Dispo):
        """Initialise la matrice en fonction de la disposition des blocs."""
        self.disposition = disposition  # La disposition avec tous les blocs
        self.largeur_matrice = self.calculer_largeur()  # Largeur totale
        self.hauteur_matrice = self.calculer_hauteur()  # Hauteur maximale
        self.matrice = self.creer_matrice()  # Crée la matrice vide

    def calculer_largeur(self):
        """Calcule la largeur totale de la matrice."""
        return sum(bloc.tables for bloc in self.disposition.blocs)

    def calculer_hauteur(self):
        """Calcule la hauteur maximale de la matrice."""
        return max(bloc.rang for bloc in self.disposition.blocs)

    def creer_matrice(self):
        """Crée une matrice vide avec des emplacements pour chaque table."""
        return [[None for _ in range(self.largeur_matrice)] for _ in range(self.hauteur_matrice)]

    def peupler_matrice(self):
        """Peuple la matrice avec les noms des blocs et leurs tables."""
        current_col = 0  # Colonne courante pour placer les blocs

        for n, bloc in enumerate(self.disposition.blocs):
            nom_bloc = chr(65 + n)  # Nom du bloc (A, B, C, ...)
            for i in range(bloc.rang):
                for j in range(bloc.tables):
                    # Remplit la matrice avec les coordonnées
                    coord = f"{nom_bloc}{i + 1}{j + 1} : None"
                    self.matrice[i][current_col + j] = coord
            current_col += bloc.tables  # Met à jour la colonne courante

    def afficher(self):
        """Affiche la matrice avec les blocs et leurs tables."""
        for row in self.matrice:
            print(" ".join(f"{item:>5}" if item else "     " for item in row))


# Exemple d'utilisation
if __name__ == "__main__":
    bloc_1 = Bloc(rang=4, tables=2)  # Bloc A
    bloc_2 = Bloc(rang=3, tables=3)  # Bloc B
    blocs = [bloc_1, bloc_2]

    disposition = Dispo(blocs)  # Créer la disposition avec les blocs
    matrice = Matrice(disposition)  # Créer la matrice

    matrice.peupler_matrice()  # Peupler la matrice avec les noms
    matrice.afficher()  # Afficher la matrice
