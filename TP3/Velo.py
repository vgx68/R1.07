while True:
    deb = int(input("Entrez une heure de debut de location"))
    fin = int(input("Entrez une heure de fin de location"))
    if deb < 0 or deb > 24 or fin > 24 or fin < 0:
        print("les heures sont comprise entre 0 et 24")
    elif deb == fin :
        print("valeur identique donc impossible")
    elif deb > fin :
        print("valeur de debut superieur impossible")
    else :
        break

cpt_hp = 0
cpt_hc = 0
for h in range(deb,fin) :
    if h >0 and h <=6 or h >=17 and h <=24 :
        cpt_hc += 1
    else :
        cpt_hp += 1

print(f"{cpt_hc}heure(s) au tarif horaire de 1euro")
print(f"{cpt_hp}heure(s) au tarif horaire de 2euros")
print(f"Tarif : {2* cpt_hp + cpt_hc} euros")