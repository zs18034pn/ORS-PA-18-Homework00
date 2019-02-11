korisnik_uneo_prvi = input("Unesite prvi broj: ")
korisnik_uneo_drugi = input("Unesite drugi broj: ")

if (not  korisnik_uneo_prvi.isnumeric()) or (not korisnik_uneo_drugi.isnumeric()) :
    print("Niste uneli dobre brojeve")
    quit()


korisnik_broj_prvi = int(korisnik_uneo_prvi)
korisnik_broj_drugi = int(korisnik_uneo_drugi)

zbir = korisnik_broj_prvi + korisnik_broj_drugi
print(zbir)

