# from recherche_intelligente import lancer_recherche
# elif choix == "2":
#     lancer_recherche()
import os

def lancer_recherche(base):
    mot_cle = input("Entrez un mot-clé à rechercher : ").lower()
    for dossier, _, fichiers in os.walk(base):
        for fichier in fichiers:
            chemin = os.path.join(dossier, fichier)
            try:
                with open(chemin, "r", encoding="utf-8") as f:
                    contenu = f.read().lower()
                    if mot_cle in contenu:
                        print(f"🔍 Mot trouvé dans : {chemin}")
            except:
                continue
