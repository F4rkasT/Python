napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

nap = int(input("adja meg a napot: "))

def szamolas(nap):
    return napok[nap]

print(szamolas(nap))
    
if (nap == 0):
    print("nap0")
elif(nap == 3):
    print("Csütörtök")
else:
    print("mész dolgozni")


