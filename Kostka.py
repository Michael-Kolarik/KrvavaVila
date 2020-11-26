class Kostka:  # Tahle třída jen definuje házení kostkou
    def __init__(self, pocet_sten):
        self.__pocet_sten = pocet_sten

    def hod(self):
        import random as _random
        if self.__pocet_sten > 0:
            vysledek = _random.randint(1, self.__pocet_sten)
        else:
            vysledek = 0
        return vysledek