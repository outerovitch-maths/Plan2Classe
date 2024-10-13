class Bloc:
    """Défini les attributs d'un bloc, rangs et tables"""

    def __init__(self, rang, tables):
        self.rang = rang  # Nombre de rangées dans le bloc
        self.tables = tables  # Nombre de tables par rangée

    def espace_y(self):
        """Calcule le nombre d'espaces entre les rangs pour chaque bloc (Axe Y)"""
        return self.rang - 1

    def afficher_bloc(self):
        """Affiche les blocs."""
        print(
            f"Bloc avec {self.rang} rangées et {self.tables} tables par rangée.")


class Dispo:
    """Défini la disposition de la classe. Nombre de blocs et leurs attributs"""

    def __init__(self, blocs):
        self.blocs = blocs  # Liste des blocs

    def afficher_disposition(self):
        """Affiche la disposition de la classe"""
        for i, bloc in enumerate(self.blocs, 1):
            print(f"Bloc {i}:")
            bloc.afficher_bloc()


class Salle:
    """Gère les calculs globaux de la salle"""

    def __init__(self, disposition: Dispo):
        self.disposition = disposition

    def total_tables(self):
        """Compte le nombre de tables dans la salle"""
        total = 0
        for bloc in self.disposition.blocs:
            total += bloc.rang * bloc.tables
        return total

    def largeur(self):
        """Trouve le nombre total de tables sur l'axe X"""
        largeur = 0
        for bloc in self.disposition.blocs:
            largeur += bloc.tables
        return largeur

    def hauteur(self):
        """Trouve le nombre maximum de rangées (Axe Y)"""
        max_hauteur = 0
        for bloc in self.disposition.blocs:
            if bloc.rang > max_hauteur:
                max_hauteur = bloc.rang
        return max_hauteur

    def espace_x(self):
        """Trouve le nombre d'espaces entre les blocs (Axe X)"""
        return len(self.disposition.blocs) - 1

    def espace_y(self):
        """Trouve le nombre d'espaces entre les blocs (Axe X)"""
        max_espace_y = 0
        for bloc in self.disposition.blocs:
            if bloc.espace_y() > max_espace_y:
                max_espace_y = bloc.espace_y()
        return max_espace_y


# Exemple d'utilisation
bloc_1 = Bloc(rang=4, tables=2)
bloc_2 = Bloc(rang=4, tables=2)
bloc_3 = Bloc(rang=4, tables=2)
bloc_4 = Bloc(rang=4, tables=2)
blocs = [bloc_1, bloc_2, bloc_3, bloc_4]

disposition = Dispo(blocs)
