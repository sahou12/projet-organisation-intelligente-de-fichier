import os
import shutil
from classifieur_ai import predire_categorie
from pdfminer.high_level import extract_text as extract_text_pdf
from docx import Document  # pip install python-docx

def lire_contenu_fichier(chemin_fichier):
    _, extension = os.path.splitext(chemin_fichier)
    extension = extension[1:].lower()
    try:
        if extension == "txt":
            with open(chemin_fichier, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read(500).lower()
        elif extension == "pdf":
            return extract_text_pdf(chemin_fichier, maxpages=1).lower()
        elif extension == "docx":
            try:
                document = Document(chemin_fichier)
                texte_docx = ""
                for paragraph in document.paragraphs:
                    texte_docx += paragraph.text + "\n"
                return texte_docx[:500].lower()
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier DOCX {chemin_fichier}: {e}")
                return None
        else:
            return None
    except Exception as e:
        print(f"Erreur lors de la lecture de {chemin_fichier}: {e}")
        return None

def grouper_et_trier_fichiers(dossier):
    resultats_tri = {}

    for nom_fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, nom_fichier)
        if os.path.isfile(chemin_complet):
            _, extension = os.path.splitext(nom_fichier)
            extension = extension[1:].lower()
            categorie_predite = None

            if extension in ["jpg", "jpeg", "png", "gif"]:
                categorie = "Images"
            elif extension in ["mp4", "avi", "mov"]:
                categorie = "Vidéos"
            elif extension in ["mp3", "wav", "aac"]:
                categorie = "Audio"
            elif extension in ["txt", "pdf", "docx"]:
                contenu = lire_contenu_fichier(chemin_complet)
                if contenu:
                    categorie_predite = predire_categorie(contenu)
                categorie = categorie_predite if categorie_predite else "Non_Classifié"
            else:
                categorie = "Autres_Fichiers"

            if categorie not in resultats_tri:
                resultats_tri[categorie] = []
            resultats_tri[categorie].append(chemin_complet)

    return resultats_tri

def deplacer_fichiers_par_categorie(resultats_tri, dossier_base):
    for categorie, fichiers in resultats_tri.items():
        chemin_categorie = os.path.join(dossier_base, categorie)
        os.makedirs(chemin_categorie, exist_ok=True)
        for chemin_fichier in fichiers:
            nom_fichier = os.path.basename(chemin_fichier)
            nouveau_chemin = os.path.join(chemin_categorie, nom_fichier)
            try:
                shutil.move(chemin_fichier, nouveau_chemin)
                print(f"✅ {nom_fichier} déplacé vers {categorie}/")
            except Exception as e:
                print(f"⚠️ Erreur déplacement {nom_fichier} : {e}")

if __name__ == "__main__":
    dossier_a_trier = input("📂 Entrez le chemin du dossier à trier : ").strip()
    if not os.path.isdir(dossier_a_trier):
        print("❌ Dossier introuvable.")
    else:
        resultats = grouper_et_trier_fichiers(dossier_a_trier)
        deplacer_fichiers_par_categorie(resultats, dossier_a_trier)
        print("🎉 Tri terminé.")
