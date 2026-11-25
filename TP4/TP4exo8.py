di={"name":"toto","firstname":"titi","promo":2026,"group":202}
di2={"name":"tata","firstname":"tutu","promo":2025,"group":102}
b = {"id1":di, "id2":di2}

for keys in di.keys():
    print("Les clés du dictionnaire sont :", keys)
for val in di.values():
    print("les valeurs du dictionnaire sont :", val)
for items in di.items():
    print("les tuplets du dictionnaire sont", items)

print("les etudiants formants le binôme sont :")
for k,v in b.items():
    print(f"- l'étudiant {v['name']} du groupe {v['group']}")
#for keys,items, in di2.items():
#    print("l'etudiant", f"{keys} {items} du {keys[3]} {items[3]}")