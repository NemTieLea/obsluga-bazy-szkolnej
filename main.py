class Wychowawca:
    def __init__(self, imie_nazwisko, klasa):
        self.imie_nazwisko = imie_nazwisko
        self.klasa = klasa

    def __str__(self):
        return f"Wychowawca: {self.klasa} [{self.imie_nazwisko}]"


class Nauczyciel:
    def __init__(self, imie_nazwisko, lista_klas, prowadzone_przedmioty):
        self.imie_nazwisko = imie_nazwisko
        self.lista_klas = lista_klas
        self.prowadzone_przedmioty = prowadzone_przedmioty

    def __str__(self):
        return f"<Nauczyciel: {self.imie_nazwisko} klasy: {self.lista_klas} prowadzi: {self.prowadzone_przedmioty}>"


class Uczen:
    def __init__(self, imie_nazwisko, klasa):
        self.imie_nazwisko = imie_nazwisko
        self.klasa = klasa

    def __str__(self):
        return f"<Uczen: {self.imie_nazwisko} w {self.klasa}>"


class Klasa:
    def __init__(self, nazwa, wychowawca=None):
        self.nazwa = nazwa
        self.wychowawca = wychowawca
        self.uczniowie = []

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)

    def __str__(self):
        uczniowie_str = ', '.join([uczen.imie_nazwisko for uczen in self.uczniowie])
        return f"<Klasa: {self.nazwa} uczniowie: [{uczniowie_str}] pod opieką: {self.wychowawca.imie_nazwisko if self.wychowawca else 'Brak wychowawcy'}>"


def wczytaj_wychowawce():
    imie_nazwisko = input('Imię i nazwisko wychowawcy: ')
    klasa = input('Nazwa klasy: ')
    nowy_wychowawca = Wychowawca(imie_nazwisko, klasa)
    return nowy_wychowawca


def wczytaj_nauczyciela():
    imie_nazwisko = input('Imię i nazwisko nauczyciela: ')
    prowadzony_przedmiot = input('Prowadzony przedmiot: ')
    lista_klas = []
    while True:
        klasa = input('Klasa (puste aby przerwać): ')
        if not klasa:
            break
        lista_klas.append(klasa)
    nowy_nauczyciel = Nauczyciel(imie_nazwisko, lista_klas, prowadzony_przedmiot)
    return nowy_nauczyciel


def wczytaj_ucznia():
    imie_nazwisko = input('Imię i nazwisko ucznia: ')
    klasa = input('Klasa: ')
    nowy_uczen = Uczen(imie_nazwisko, klasa)
    return nowy_uczen


def wykonaj_akcje_klasa(klasy):
    nazwa_klasy = input('Podaj nazwę klasy: ')
    for klasa in klasy:
        if klasa.nazwa == nazwa_klasy:
            print(klasa)
            return
    print(f"Klasa {nazwa_klasy} nie została znaleziona.")


def wykonaj_akcje_uczen(uczniowie, nauczyciele):
    imie_nazwisko_ucznia = input('Imię i nazwisko ucznia: ')
    for uczen in uczniowie:
        if uczen.imie_nazwisko == imie_nazwisko_ucznia:
            print(uczen)
            przedmioty_i_nauczyciele = []
            for nauczyciel in nauczyciele:
                if uczen.klasa in nauczyciel.lista_klas:
                    przedmioty_i_nauczyciele.append((nauczyciel.prowadzone_przedmioty, nauczyciel.imie_nazwisko))
            for przedmiot, nauczyciel in przedmioty_i_nauczyciele:
                print(f"Przedmiot: {przedmiot}, Nauczyciel: {nauczyciel}")
            return
    print(f"Uczeń {imie_nazwisko_ucznia} nie został znaleziony.")


def wykonaj_akcje_nauczyciel(nauczyciele):
    imie_nazwisko_nauczyciela = input('Imię i nazwisko nauczyciela: ')
    for nauczyciel in nauczyciele:
        if nauczyciel.imie_nazwisko == imie_nazwisko_nauczyciela:
            print(nauczyciel)
            return
    print(f"Nauczyciel {imie_nazwisko_nauczyciela} nie został znaleziony.")


def wykonaj_akcje_wychowawca(wychowawcy, klasy):
    imie_nazwisko_wychowawcy = input('Imię i nazwisko wychowawcy: ')
    for wychowawca in wychowawcy:
        if wychowawca.imie_nazwisko == imie_nazwisko_wychowawcy:
            print(wychowawca)
            for klasa in klasy:
                if klasa.wychowawca == wychowawca:
                    print(f"Klasa: {klasa.nazwa}")
            return
    print(f"Wychowawca {imie_nazwisko_wychowawcy} nie został znaleziony.")


nauczyciele = []
wychowawcy = []
uczniowie = []
klasy = []

while True:
    akcja = input('utworz / zarzadzaj / koniec: ')
    if akcja == 'koniec':
        print("Kończę")
        break
    elif akcja == 'utworz':
        while True:
            akcja_wewnetrzna = input('uczen / nauczyciel / wychowawca / klasa / koniec: ')
            if akcja_wewnetrzna == 'koniec':
                break
            elif akcja_wewnetrzna == 'wychowawca':
                nowy_wychowawca = wczytaj_wychowawce()
                wychowawcy.append(nowy_wychowawca)
                istnieje = False
                for klasa in klasy:
                    if klasa.nazwa == nowy_wychowawca.klasa:
                        klasa.wychowawca = nowy_wychowawca
                        istnieje = True
                        break
                if not istnieje:
                    nowa_klasa = Klasa(nowy_wychowawca.klasa, nowy_wychowawca)
                    klasy.append(nowa_klasa)
            elif akcja_wewnetrzna == 'nauczyciel':
                nowy_nauczyciel = wczytaj_nauczyciela()
                nauczyciele.append(nowy_nauczyciel)
            elif akcja_wewnetrzna == 'uczen':
                nowy_uczen = wczytaj_ucznia()
                uczniowie.append(nowy_uczen)
                istnieje = False
                for klasa in klasy:
                    if klasa.nazwa == nowy_uczen.klasa:
                        klasa.dodaj_ucznia(nowy_uczen)
                        istnieje = True
                        break
                if not istnieje:
                    nowa_klasa = Klasa(nowy_uczen.klasa)
                    nowa_klasa.dodaj_ucznia(nowy_uczen)
                    klasy.append(nowa_klasa)
            else:
                print("Nie ma takiego stanowiska")
    elif akcja == 'zarzadzaj':
        while True:
            akcja_wewnetrzna = input('klasa / uczen / nauczyciel / wychowawca / koniec: ')
            if akcja_wewnetrzna == 'koniec':
                break
            elif akcja_wewnetrzna == 'klasa':
                wykonaj_akcje_klasa(klasy)
            elif akcja_wewnetrzna == 'uczen':
                wykonaj_akcje_uczen(uczniowie, nauczyciele)
            elif akcja_wewnetrzna == 'nauczyciel':
                wykonaj_akcje_nauczyciel(nauczyciele)
            elif akcja_wewnetrzna == 'wychowawca':
                wykonaj_akcje_wychowawca(wychowawcy, klasy)
            else:
                print("Nie ma takiej komendy")
    else:
        print("Nie ma takiej komendy...")