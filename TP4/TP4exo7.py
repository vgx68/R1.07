binome = ("login1", "login2")
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")

login3 = input("Entrez le login du 3ème : ")
binome = binome + (login3,)

print(f"Trinôme formé : {binome}")

# del ou modifier une liste sur un tuplet n'est pas possible