class Filliere:
    def __init__(self, codeF, nomF):
        self.codeF = codeF
        self.nomF = nomF
        self.list = []

    def ajouter(self, groupe):
        self.list.append(groupe)

    def afficher(self):
        return f"{self.nomF}"
    
    def afficherGroupe(self):
        for groupe in self.list:
            print(groupe.codeG)

    def listGroupe(self, codeG):
        print("==============================")
        print(f"Filliere              : {self.nomF}")
        for groupe in self.list:
            if groupe.codeG.lower() == codeG.lower():
                groupe.listStudent()
                break