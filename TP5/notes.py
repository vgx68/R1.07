notes = 0
coef = 0
compteur = 0

for i in range(0,5):
    s1 = (str(input(f"Note du module {compteur+1} et coef du module : ")))
    s2 = s1.split(" ")
    s3 = s2[0]
    s4 = s2[1]
    print(s3, s4)
    compteur += 1
