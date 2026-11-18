L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
smax = 0
p_max=0
for i in range(len(L1)) :
    count = L1.count(L1[i])
    if  count > smax :
        smax = count
        p_max = i
print(f"Le nombre le plus fréquent dans la liste est le {L1[p_max]} ({smax}x)")
