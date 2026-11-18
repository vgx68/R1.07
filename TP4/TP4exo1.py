m=[]
table=float(input("Entre la valeur"))
for i in range(0,9) :
    m.append(table * i)

for i in range(len(m)) :
    prod = round(m[i], 1)
    print(table,"*",i,"=",prod)