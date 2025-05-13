import sqlite3, yaml, json5, csv, os, xml.etree.ElementTree as ET

"""
Le programme doit créer une base de données SQLite3 avec une table “médias” contenant les colonnes suivantes :
- id (clé primaire, entier, auto-incrémenté)
- type 
- titre 
- auteur 
- date_emprunt 

Le programme doit alimenter la table “médias” avec au minimum 3 lignes.

Le programme doit proposer un menu à l'utilisateur avec les options suivantes :
    1. Afficher le contenue complet de la table dans la console (de manière lisible et tabulaire)
    2. Générer un fichier csv
    3. Générer un fichier xml
    4. Générer un fichier json  
    5. Générer un fichier yaml
"""

def creationTable():
    connectionSQLITE = sqlite3.connect("TP - 3/medias.db")
    cur = connectionSQLITE.cursor()
    try:
        cur.execute("CREATE TABLE MEDIA ("
                    "IDENTIFIANT INT PRIMARY KEY,"
                    "TYPE NOT NULL DEFAULT 'Livre',"
                    "TITRE NOT NULL,"
                    "AUTEUR NOT NULL,"
                    "DATE_EMPRUNT)")
    except Exception as err:
        print(err.args)

def ajoutLigne(data):
    connectionSQLITE = sqlite3.connect("TP - 3/medias.db")
    cur = connectionSQLITE.cursor()
    cur.executemany("INSERT INTO MEDIA (IDENTIFIANT, TYPE, TITRE, AUTEUR, DATE_EMPRUNT) VALUES (?, ?, ?, ?, ?)", data)
    connectionSQLITE.commit()

def main(n=None):
    if n== None:
        input("Bonjour, bienvenue dans votre Gestionnaire de Médias ! \n\n Appuyez sur une touche pour continuer...")
        n=0
    if n==0:
        n=int(input("Voici la liste de vos possibilités : \n\n 1. Afficher le contenu complet de la table \n 2. Générer un fichier csv \n 3. Générer un fichier xml \n 4. Générer un fichier json \n 5. Générer un fichier yaml \n\n Appuyez sur une touche pour continuer...\n\n Votre choix : "))
    if n==1:
        afficherTable()
        pass
    elif n==2:
        converterCSV()
        pass
    elif n==3:
        converterXML()
        pass
    elif n==4:
        converterJSON()
        pass
    elif n==5:
        converterYAML()
        pass
    else:
        print("Erreur, veuillez choisir une option valide.")
        main(0)

def selectTable():
    connectionSQLITE = sqlite3.connect("TP - 3/medias.db")
    cur = connectionSQLITE.cursor()
    cur.execute("SELECT * FROM MEDIA")
    rows = cur.fetchall()
    return rows

def ToLDictionaire(rows):
    Ldictionnaire = []
    for row in rows:
        media = {
            "Identifiant": row[0],
            "Type": row[1],
            "Titre": row[2],
            "Auteur": row[3],
            "Date_Emprunt": row[4]
        }
        Ldictionnaire.append(media)
    return Ldictionnaire

def converterCSV():
    rows = selectTable()
    try:
        with open('TP - 3/media.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Identifiant", "Type", "Titre", "Auteur", "Date_Emprunt"])
            writer.writerows(rows)
            print("Le fichier media.csv a été créé avec succès.")
    except Exception as err:
        print("Erreur lors de la création du fichier media.csv :", err)
    pass

def converterXML():
    rows = selectTable()
    try:
        root = ET.Element("media")
        for row in rows:
            media = ET.SubElement(root, "media")
            id_elem = ET.SubElement(media, "identifiant")
            id_elem.text = str(row[0])
            type_elem = ET.SubElement(media, "type")
            type_elem.text = row[1]
            titre_elem = ET.SubElement(media, "titre")
            titre_elem.text = row[2]
            auteur_elem = ET.SubElement(media, "auteur")
            auteur_elem.text = row[3]
            date_emprunt_elem = ET.SubElement(media, "date_emprunt")
            date_emprunt_elem.text = row[4]

        tree = ET.ElementTree(root)
        tree.write("TP - 3/media.xml", encoding='utf-8', xml_declaration=True)
        print("Le fichier media.xml a été créé avec succès.")
    except Exception as err:
        print("Erreur lors de la création du fichier media.xml :", err)
    pass

def converterJSON():
    rows = selectTable()
    rows=ToLDictionaire(rows)
    print(rows)
    try :
        with open('TP - 3/media.json', 'w', encoding='utf-8') as file:
            json5.dump(rows, file, indent=4)
            print("Le fichier media.json a été créé avec succès.")
    except Exception as err:
        print("Erreur lors de la création du fichier media.json :", err)
    pass

def converterYAML():
    rows = selectTable()
    rows=ToLDictionaire(rows)
    try : 
        with open('TP - 3/media.yml', 'w', encoding='utf-8') as file:
            yaml.dump(rows, file, indent=4)
            print("Le fichier media.yml a été créé avec succès.")
    except Exception as err:
        print("Erreur lors de la création du fichier media.yml :", err)
    pass

def afficherTable():
    rows = selectTable()
    print(" +---------------------------------------------------------------------------+ \n |  ID  |      Type      |     Titre     |     Auteur     |   Date Emprunt   | \n +---------------------------------------------------------------------------+")
    for row in rows:
        if len(row[3]) > 13:
            ligne = row[3]
            row = (row[0], row[1], row[2], ligne[:13], row[4])
        print(f" |  {row[0]}   | {row[1].ljust(12,' ')}   | {row[2].ljust(12,' ')}  | {row[3].ljust(13,' ')}  |   {row[4].ljust(13, ' ')}  |")
    print(" +---------------------------------------------------------------------------+ ")
    


if __name__ == "__main__":
    try :
        with open('TP - 3/medias.db', 'r') as file:
            pass
    except FileNotFoundError:
    # if not os.path.exists("TP - 3/medias.db"):
        creationTable()
        data = [
            (1, 'Livre', 'Harry Potter', 'J.K. Rowling', 'null'),
            (2, 'Film', 'Inception', 'Christopher Nolan', 'null'),
            (3, 'Musique', 'Thriller', 'Michael Jackson', 'null')
        ]
        ajoutLigne(data)
    main()

