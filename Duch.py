#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
class Duch:  # Tahle třída slouží k vykreslení duchů - k rozhovoru
    def __init__(self, popis, pozadavek, prikaz, podminka, pritomnost, pribeh, pojmenovani):
        self.__popis = popis
        self.__pozadavek = pozadavek
        self.__prikaz = prikaz
        self.__podminka = podminka
        self.__pritomnost = pritomnost
        self.__pribeh = pribeh
        self.__pojmenovani = pojmenovani

    @property
    def popis(self):
        return self.__popis

    @property
    def pritomnost(self):
        return self.__pritomnost

    @property
    def prikaz(self):
        return self.__prikaz

    @property
    def pozadavek(self):
        return self.__pozadavek

    @property
    def podminka(self):
        return self.__podminka

    @property
    def pribeh(self):
        return self.__pribeh

    def uspokojeni(self):
        self.__pritomnost = False

    @property
    def jmeno(self):
        return self.__pojmenovani
    def __str__(self):
        return str(self.__popis)

    def rozhovor(self, hrdinka):
        if self.__pojmenovani != "Trezor":
            print("Mezzobran zkusila ducha několikrát různě oslovit, ale odpověď je stále stejná.")
        print(self.pozadavek)
        if self.podminka in hrdinka.inventar:
            cprint("Jestliže chceš vyhovět, stiskni A, jestliže ne, stiskni N.", "green")
            volba2 = input()
            if volba2 == "A":
                print(self.pribeh)
                self.uspokojeni()
        else:
            print("\'Je mi líto, ale s tím já teď nic nenadělám,\' pokrčila temná elfka rameny.")
