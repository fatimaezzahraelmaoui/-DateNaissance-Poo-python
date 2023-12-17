
class DateNaissance:
     def __init__(self,jour,mois,année):
        self.__Jour = jour
        self.__Mois = mois
        self.__Année = année
    
def getJour(self):
        return self.__Jour
def setJour(self,jour):
        self.__Jour = jour
def getMois(self):
        return self.__Mois
def setMois(self,mois):
        self.__Mois = mois
def getAnnée(self):
        return self.__Année
def setAnnée(self,année):
        self.__Année = année
    
def ToString(self):
    return(str(self.__Jour)+"/"+str(self.__Mois)+"/"+str(self.__Année))

class Personne(DateNaissance):
    def __init__(self,jour,mois,année,nom,prenom,datenaissance):
        super().__init__(jour,mois,année)
        self.__Nom = nom
        self.__Prenon = prenom
        self.Date = datenaissance
        
def AfficherInfo(self):
    print("le nom est :",self.__Nom)
    print("le prenom est :",self.__Prenom)
    print("jour est :",self.__Jour)
    print("mois est :",self.__Mois)
    print("l'Année est :",self.__Année)
    print("votre date de naissance est :",self.__Date)
    
class Employe(Personne):
    def __init__(self,jour,mois,année,nom,prenom,datenaissance,salaire):
        super().__init__(jour,mois,année,nom,prenom,datenaissance)
        self.__Nom = nom
        self.__Prenon = prenom
        self.__Date = datenaissance
        self.Salaire = salairedef 

def AfficherInfo(self):
    print("le nom est :",self.__Nom)
    print("le prenom est :",self.__Prenom)
    print("jour est :",self.__Jour)
    print("mois est :",self.__Mois)
    print("l'Année est :",self.__Année)
    print("votre date de naissance est :",self.__Date)
    print("le salaire est :",self.Salaire)
    




D1= DateNaissance(31,11,2021)
print(D1.ToString())

EM1 = Employe(25,6,2023,"kawtar","soltane","2/7/2003",23800)
#EM2 = Eleve("sara","amrani",20,"bac",17)
#EM3 = Eleve("kawtar","khalil",23,"infirmiére",17)
print(S1.AfficherInfo())
    
    
    
    
        
    