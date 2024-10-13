from PIL import Image
from eleve import Eleve
from disposition import Bloc
from disposition import Dispo
from disposition import Salle


class Myimage:
    """Défini les attributs de l'image, hauteur, largeur"""

    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur  # Hauteur de l'image
        self.largeur = largeur  # Largeur de l'image

    def output_image(self):
        """Crée une image blanche"""
        image = Image.new('RGB', (self.hauteur, self.largeur), (255, 255, 255))
        image.save('output.png')
        image.show('output.png')


bloc_1 = Bloc(rang=4, tables=2)
bloc_2 = Bloc(rang=5, tables=2)
bloc_3 = Bloc(rang=4, tables=3)
bloc_4 = Bloc(rang=3, tables=2)
blocs = [bloc_1, bloc_2, bloc_3, bloc_4]

disposition = Dispo(blocs)
salle = Salle(disposition)

# Définir les dimensions de l'image
margins = 5
h = salle.hauteur() * 5 + 2 * margins + salle.espace_y() * 5
l = salle.largeur() * 10 + 2 * margins + salle.espace_x() * 5

# Créer l'image avec la classe Myimage
image = Myimage(l, h)

# Générer l'image blanche
image.output_image()
