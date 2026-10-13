nb=int(input("Entrez un nombre entier"))
if nb==0 :
    print("le nombre est zéro et il est pair")
elif nb>0 :
    nb = nb % 2
    if nb==0 :
        print("le nombre est positif et pair")
    else :
        print("le nombre est positif et impair")
elif nb<0 :
    nb = nb % 2
    if nb == 0:
        print("le nombre est négatif et pair")
    else:
        print("le nombre est négatif et impair")