napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
nap = int(input("adja meg a napot: "))
nap_mulva = int(input("Hány napot aludtt ott: "))
ottalvas = 0
ottalvas += nap
ottalvas += nap_mulva
ottalvas %= 7
print(napok[ottalvas])