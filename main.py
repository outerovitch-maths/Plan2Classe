from Plan2Classe import Eleve
from Plan2Classe import Dispo
from Plan2Classe import Bloc
import os

os.system('clear')

print("""
Plan2Classe ©
Permet de créer des plans de classes randomisés
""")


def selection():
    choice_1 = "1"
    i = 0
    blocs = []
    while not choice_1 == "2":
        if len(blocs) == 0:
            print("Aucun bloc crées pour le moment")
        else:
            Dispo(blocs).afficher_disposition()
            print("\n")
        print("""
        (1) Ajouter un bloc
        (2) Imprimer le plan de classe\n""")
        choice_1 = input("Que voulez-vous faire ? ")
        if choice_1 == "1":
            i = i+1
            print(f"Caractéristiques du Bloc {i} :\n")
            rang = input("Nombre de rangées : ")
            tables = input("Nombre de tables par rangées : ")
            bloc_i = Bloc(rang, tables)
            blocs.append(bloc_i)
            os.system('clear')
        elif choice_1 == "2":
            print("En cours......")
        else:
            print("Choix impossible")


selection()
# e1 = Eleve('Bob', 'Bool', 'M', 3)
# print(e1.nom)
# print(e1.prenom)
# print(e1.genre)
# print(e1.attitude)
