import time
n=int(input("valeur de n positive"))
while n>0 :
    time.sleep(1)
    n=n-1
    print(n, flush=True)
