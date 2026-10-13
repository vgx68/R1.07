tab = [1, "Eh !", 3, "Oh !"]
print(type(tab))
"""Le type est une liste de tableau"""
for val in tab :
    print (val)
tab[3] = "Ah! "
"""On modifie dans la valeur 3 le Oh ! par Ah!"""
for i in range(len(tab)) :
    """Nombre de valeur dans le tableau"""
    print(tab[i])