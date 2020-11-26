#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
class Cutscena:
    def __init__(self, uvod, zadani, priprava, zahrada, mistnost, hrdinka, konec_smrt, konec_utek, konec_poprava, konec_zaplaceni, konec_dluh, konec_ocosteni, odmena, obsah_dopisu):
        self.__uvod = uvod
        self.__zadani = zadani
        self.__priprava = priprava
        self.__zahrada = zahrada
        self.__mistnost = mistnost
        self.__hrdinka = hrdinka
        self.__konec_smrt = konec_smrt
        self.__konec_utek = konec_utek
        self.__konec_poprava = konec_poprava
        self.__konec_zaplaceni = konec_zaplaceni
        self.__konec_dluh = konec_dluh
        self.__konec_ocosteni = konec_ocosteni
        self.__odmena = odmena
        self.__obsah_dopisu = obsah_dopisu
    def konec(self):
        if self.__hrdinka.nazivu and self.__hrdinka.dokonceni:
            print("Pomalu se vracela do města a přemítala o tomto zážitku. Napadlo ji, co je asi v těch dopisech. Byla\n tma, takže člověk nemohl na čtení ani pomyslet. Ale ona nebyla člověk.")
            cprint("Chceš si přečíst dopisy? Stiskni A. Pokud nechceš, stiskni N.", "green")
            precist = input()
            if precist == "A":
                print(self.__obsah_dopisu)
                cprint("Chceš oznámit tuhle věc, předat svého zákazníka k potrestání? Pokud ano, stiskni A, pokud ne, stiskni N.", "green")
                zradit = input()
            else:
                zradit = "N"
            if self.__hrdinka.smrt == False and zradit == "A":
                print(self.__konec_ocosteni)
                if self.__hrdinka.vypis_pocitadla == 8:
                    print(self.__odmena)
            elif self.__hrdinka.smrt == False:
                print(self.__konec_zaplaceni)
            elif zradit == "A":
                print(self.__konec_dluh)
            else:
                print(self.__konec_poprava)
        elif self.__hrdinka.nazivu:
            print(self.__konec_utek)
        else:
            print(self.__konec_smrt)
    def vstup(self):
        print(self.__uvod)
        cprint("Stiskni Enter.", "green")
        input()
        print(self.__zadani)
        cprint("Stiskni Enter.", "green")
        input()
        print(self.__priprava)
        cprint("Stiskni Enter.", "green")
        input()
        print(self.__zahrada)
        cprint("Stiskni Enter.", "green")
        input()
    def hra(self):
        self.vstup()
        self.__mistnost.vstup()
        self.konec()
