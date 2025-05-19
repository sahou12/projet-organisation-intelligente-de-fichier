import json
import os

fichier_commentaires = "commentaires.json"

def ajouter_commentaire(utilisateur, fichier, commentaire):
    if os.path.exists(fichier_commentaires):
        with open(fichier_commentaires, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    if fichier not in data:
        data[fichier] = []

    data[fichier].append({"utilisateur": utilisateur, "commentaire": commentaire})

    with open(fichier_commentaires, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("✅ Commentaire ajouté.")

def verifier_acces(utilisateur, fichier):
    # Simplification : tous les utilisateurs ont accès à tout
    return True
