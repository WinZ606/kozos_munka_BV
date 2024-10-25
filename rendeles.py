import etlap

def rendeles1(lev1,lev_ar,foet,foet_ar):
    rendeles = int(input(f"Mit kér?\n1 -> Levesek\n2 -> Főételek"))
    if rendeles == 1:
        leves = int(input(f"Itt vannak a leveseink: \n"))
    else:
        print()