class Bloc:
    """Défini les attributs d'un bloc, rangs et tables"""

    def __init__(self, rang, tables):
        self.rang = rang  # Nombre de rangées dans le bloc
        self.tables = tables  # Nombre de tables par rangée

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

    def compte_tables(self):
        """Compte le nombre de tables dans la salle"""
        compte = 0
        for bloc in self.blocs:
            compte = compte+bloc.rang*bloc.tables
        return compte

    def hauteur_salle(self):
        """Trouve le nombre maximum de rangées"""
        compte = 0
        for bloc in self.blocs:
            if bloc.rang > compte:
                compte = bloc.rang
        return compte

    def largeur_salle(self):
        """Trouve le nombre maximum de rangées"""
        compte = 0
        for bloc in self.blocs:
            compte = bloc.tables+compte
        return compte


# Exemple d'utilisation
bloc_1 = Bloc(rang=4, tables=2)
bloc_2 = Bloc(rang=4, tables=2)
bloc_3 = Bloc(rang=4, tables=2)
bloc_4 = Bloc(rang=4, tables=2)
blocs = [bloc_1, bloc_2, bloc_3, bloc_4]
espaces = len(blocs)-1

disposition = Dispo(blocs)

# print(disposition.afficher_disposition())
# print(f"Total de tables : {disposition.compte_tables()}")
# print(f"Hauteur salle : {disposition.hauteur_salle()}")
# print(f"Largeur salle : {disposition.largeur_salle()}")
# print(espaces)
