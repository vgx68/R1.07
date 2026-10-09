x1=int(input("Entrez x1: "))
y2=int(input("Entrez y2: "))

print("avant permu", x1)
print("avant permu", y2)
tmp = x1
x1 = y2
y2 = tmp
print("après permu", x1)
print("après permu", y2)