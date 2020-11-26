#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
from Kostka import Kostka
kostka = Kostka(20)
class Ukryt:  # Tahle třída vykresluje úkryty, ve kterých se některé zombie schovávají
    def __init__(self, jmeno, zombie, petlice, hrdinka, plny, kostka, druha_zombie):
        self.__jmeno = jmeno
        self.__zombie = zombie
        self.__petlice = petlice
        self.hrdinka = hrdinka
        self.__plny = plny
        self.__kostka = kostka
        self.__druha_zombie = druha_zombie

    @property
    def jmeno(self):
        return self.__jmeno

    @property
    def nazivu(self):
        return self.__zombie.nazivu

    def ukryta_zombie(self):
        return self.__zombie

    @property
    def zamcene_dvere(self):
        return self.__petlice

    def otevreni(self):
        cprint("Co chceš s {0} dělat?".format(self.jmeno),"green")
        if self.__petlice:
            cprint("Uvolnit - stisni U","green")
        if not self.__petlice:
            cprint("Zajistit - stiskni Z","green")
        cprint("Skrz ně zaútočit - stiskni S","green")
        cprint("Otevřít je - stiskni O","green")
        cprint("Nic - stiskni N", "green")
        volba = input()
        if volba == "U":
            self.__petlice = False
        if volba == "Z":
            self.__petlice = True
        if volba == "S":
            self.utok_skrz()
        if volba == "O":
            self.otevreni_dvirek()
        if volba == "N":
            print("Mezzobran mírně poodstoupila.")

    def vyprazdneni(self):
        self.__plny = False

    @property
    def plnost(self):
        return self.__plny
    def otevreni_dvirek(self):
        if self.plnost:
            if self.__zombie.nazivu:
                cprint("Za {0} je {1}".format(self.jmeno, self.__zombie.jmeno),"green")
                self.__zombie.prepad(self.hrdinka, kostka)
                self.hrdinka.bitva(self.__zombie, self.__druha_zombie, kostka)
            else:
                print("Už tu nic zajímavého není.")
        else:
            print("Už tu nic zajímavého není.")
    def utok_skrz(self):
        if self.plnost:
            if self.__zombie.nazivu:
                print("Za {0} je {1}".format(self.jmeno, self.__zombie.jmeno()))
                self.hrdinka.prepad(self.__zombie, self.__kostka)
                self.hrdinka.bitva(self.__zombie, self.__druha_zombie, self.__kostka)
            else:
                print("Čepel se zabodla do mrtvé zombie.")
        else:
            print("Už tu nic zajímavého není.")
class Pokladnice(Ukryt):
    def __init__(self, jmeno, zombie, petlice, hrdinka, plny, kostka, druha_zombie, poklad):
        super().__init__(jmeno, zombie, petlice, hrdinka, plny, kostka, druha_zombie)
        self.__poklad = poklad
    def utok_skrz(self):
        if self.__poklad.pritomnost:
            if self.__poklad.rozbitost:
                print("Zbraň jen pohnula s pár {0}.".format(self.__poklad.strepy))
            else:
                self.__poklad.rozbiti(self.hrdinka)
        else:
            print("Už tu nic zajímavého není.")
    def otevreni_dvirek(self):
        if self.__poklad.pritomnost:
            if self.__poklad.rozbitost:
                print("Jsou tu jen {0}.".format(self.__poklad.strepy))
            else:
                self.__poklad.vzeti(self.hrdinka)
        else:
            print("Nic zajímavého tu není.")
