f=1
n=int(input("Entrez un nombre"))
if n<0:
    print("les valeurs négatives ne sont pas inclus")
else :
    for i in range(1,n+1) :
        f=f*i
        print(f"La factorielle de {n} est : {f}")