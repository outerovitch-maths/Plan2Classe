class Eleve:
    """
    Attributs : nom, prenom, genre, attitude (0=neutre, 1=travailleur, 2=bavard, 3=très bavard)
    """

    def __init__(self, nom, prenom, genre, attitude):
        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.attitude = attitude

        self.validation_genre()
        self.validation_attitude()

    def validation_genre(self):
        if not self.genre == "M" and not self.genre == "F":
            raise ValueError("Le genre doit être 'F' ou 'M'")

    def validation_attitude(self):
        if not isinstance(self.attitude, int) or not self.attitude in [0, 1, 2, 3]:
            raise ValueError("L'attitude doit être un entier 0<a<3")
