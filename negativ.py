szám1 = int(input("Adj meg egy nullától különböző számot: "))
szám2 = int(input("Adj meg egy másik nullától különböző számot: "))

if (szám1 > 0 and szám2 > 0):
    print("A két szám közül egyik sem negatív")
elif (szám1 < 0 and szám2 < 0):
    print("Mind a két szám negatív")
elif (szám1 > 0 and szám2 < 0):
    print("A két szám közül a második negatív")
elif (szám1 < 0 and szám2 > 0):
    print("A két szám közül az első negatív")

