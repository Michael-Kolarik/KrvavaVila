#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
from Kostka import Kostka
class Hrdinka:  # Tahle třída je pro hlavní postavu
    def __init__(self, jmeno, utocne_cislo, obranne_cislo, zraneni, zivoty, poloha, inventar, druha_ruka, zakerny_utok,
                 kostka, hadanka, prevlekani):
        self.__jmeno = jmeno
        self.__zivoty = zivoty
        self.__maxzivot = zivoty
        self.__utocne_cislo = utocne_cislo
        self.__obranne_cislo = obranne_cislo
        self.__kostka = kostka
        self.__zraneni = zraneni
        self.__poloha = poloha
        self.__inventar = inventar
        self.__druha_ruka = druha_ruka
        self.__zakerny_utok = zakerny_utok
        self.__pocitadlo = 0
        self.__hotovo = False
        self.__zabit = False
        self.__hadanka = hadanka
        self.__prevlekani = prevlekani
        # Definuje vstupy

    @property
    def jmeno(self):
        return str(self.__jmeno)  # vypisuje jmeno

    @property
    def nazivu(self):
        return self.__zivoty > 0  # Zjistí jestli bojovík žije

    def obrana(self, zasah, poskozeni):
        if zasah >= self.__obranne_cislo:
            print("Rána elfku řádně zabolela")
            if self.__zakerny_utok:
                poskozeni = poskozeni/2
            self.__zivoty = self.__zivoty - poskozeni
        else:
            print("Mezzobran se mrštně vyhnula útoku.")
        cprint(self.graficky_zivot(), "red")
        if self.__zivoty < 0:
            self.__zivoty = 0

    def utok(self, souper, volba, kostka):
        if volba == "U":
            print("Mezzobran obratně zaútočila.")
            if self.__obranne_cislo > 18:
                self.__obranne_cislo = self.__obranne_cislo - 5
            hod_na_utok = kostka.hod() + self.__utocne_cislo + 3
            sestistenka = Kostka(6)
            kostka_zraneni = Kostka(self.__zraneni)
            druha_kostka_zraneni = Kostka(self.__druha_ruka)
            hod_na_zraneni = kostka_zraneni.hod() + self.__utocne_cislo + druha_kostka_zraneni.hod()
            if self.__zakerny_utok:
                hod_na_zraneni = hod_na_zraneni + sestistenka.hod() + sestistenka.hod()
            souper.obrana(hod_na_utok, hod_na_zraneni)
        else:
            print("Elfka zaujala obranný postoj.")
            if self.__obranne_cislo < 18:
                self.__obranne_cislo = self.__obranne_cislo + 5

    def souboj(self, protivnik, kostka, volba):

        if kostka.hod() + protivnik.iniciativa <= 16:
            self.utok(protivnik, volba, kostka)
            if protivnik.nazivu:
                protivnik.utok(self, kostka)
        else:
            protivnik.utok(self, kostka)
            if self.nazivu:
                self.utok(protivnik, volba, kostka)

    def prepad(self, cil, kostka):
        hod_na_utok = kostka.hod() + self.__utocne_cislo + 2
        sestistenka = Kostka(6)
        kostka_zraneni = Kostka(self.__zraneni)
        druha_kostka_zraneni = Kostka(self.__druha_ruka)
        hod_na_zraneni = kostka_zraneni.hod() + self.__utocne_cislo + druha_kostka_zraneni.hod() + sestistenka.hod() + sestistenka.hod()
        cil.obrana(hod_na_utok, hod_na_zraneni)

    def boj_s_presilou(self, protivnik1, protivnik2, kostka, volba):

        hod_na_iniciativu = protivnik1.iniciativa + kostka.hod()
        self.overeni_zakerneho_utoku(False)
        if volba == "1":
            if hod_na_iniciativu > 15:
                protivnik2.utok(self, kostka)
            self.souboj(protivnik1, kostka, volba)
            if hod_na_iniciativu <= 15:
                protivnik2.utok(self, kostka)
        elif volba == "2":
            if hod_na_iniciativu > 15:
                protivnik1.utok(self, kostka)
            self.souboj(protivnik2, kostka, volba)
            if hod_na_iniciativu <= 15:
                protivnik1.utok(self, kostka)
        else:
            self.utok(protivnik1, volba, kostka)
        self.overeni_zakerneho_utoku(True)

    def bitva(self, nepritel1, nepritel2, kostka):
        while nepritel1.nazivu or nepritel2.nazivu:
            if nepritel1.nazivu and nepritel2.nazivu:
                cprint("Pokud chceš zaútočit na dívku pokrytou jinovatkou, stiskni 1, pokud na chlapce v livreji, stiskni 2, pokud se chceš pouze bránit, stiskni O", "green")
                volba = input()

                self.boj_s_presilou(nepritel1, nepritel2, kostka, volba)
            elif nepritel1.nazivu:
                cprint("Pokud chceš útočit, stiskni U, pokud se chceš jenom bránit, stiskni O", "green")
                volba = input()
                self.souboj(nepritel1, kostka, volba)
            else:
                cprint("Pokud chceš útočit, stiskni U, pokud se chceš jenom bránit, stiskni O", "green")
                volba = input()
                self.souboj(nepritel2, kostka, volba)
        if self.__obranne_cislo > 18:
            self.__obranne_cislo = self.__obranne_cislo - 5

    def poloha(self, pokoj):
        self.__poloha = pokoj

    @property
    def lokalizace(self):
        return self.__poloha

    def overeni_zakerneho_utoku(self, ZU):
        self.__zakerny_utok = ZU
    @property
    def inventar(self):
        return self.__inventar

    def sebrani_veci(self, vec):
        print("Zlodějka našla", vec)
        self.__inventar.append(vec)
        if vec == "rapír a dýku.":
            print(self.__prevlekani)
            self.__zraneni = 8
            self.__druha_ruka = 4
        if vec == "učebnici.":
            self.hadanka()

    def pocitadlo(self, duch):
        if duch.pritomnost == False:
            self.__pocitadlo = self.__pocitadlo + 1
            if duch.jmeno == "Trezor":
                self.__inventar.append("dopisy")
                self.hotovo()

    def hotovo(self):
        self.__hotovo = True

    @property
    def dokonceni(self):
        return self.__hotovo

    @property
    def vypis_pocitadla(self):
        return self.__pocitadlo

    def hadanka(self):
        print(self.__hadanka)
        cprint("chceš řešit hádanku? Stiskni A. Pokud nechceš, stiskni N.","green")
        rozhodnuti = input()
        while rozhodnuti == "A":
            cprint("Napiš odpověď", "green")
            odpoved = input()
            if odpoved == "4":
                print("\'To je správně,\' řekla mluvící učebnice.")
                rozhodnuti = "N"
                self.__inventar.append("odpověď")
            else:
                print("\'To je špatně,\' řekla mluvící učebnice.")
                rozhodnuti = input()

    def zabiti(self):
        self.__zabit = True
    @property
    def smrt(self):
        return self.__zabit
    def graficky_zivot(self):
        ukazatel = "["
        for i in range(self.__maxzivot):
            if i < self.__zivoty:
                ukazatel=ukazatel+"♥"
            else:
                ukazatel = ukazatel + " "
        ukazatel=ukazatel+"]"
        return ukazatel #vypisuje HP
    def zmena_zbroje(self):
        self.__obranne_cislo = self.__obranne_cislo + 1
    def leceni(self):
        ctyrstenka = Kostka(4)
        lecba = ctyrstenka.hod() + ctyrstenka.hod() + 2
        self.__maxzivot = self.__maxzivot + lecba
        self.__zivoty = self.__zivoty + lecba