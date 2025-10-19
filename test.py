from student import Student
from groupe import Groupe
from filliere import Filliere
from centre import Centre

isag=Centre("INSITITU SPECIALISE D ART GRAPHIC","ISAG")


dev = Filliere("DEV","Developpement Digital")
info = Filliere("INFO","Infographie")
des = Filliere("DES","Design Digital")

isag.ajouter(dev)
isag.ajouter(info)
isag.ajouter(des)


dev101 = Groupe("DEV101","1ere Annee Groupe 1")
dev102 = Groupe("DEV102","1ere Annee Groupe 1")

dev.ajouter(dev101)
dev.ajouter(dev102)

s1 = Student("Sandaoui ","Anas   ","Casablanca",[12, 29])
s2 = Student("SDHJH    ","GRR    ","Casablanca",[12, 29])
s3 = Student("nassi    ","khal   ","Casablanca",[16, 30])
s4 = Student("reve     ","pheonix","Casablanca",[1, 20])
s5 = Student("sage     ","ghabi  ","Casablanca",[19, 22])
s6 = Student("ghadi    ","leila  ","Casablanca",[12, 29])
s7 = Student("babakhali","Ouassim","Casablanca",[17, 30])
s8 = Student("Tarik    ","Diaa   ","Casablanca",[19, 40])


dev101.ajouter(s1)
dev101.ajouter(s2)
dev101.ajouter(s3)
dev101.ajouter(s4)

dev102.ajouter(s5)
dev102.ajouter(s6)
dev102.ajouter(s7)
dev102.ajouter(s8)


isag.groupeFiliere("dev")