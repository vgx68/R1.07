nMax=int(input("Valeur nMax ?"))
n=int(input("Quelle est la taille de votre vecteur entre 1 et 10 ?"))

if 1 <= n <= nMax:
    v1 = []
    v2 = []
    for i in range(n):
        print("Saisie premier vecteur :")
        val= int(input(f"v1[{i}] = "))
        v1.append(val)

    for i in range(n):
        print("Saisie second vecteur :")
        val = int(input(f"v2[{i}] = "))
        v2.append(val)

    scal = 0.0

    for i in range(n):
        scal += v1[i]*v2[i]

    print(f"Le produit scalaire de v1 par v2 vaut {scal}")
else:
    print("Erreur")