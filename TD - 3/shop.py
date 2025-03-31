from Client import Client
import pickle

cli=None

def main(val=None):
    if val==None:
        val=input("Menu : \n    1) Renseigner nom et email\n    2) Ajout d'articles au panier\n    3) Sérialiser l'objet\n    4) Désérialiser l'objet \n    5) Régler la commande \n\n Votre saisie :")
    if val=='1':
        global cli
        nom=input('Nom : ')
        email=input('Email : ')
        cli=Client(nom, email)
        main()
    elif val=='2':
        YN=input('Voulez vous ajouter un article ? Y/n \n Votre saisie : ')
        if YN=='Y':
            art=input('Article à ajouter : ')
            Q=input('Quantitée : ')
            p=input('Prix à l\'unitée : ')
            cli.ajout_panier([art, Q, p])
            main('2')
        elif YN=='n':
            main()
    elif val=='3':
        with open('./TD - 3/cli.pso', 'wb') as f:
            pick = pickle.Pickler(f, pickle.HIGHEST_PROTOCOL)
            pick.dump(cli)
        main()
    elif val=='4':
        try :
            with open('./TD - 3/cli.pso', 'rb') as f:
                unpick = pickle.Unpickler(f)
                cli=unpick.load()
        except Exception as err:
            print(err.args)
        main()
    elif val=='5':
        mode_reglement=input('Veuillez préciser votre mode de payement : ')
        cli.regler_commande(mode_reglement)
    elif val=="":
        pass

main()