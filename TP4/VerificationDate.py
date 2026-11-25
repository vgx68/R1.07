date = input("Saisir la date : ")

jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:])

print(jour, mois, annee)

nb_jour_dans_mois_bis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nb_jour_dans_mois_non_bis = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if annee < 1000:
    print("Année incorrecte")
else:
    if mois < 1 or mois > 12:
        print("Mois incorrecte")
    else:
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            nb_jour_dans_mois = nb_jour_dans_mois_bis[mois - 1]
        else:
            nb_jour_dans_mois = nb_jour_dans_mois_non_bis[mois - 1]
        if jour < 1 or jour > nb_jour_dans_mois:
            print("Jour incorrecte")
        else:
            print("Jour correcte")

