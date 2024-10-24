def csillag1():
    print("*"*36)
    print("LEVESEK")

def csillag2():
    print("*"*38)
    print("FŐÉTELEK")

def kiir(levesek, levesek_ar):
    i = 0
    csillag1()
    while i < len(levesek):
        if len(levesek[i]) > 12:
            pontok = ("."*7)
        else:
            pontok = ("."*12)
        print(f"{i+1}. -> {levesek[i]} {pontok} {levesek_ar[i]:>.0f} Ft")
        i += 1

def kiir(levesek, levesek_ar):
    i = 0
    csillag1()
    while i < len(levesek):
        if len(levesek[i]) > 12:
            pontok = ("."*7)
        else:
            pontok = ("."*12)
        print(f"{i+1}. -> {levesek[i]} {pontok} {levesek_ar[i]:>.0f} Ft")
        i += 1