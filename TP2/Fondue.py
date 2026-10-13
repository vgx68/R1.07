base=4
fromage=800
eau = 2
ail = 2
pain = 400
nbconvives= int(input("Entrez le nombre de personne(s) conviviées à la fondues : "))
nvqfromage = float(fromage * nbconvives / base)
nvqeau = float(eau * nbconvives / base)
nvqail = float(ail * nbconvives / base)
nvqpain = float(pain * nbconvives / base)
print("Pour faire une fondue fribourgeoise pour ", nbconvives, " personnes, il vous faut :")
print("- ",nvqfromage,"gr de fromage")
print("- ",nvqeau,"dl d'eau")
print("- ",nvqail,"gousse(s) d'ail")
print("- ",nvqpain,"gr de pain")
