prenom = str.capitalize(input("prenom: "))
nom = str.upper(input("nom: "))
prenom2 = str.capitalize(input("prenom: "))
nom2 = str.upper(input("nom: "))
if prenom > prenom2 or nom > nom2 or prenom == prenom2 and nom == nom2:
    print(prenom2)
    print(nom2)
    print(prenom)
    print(nom)
else:
    print(prenom)
    print(nom)
    print(prenom2)
    print(nom2)