#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
from Kostka import Kostka

class Zombie:  # Tahle třída je na zombie - fyzické protivníky
    def __init__(self, jmeno, utocne_cislo, obranne_cislo, zraneni, zivoty, iniciativa, kostka, popis):
        self.__jmeno = jmeno
        self.zivoty = zivoty
        self.maxzivot = zivoty
        self.utocne_cislo = utocne_cislo
        self.obranne_cislo = obranne_cislo
        self.kostka = kostka
        self.zraneni = zraneni
        self.__iniciativa = iniciativa
        self.popis = popis  # Definuje vstupy


    def jmeno(self):
        return str(self.__jmeno)  # vypisuje jmeno


    @property
    def nazivu(self):
        return self.zivoty > 0  # Zjistí jestli bojovík žije

    @property
    def iniciativa(self):
        return self.__iniciativa

    def obrana(self, zasah, poskozeni):
        if zasah >= self.obranne_cislo:
            self.zivoty = self.zivoty - poskozeni
            print("Ostří zajelo do neživého těla.")
        else:
            print("Útok tu bytost minul.")
        if self.zivoty <= 0:
            print("Mezzobran se podařilo bodnout zvlášť citelně.")
            if self.kostka.hod() >= poskozeni + 2:
                self.zivoty = 1
                print("Ale zombie se i po téhle ráně zvedá.")
            else:
                self.zivoty = 0
                print("{0} to má za sebou.".format(self.__jmeno))

    def utok(self, souper, kostka):
        if self.zraneni > 0:
            print("{0} se ohnala svou nemrvou pěstí.".format(self.__str__()))
        else:
            print("Modla na Mezzobran dál dorážela.")
        hod_na_utok = kostka.hod() + self.utocne_cislo + 2
        kostka_zraneni = Kostka(self.zraneni)
        hod_na_zraneni = kostka_zraneni.hod() + self.utocne_cislo
        souper.obrana(hod_na_utok, hod_na_zraneni)

    def __str__(self):
        return self.popis  # vypisuje popis

    def prepad(self, cil, kostka):
        print("Náhle elfka uslyší divný zvuk. Je to {0} Divoce se rozmáchne a útočí.".format(self.__str__()))
        hod_na_utok = kostka.hod() + self.utocne_cislo + 7
        kostka_zraneni = Kostka(self.zraneni)
        hod_na_zraneni = kostka_zraneni.hod() + self.utocne_cislo
        cil.obrana(hod_na_utok, hod_na_zraneni)

class Demon(Zombie):  # Tahle třída je pro vylepšeného finálního bosse
    def __init__(self, jmeno, utocne_cislo, obranne_cislo, zraneni, zivoty, iniciativa, kostka, popis, viditelny):
        super().__init__(jmeno, utocne_cislo, obranne_cislo, zraneni, zivoty, iniciativa, kostka, popis)
        self.__viditelny = True

    def obrana(self, zasah, poskozeni):
        if zasah >= self.obranne_cislo:
            print("Zbraň démona zasáhla navzdory vší jeho nepřirozenosti.")
            self.zivoty = self.zivoty - (poskozeni / 2)
        else:
            print("Ostří však tu malou zrůdičku minulo.")
        if self.zivoty < 0:
            self.zivoty = 0

    def utok(self, souper, kostka):
        if self.__viditelny:
            print("Démon se zneviditelnil. Mezzobran tušila kde je, ale útok i obrana teď budou těžší.")
            self.__viditelny = False
            self.obranne_cislo = self.obranne_cislo + 5
            self.utocne_cislo = self.utocne_cislo + 5
        else:
            print("Démon zaútočil svým jedovým ocasem a při tom se zviditelnil.")
            self.__viditelny = True
            hod_na_utok = kostka.hod() + self.utocne_cislo + 2
            sestistenka = Kostka(6)
            jedove_zraneni = sestistenka.hod() + sestistenka.hod() + sestistenka.hod()
            kostka_zraneni = Kostka(self.zraneni)
            hod_na_zraneni = kostka_zraneni.hod() + self.utocne_cislo
            if kostka.hod() < 9:
                hod_na_zraneni = hod_na_zraneni + jedove_zraneni
            else:
                hod_na_zraneni = hod_na_zraneni + jedove_zraneni / 2
            souper.obrana(hod_na_utok, hod_na_zraneni)
            self.obranne_cislo = self.obranne_cislo - 5
            self.utocne_cislo = self.utocne_cislo - 5
