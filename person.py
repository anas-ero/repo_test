class Person:
    def __init__(self, nom, prenom, ville):
        self.nom = nom
        self.prenom = prenom
        self.ville = ville

    def afficher(self):
        return f"{self.nom}     {self.prenom}     {self.ville}"
    
    