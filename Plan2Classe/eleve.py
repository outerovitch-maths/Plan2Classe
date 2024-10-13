class Eleve:
    """
    Attributs : nom, prenom, genre, attitude
    """

    def __init__(self, nom: str, prenom: str, genre: str, attitude: int):
        """
        Paramètres :
        - nom : str, le nom de l'élève
        - prenom : str, le prénom de l'élève
        - genre : str 'M' ou 'F'
        - attitude : int (0=neutre, 1=travailleur, 2=bavard, 3=très bavard)
        """
        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.attitude = attitude

        self.validation_genre()
        self.validation_attitude()

    def validation_genre(self):
        if self.genre not in ["M", "F"]:
            raise ValueError("Le genre doit être 'F' ou 'M'")

    def validation_attitude(self):
        if not isinstance(self.attitude, int) or not self.attitude in [0, 1, 2, 3]:
            raise ValueError(
                "L'attitude doit être un entier compris entre 0 et 3")

# tests
# eleve1 = Eleve("Dupont", "Alice", "F", 2)  # Valide
# eleve2 = Eleve("Martin", "Bob", "M", 1)    # Valide

# Genre invalide, va lever une ValueError
# eleve3 = Eleve("Smith", "John", "X", 3)

# Genre de longueur > 1, va lever une ValueError
# eleve4 = Eleve("Dupont", "Alice", "Female", 2)
