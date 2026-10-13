list1= []
list2= []
list3= []
for i in range(10) :

    while True :
        val = int(input(f"Entrez un nombre ({i+1}) :"))
        if val > 20 or val < 0:
            print("Valeur non valide")
        else:
            if val < 10:
                list1.append(val)
            elif val >= 10 and val < 15:
                list2.append(val)
            elif val >= 15:
                list3.append(val)
            break

print(list1)
print(list2)
print(list3)