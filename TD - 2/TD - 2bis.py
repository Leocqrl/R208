import os, json5, yaml

def cwd():
    return os.getcwd()

print(cwd())
CompletFile=[]
with open ("TD - 2/file.json", encoding='utf-8') as f:
    for i in f:
        file=json5.loads(i)
        CompletFile.append(file)


with open('TD - 2/file.yml', 'w', encoding='utf-8') as file:
    yaml.dump(CompletFile, file, indent=4)

print(CompletFile)

Nom=input('Veuillez saisir les données du nouvel utilisateur. \n Nom: ')
Prenom=input('Prénom : ')
age=input('Âge : ')
type=input('Type de contrat : ')

Ajout=[{"age":int(age),"nom" : Nom, "prenom" : Prenom, "typecontrat":type}]

with open('TD - 2/file.yml', 'a', encoding='utf-8') as file:
    yaml.dump(Ajout, file, indent=4)

with open("TD - 2/file.json", 'a', encoding='utf-8') as file:
    json5.dump(Ajout[0], file, indent=4)
