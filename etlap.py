def kiir2(jel:str = "=", szam:int = 30):
    print(jel * szam)

def kiir(levesek, levesek_ar, hossz:int=30):
    i = 0
    while i < len(levesek):
        print(f"{i + 1}. {levesek[i]:<{hossz-15}} {levesek_ar[i]:>8.0f} FT")
        i += 1