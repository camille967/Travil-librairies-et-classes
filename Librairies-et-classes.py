class Cahier:
    def __init__(self, sujet, completion, nbPages, couleur, titre):
        self.sujet = sujet
        self.completion = completion
        self.nbPages = nbPages
        self.couleur = couleur
        self.titre = titre

    def pourcentageCompletion(self):
        nbPagesTotal = int(self.nbPages.split()[0])
        nbPagesComplete = int(self.completion.split()[0])
        pourcentage = nbPagesComplete / nbPagesTotal * 100
        print(f"Le cahier de {self.sujet} est rempli à {pourcentage}%.")

    def ouvrir(self):
        pageActuelle = int(self.completion.split()[0])
        print(f"Ouvrir le cahier {self.titre} à la page {pageActuelle}.")

cahierPhysique = Cahier("physique", "121 pages", "159 pages", "Rouge", "Trajectoires mécaniques")
cahierChimie = Cahier("chimie", "137 pages", "308 pages", "Bleu", "Option science")
cahierFrancais = Cahier("francais", "93 pages", "158 pages", "Mauve", "À toute épreuve")

cahierPhysique.ouvrir()
cahierPhysique.pourcentageCompletion()
print()
cahierChimie.ouvrir()
cahierChimie.pourcentageCompletion()
print()
cahierFrancais.ouvrir()
cahierFrancais.pourcentageCompletion()
print()



