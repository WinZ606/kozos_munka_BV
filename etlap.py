def kiir2(jel:str = "=", szam:int = 25):
    print(jel * szam)

def kiir(levesek, levesek_ar):
    i = 0
    while i < len(levesek):
        print(f"{i+1}. {levesek[i]} {levesek_ar[i]:>.0f}FT")
        i += 1