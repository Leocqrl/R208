from Tri import Tri_a_bulles

# Dictionnaire sous la forme : 
#    d={'Nom':['prenom','numéro']} 
d={'ELK':['Amine','0753628195'],'CQL': ['Léo','0673426189'], 'SLM':['Ilies','0863821729']}

def main(V=None):
    global d
    if V==None:
        V=input(' +-----------------------+ \n |Gestionnaire de contact| \n +-----------------------+ \n |   * Visualiser(V)     | \n |   * Ajouter(A)        | \n |   * Modifier(M)       | \n |   * Supprimer(S)      | \n |   * Rechercher(R)     | \n +-----------------------+ \n\n Votre Saisie : ')
        main(V)
    elif V=='V':
        tri=Tri_a_bulles(list(d.keys()))
        temp={}
        for lt in tri:
            temp[lt]=d[lt]
        d=temp
        print(' +-----------------------------------------+ \n |  Nom  |      Prenom      |    Numéro    | \n +-----------------------------------------+')
        for i in d:
            print(f' |  {i}  |    {d[i][0].ljust(12,' ')}  |  {d[i][1]}  |')
        print(' +-----------------------------------------+ ')
        
    elif V=='A':
        Nom=input('Veuillez saisir le nom (format : Blanc --> BLC): ')
        if Nom=='':
            main()
        else :
            Prenom=input('Veuillez saisir le prénom : ')
            num=input('Veuillez saisir le numéro de téléphone : ')
            d[Nom]=[Prenom, num]
            main('A')
    elif V=='M':
        nom=input('Nom du contact que vous souhaitez modifier :')
        if nom=='':
            pass
        else : 
            M=input('Que voulez vous modifier, Prénom(P) ou Numéro de téléphone(N): ')
            val=input('Valeur :')
            if M=='P':
                d[nom][0]=val
            elif M=='N':
                d[nom][1]=val
            elif M=='':
                pass
        main()
    elif V=='S':
        nom=input('Nom du contact que vous souhaitez supprimer :')
        d.pop(nom)
        main()
    elif V=='R':
        rec=input('Indiquez le nom du contact recherché : ')
        if rec in d:
            print(f' +-----------------------------------------+ \n |  Nom  |      Prenom      |    Numéro    | \n +-----------------------------------------+ \n |  {rec}  |    {d[rec][0].ljust(12,' ')}  |  {d[rec][1]}  | \n +-----------------------------------------+ ')
        elif rec=='':
            pass
        else :
            print('Contact inconnu.e')
            main('R')
        main()
        
    elif V=='':
        pass
    
main()