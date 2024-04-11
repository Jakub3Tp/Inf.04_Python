class Notatka():
    __licznik = 0

    def __init__(self, tytul, tresc):
        Notatka.licznik += 1
        self.__id = Notatka.__licznik
        self.tytul = tytul
        self.tresc = tresc

    def wyswietl(self):
        print(f"Tytuł: {self.tytul}, Treść:  {self.tresc}")

    def diagnostyka(self):
       print(f"{self.tytul}, {self.tresc}")