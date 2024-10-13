from PIL import Image, ImageDraw, ImageFont

# Dimensions de l'image
largeur, hauteur = 200, 100
marge = 10

# Crée une image blanche
image = Image.new("RGB", (largeur, hauteur), "white")
draw = ImageDraw.Draw(image)

# Définition des dimensions du rectangle avec des marges
x0, y0 = marge, marge
x1, y1 = largeur - marge, hauteur - marge

# Dessine le rectangle noir
draw.rectangle([x0, y0, x1, y1], outline="black", width=3)

# Charge une police de caractères
try:
    # Utilise une police par défaut si tu n'as pas de police spécifique
    font = ImageFont.load_default()
except IOError:
    font = ImageFont.load_default()

font_size = 15
font = ImageFont.truetype(r"Arial.ttf", font_size)
# Position et texte à afficher
texte = "Nom Prénom"
textwidth = draw.textlength(texte, font)
textheight = font_size
text_x = (largeur - textwidth) // 2
text_y = (hauteur - textheight) // 2

# Dessine le texte
draw.text((text_x, text_y), texte, fill="black", font=font)

# Enregistre l'image
image.save("image_rectangle.png")

# Affiche l'image (facultatif, si tu veux la voir immédiatement)
image.show()
