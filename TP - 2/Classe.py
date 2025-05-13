import re, datetime

class client():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.mail__= None
        self.tel__= None
        self.cp__= None
        self.bthd__= None
        
    def verification_mail(self, mail):
        while not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail):
            print(f'Erreur: votre adresse mail "{mail}" est invalide.')
            mail = input('Adresse mail :')
        self.mail__ = mail
    
    def verification_tel(self, tel):
        while not re.match(r'[0][1-9]+\.[0-9][0-9]+\.[0-9][0-9]+\.[0-9][0-9]+\.[0-9][0-9]', tel):
            print(f'Erreur: votre numéro de téléphone "{tel}" est invalide.')
            tel = input('Numéro de téléphone :')
        self.tel__ = tel
    
    def verification_cp(self, cp):
        while not re.match(r'[0-8][0-9][0-9][0-9][0-9]|9[0-5][0-9][0-9][0-9]', cp):
            print(f'Erreur: votre Code postal "{cp}" n\'existe pas.')
            cp=input('Code Postal :')
        self.cp__=cp
        
    def verification_bthd(self, bthd):
        while not datetime.datetime.strptime(bthd, "%d/%m/%Y"):
            print(f'Erreur: votre date de naissance {self.bthd__} ne correspond pas au format jj/mm/aaaa')
            self.bthd__=input('Date de naissance :')
        self.bthd__=bthd