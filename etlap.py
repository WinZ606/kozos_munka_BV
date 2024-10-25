def kiir2(jel:str = "=", szam:int = 25):
    print(jel * szam)

def kiir(levesek, levesek_ar):
    i = 0
    while i < len(levesek):
        if (len(levesek)) > 10:
            print(f"{i+1}. {levesek[i]} {levesek_ar[i]:>0.0f}FT")
        else:
            print(f"{i+1}. {levesek[i]} {levesek_ar[i]:>8.0f}FT")
        i += 1