pontszam = int(input("kérem a pontszámodat"))
#0-19   1   20-39   2   40-59   3   60-79   4   80-100   5
if (20 > pontszam):
    print("elégtelen")
elif( 40 > pontszam):
    print("elégséges")
elif( 60 > pontszam):
    print("közepes")
elif( 80 > pontszam):
    print("jó")
else:
    print("jeles")
