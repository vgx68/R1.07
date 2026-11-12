import time
n=int(input("valeur de n positive"))
for i in range(0,n):
    time.sleep(1)
    n=n-1
    print(n, flush=True)
