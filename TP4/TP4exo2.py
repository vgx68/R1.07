nbetud= int(input("Donnez le nombre d'etudiants : "))
moyenne=0.0
notes=[]

som = 0
while True:
    for num_etu in range (nbetud):
        note = (float(input(f"Note étudiant {num_etu} : ")))
        if note<0 or note>20 :
            break
        else:
            notes.append(note)
            som += note
            moyenne = som / nbetud
    print(f"moyenne de classe : {moyenne}")
    for num_etu in range (nbetud):
        ecart = notes[num_etu]-moyenne
        print("Numéro de l'etudiant | note | ecart de la moyenne")
        print(f"{num_etu} |{notes[num_etu]} |{ecart}")