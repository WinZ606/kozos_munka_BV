import etlap

def rendeles1(levesek,levesek_ar,foetelek,foetelek_ar):
    rend_lev = []
    rend_lev_ar = []
    rend_foet = []
    rend_foet_ar = []
    rendeles = int(input(f"1. Levesek\n2. Főételek\nMit kér? "))
    if rendeles == 1:
        leves = int(input(f"Mit kér?\n"))
        rend_lev.append(levesek[leves]),rend_lev_ar.append(levesek_ar[leves])
        while leves != 0:
            rend_lev.append(levesek[leves]),rend_lev_ar.append(levesek_ar[leves])
            leves = int(input("Még valamit? \n"))
    elif rendeles == 2:
        rend_foet.append(foetelek[foetel]),rend_foet_ar.append(foetelek_ar[foetel])
        foetel = int(input(f"Mit kér?\n"))
        while foetel != 0:
            rend_lev.append(foetel[foetel]),rend_foet_ar.append(foetelek_ar[foetel])
            foetel = int(input("Még valamit? \n"))
    print(rend_lev)
    print(rend_lev_ar)
    print(rend_foet)
    print(rend_foet_ar)