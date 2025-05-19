import sys
import os

# Ajout du dossier courant dans sys.path pour les imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from recherche import recherche_mot_cle  # CHANGÉ ICI
from gestion_utilisateurs import verifier_acces, ajouter_commentaire  # Si ce fichier existe toujours

def lancer_recherche(dossier):
    mot = input("Entrez un mot-clé à rechercher : ").strip()
    fichiers = recherche_mot_cle(dossier, mot)

    if fichiers:
        print("Fichiers trouvés :")
        for f in fichiers:
            print(" -", f)
    else:
        print("Aucun fichier trouvé avec ce mot-clé.")

def menu_principal():
    while True:
        print("\n=== Projet de classement intelligent de documents ===")
        print("1. Rechercher un document")
        print("2. Ajouter un commentaire")
        print("3. Quitter")
        choix = input("Choisissez une option : ").strip()

        if choix == "1":
            dossier = "test_docs"  # Dossier où tu mets tes fichiers à rechercher
            if os.path.exists(dossier) and os.path.isdir(dossier):
                lancer_recherche(dossier)
            else:
                print(f"Le dossier '{dossier}' n'existe pas. Merci de le créer ou de changer ce chemin.")

        elif choix == "2":
            utilisateur = input("Nom de l'utilisateur : ").strip()
            fichier = input("Nom du fichier : ").strip()
            commentaire = input("Votre commentaire : ").strip()
            ajouter_commentaire(utilisateur, fichier, commentaire)

        elif choix == "3":
            print("Au revoir !")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu_principal()

