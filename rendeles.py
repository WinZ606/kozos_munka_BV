import etlap

def rendeles1(levesek,levesek_ar,foetelek,foetelek_ar):
    rend_lev = []
    rend_lev_ar = []
    rend_foet = []
    rend_foet_ar = []
    rendeles = int(input(f"1. Levesek\n2. Főételek\nMit kér? "))
    if rendeles == 1:
        leves:int = int(input(f"Mit kér?\n"))
        while leves != -1:
            rend_lev.append(levesek[leves-1]),rend_lev_ar.append(levesek_ar[leves-1])
            leves:int = int(input("Még valamit? \n"))
        eves = int(input(f"Kér főételt?\n1. Igen\n2. Nem\n"))
        if eves == 2:
            print(rend_lev)
            print(rend_lev_ar)
        elif eves == 1:
            foetel = int(input(f"Mit kér?\n"))
            rend_foet.append(foetelek[foetel-1]),rend_foet_ar.append(foetelek_ar[foetel-1])
            while foetel != 0:
                rend_lev.append(levesek[leves-1]),rend_lev_ar.append(levesek_ar[leves-1])
                leves = int(input("Még valamit? \n"))
            print(rend_lev)
            print(rend_lev_ar)
            print(rend_foet)
            print(rend_foet_ar)
    elif rendeles == 2:
        rend_foet.append(foetelek[foetel-1]),rend_foet_ar.append(foetelek_ar[foetel-1])
        foetel = int(input(f"Mit kér?\n"))
        while foetel != 0:
            rend_lev.append(foetel[foetel-1]),rend_foet_ar.append(foetelek_ar[foetel-1])
            foetel = int(input("Még valamit? \n"))
        print(rend_foet)
        print(rend_foet_ar)