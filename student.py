from person import Person


class Student(Person):
    def __init__(self, nom, prenom, ville, notes,):
        super().__init__(nom, prenom, ville)
        self.moyenne= (notes[0] + notes[1])/3

    def resultat(self):
        if self.moyenne >= 10:
            return "Admis"
        else:
            return "Non Admis"
    
    def afficher(self):
        return f"{super().afficher()}     {self.moyenne:.2f}     {self.resultat()}"
    
    