import random
x=random.randint(0,100)
print(x)
n=int(input("Je devine un nombre :"))
while True:
    if n == x:
        break
    else:
        if x<n:
            print(f"({n}) est plus grand continuer a chercher")
            n=int(input("Je devine un nombre :"))
        else :
            print(f"({n}) est plus petit continuer a chercher")
            n=int(input("Je devine un nombre :"))

print("Bravo...")