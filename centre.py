class Centre:
    def __init__(self,nomC, codeC):
        self.nomC = nomC
        self.codeC = codeC
        self.list = []
    
    def ajouter(self, filiere):
        self.list.append(filiere)

    
    def listdefiliere(self):
        print("==========================")
        print(f"Centre         : {self.codeC}")
        for filiere in self.list:
            print(filiere.afficher())

    
    def groupeFiliere(self,codeF):
        for filiere in self.list:
            if filiere.codeF.lower() == codeF.lower():
                filiere.afficherGroupe()
                break