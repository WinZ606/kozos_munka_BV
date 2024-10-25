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
        while leves >=1 and leves <= 3:
            leves == int(input("Még valamit? \n"))
            rend_lev.append(levesek[leves]),rend_lev_ar.append(levesek_ar[leves])
    elif rendeles == 2:
        foetel = int(input(f"Mit kér?\n"))
        rend_foet.append(foetelek[foetel]),rend_foet_ar.append(foetelek_ar[foetel])
        while leves != 0:
            foetel == int(input("Még valamit? \n"))
            rend_lev.append(foetel[foetel]),rend_foet_ar.append(foetelek_ar[foetel])
    print(rend_lev)
    print(rend_lev_ar)
    print(rend_foet)
    print(rend_foet_ar)