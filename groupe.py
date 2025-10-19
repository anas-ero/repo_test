class Groupe:
    def __init__(self, codeG, nomG):
        self.codeG = codeG
        self.nomG = nomG
        self.list= []
    
    def ajouter(self, student):
        self.list.append(student)

    def listStudent(self):
        print("====================================================")
        print(f"Groupe                 : {self.codeG}==============")
        print("====================================================")
        print("Nom     Prenom     ville     Moyenne     Resultat   ")
        print("====================================================")
        for student in self.list:
            print(student.afficher())
