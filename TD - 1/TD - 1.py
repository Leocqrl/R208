d={"Marteaux":51,
   "Scies":11,
   "Pelles":78,
   "Perceuses":5,
   "Niveaux à bulle":65,
   "Rabots":26,
   "Jeu de clés plates":1}


def menu(x=None):
    global d
    if x==None:
        x=input('Veuillez saisir la référence recherchée. \n   > Afficher le stock disponible : Tout\n   > Mettre fin au programme : Fin \n   Que voulez vous faire ? ')
    #Mettre fin au programme
    if x=='Fin':
        return("Menu fermé, aurevoir.")
    #Afficher tout
    elif x=='Tout':
        print('Il reste en stock :')
        for i in d:
            print(f'    - {d[i]} {i}')
        menu()

    #Message d'erreur
    # if (x!='Tout' or x!='Fin' ) and x not in d.keys() :
    #     print("La référence n'est pas reconnue.")
    #     menu()

    #Option d'ajout
    elif x[0]=="+":
        for n, caractère in enumerate(x): 
            if caractère == '>': y=n
        valeur=x[1:y]
        nombre=x[y+1:]
        d[valeur]=nombre
        menu('Tout')
    
    #Option de modification
    elif x[0]=="#":
        for n, caractère in enumerate(x): 
            if caractère == '>': y=n
        valeur=x[1:y]
        nombre=x[y+1:]
        d.update({valeur:nombre})
        menu('Tout')

    else:
        print(f'Il reste {d[x]} {x}.')
        menu()

menu()

