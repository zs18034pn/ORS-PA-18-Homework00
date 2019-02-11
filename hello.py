def validni_brojevi(x, y) :
    if not x.isnumeric()or not y.isnumeric() :
        return False
    else:
        return True


korisnik_uneo_prvi = input("Unesite prvi broj: ")
korisnik_uneo_drugi = input("Unesite drugi broj: ")

if not validni_brojevi(korisnik_uneo_prvi, korisnik_uneo_drugi) :
    quit ("Brojevi nisu validni")


korisnik_broj_prvi = int(korisnik_uneo_prvi)
korisnik_broj_drugi = int(korisnik_uneo_drugi)

zbir = korisnik_broj_prvi + korisnik_broj_drugi
print(zbir)

