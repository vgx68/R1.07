x1=int(input("Entrez x1: "))
y2=int(input("Entrez y2: "))

print("avant permu")
print("x1", x1)
print("y2", y2)
tmp = x1
x1 = y2
y2 = tmp
print("apres permu")
print("x1", x1)
print("y2", y2)