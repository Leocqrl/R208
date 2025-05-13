from Classe import client

def main():
    saisie=input('Veuillez saisir les informations suivantes :')
    if saisie=='':
        nom=input('Nom :')
        prenom=input('Prénom :')
        client1=client(nom, prenom)
        mail=input('Email :')
        client1.verification_mail(mail)
        tel=input('Téléphone :')
        client1.verification_tel(tel)
        cp=input('Code Postal :')
        client1.verification_cp(cp)
        bthd=input('Date de naissance :')
        client1.verification_bthd(bthd)
        input(f'Bonjour {client1.prenom} {client1.nom}, vous êtes inscrit avec succès. \n Voici un récapitulatif de vos informations : \n Nom : {client1.nom} \n Prénom : {client1.prenom} \n Email : {client1.mail__} \n Téléphone : {client1.tel__} \n Code Postal : {client1.cp__} \n Date de naissance : {client1.bthd__}\n')
    

client1=main()