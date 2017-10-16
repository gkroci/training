def vytvor_tabulku(velikost=5):
    seznam_radku = []
    for a in range(velikost):
        radek = []
        for b in range(velikost):
            radek.append(a * b)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku()

for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()
