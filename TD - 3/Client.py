"""
Propriétés à ajouter : 
  Nom (publique)
  Email (publique)
  Panier (publique)
  Mode de règlement de la commande (publique)
  Statut de la commande (privé)

Méthodes à ajouter :
  Ajouter au panier (publique)
      Référence article
      nom article
      Montant article
  
  Régler la commande (publique)
      Mode de règlement
""" 

class Client:
    def __init__(self, nom : str, email : str):
        # nom et email

        self.nom=nom
        self.email=email
        self.panier={}
        self.__statut="Vide"
    
    def ajout_panier(self, article : list):
        self.__statut="En cours"
        self.panier[article[0]]=article[1:]
        return self.nom, self.email, self.panier

    def regler_commande(self, mode_reglement):
        self.__statut="Terminée"
        prix=0
        for n in self.panier.values():
            prix+=int(n[1])*int(n[0])
        print(f'Statut de la Commande : {self.__statut}. Il vous reste à payer {prix}€.')
        

