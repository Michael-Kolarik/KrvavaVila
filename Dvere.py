#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
class Nedvere:  # Tahle třída slouží jako pomocná pro definování konkrétních objektů jiných tříd
    def __init__(self):
        self.__xyz = "xyz"

    def pruchod(self):
        x = input()
        print(x)


class Dvere:  # Tahle třída vykresluje dveře mezi místnostmi
    def __init__(self, prvnimistnost, druhamistnost, popis, postava):

        self.prvnimistnost = prvnimistnost
        self.druhamistnost = druhamistnost
        self.__popis = popis
        self.postava = postava

    @property
    def popis(self):
        return self.__popis

    def pruchod(self, postava):
        if self.postava.lokalizace == self.prvnimistnost.nazev():
            self.postava.poloha(self.druhamistnost.nazev())
            self.druhamistnost.vstup()

        else:
            self.postava.poloha(self.prvnimistnost.nazev())
            self.prvnimistnost.vstup()

    def prejmenovani (self, jmeno):
        self.__popis = jmeno
class Zablokovane_dvere(Dvere):  # Tahle třída je pro speciální případ dveří
    def __init__(self, prvnimistnost, druhamistnost, popis, postava, dialog):
        super().__init__(prvnimistnost, druhamistnost, popis, postava)
        self.__zablokovani = True
        self.__dialog = dialog

    def pruchod(self, postava):
        if self.__zablokovani:
            print(self.__dialog)
            self.prvnimistnost.zustat()
        else:
            if self.postava.lokalizace == self.prvnimistnost.nazev():
                self.postava.poloha(self.druhamistnost.nazev())
                self.druhamistnost.vstup()
            else:
                self.postava.poloha(self.prvnimistnost.nazev())
                self.prvnimistnost.vstup()
    def odblokovani(self):
        self.__zablokovani = False


class Vrata(Dvere):
    def __init__(self, prvnimistnost, druhamistnost, popis, postava):
        super().__init__(prvnimistnost, druhamistnost, popis, postava, )

    def pruchod(self, postava):
        if self.postava.dokonceni:
            print("Mezzobran vyšla z vily.")
        else:
            print("Skutečně chceš odejít bez splnění úkolu? Pokud skutečně ano, stiskněte A")
            volba = input()
            if volba == "A":
                print("Mezzobran vyšla z vily.")
            else:
                self.prvnimistnost.zustat()