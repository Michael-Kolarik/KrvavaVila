#!/usr/bin/env python3
import sys
from termcolor import colored, cprint
from Dvere import Dvere
from Kostka import Kostka
kostka = Kostka(20)
class Mistnost:  # Tahle třída slouží k vytvoření jednotlivých místností vily
    def __init__(self, duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka):
        self.duch = duch
        self.zombie = zombie
        self.dvere = dvere
        self.__poklad = poklad
        self.ukryt = ukryt
        self.popis = popis
        self.__nazev = nazev
        self.hrdinka = hrdinka
        self.druha_zombie = druha_zombie
        self.__kostka = kostka


    def nazev(self):
        return self.__nazev
    @property
    def poklad(self):
        return self.__poklad

    def vstup(self):
        print(self.popis)
        if self.duch.pritomnost:
            print(self.duch.__str__())
        if self.zombie.nazivu:
            print(self.zombie.__str__())
            self.hrdinka.bitva(self.zombie, self.druha_zombie, self.__kostka)
        self.zustat()

    def zustat(self):
        volba = "G"
        while volba != "J":
            if self.hrdinka.nazivu:
                self.vypis_moznosti()
                volba = input()
            else:
                volba = "J"
            if volba == "R":
                if self.bezpecno:
                    self.duch.rozhovor(self.hrdinka)
                    self.hrdinka.pocitadlo(self.duch)
                else:
                    self.prepadeni_zombii()
            elif volba == "P":
                if self.bezpecno:
                    self.hrdinka.sebrani_veci(self.__poklad)
                    self.__poklad = "Nic"
                else:
                    self.prepadeni_zombii()
            elif volba == "Z":
                self.otevreni_ukrytu()
            elif volba == "H":
                self.hrdinka.hadanka()
        if self.hrdinka.nazivu:
            self.odchod()

    def odchod(self):
        self.dvere.pruchod(self.hrdinka)

    def vypis_moznosti(self):
        cprint("Zvol další postup:", "green")
        if self.duch.pritomnost:
            cprint("{0}, pak stiskni R".format(self.duch.prikaz),"green")
        if self.ukryt.jmeno != "Nic":
            self.vypis_ukrytu()
        if self.__poklad != "Nic":
            cprint("Pokud chceš prohledat místnost, stiskni P", "green")
        if "učebnici." in self.hrdinka.inventar:
            if "odpověď" in self.hrdinka.inventar:
                x = "X"
            else:
                cprint("Pokud chceš luštit hádanku, stiskni H","green")
        cprint("Pokud chceš jít jinam, stiskni J", "green")

    def prepadeni_zombii(self):
        self.zombie = self.ukryt.ukryta_zombie()
        self.ukryt.vyprazdneni()
        self.zombie.prepad(self.hrdinka,kostka)
        self.hrdinka.bitva(self.zombie, self.druha_zombie, kostka)

    def vypis_ukrytu(self):
        cprint("Pokud se chceš zaměřit na {0}, stiskni Z".format(self.ukryt.jmeno), "green")

    @property
    def bezpecno(self):
        return self.ukryt.jmeno == "Nic" or self.ukryt.nazivu == False or self.ukryt.zamcene_dvere == True or self.ukryt.plnost == False

    def otevreni_ukrytu(self):
        self.ukryt.otevreni()
    def predefinovani_dveri(self, dvere):
        self.dvere = dvere


class Hala(Mistnost):  # Tahle třída je pro pokoje s mnoha dveřmi
    def __init__(self, duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka,
                 druhe_dvere,
                 treti_dvere, ctvrte_dvere, pate_dvere, skryte_dvere):
        super().__init__(duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka)
        self.__druhe_dvere = druhe_dvere
        self.__treti_dvere = treti_dvere
        self.__ctvrte_dvere = ctvrte_dvere
        self.__pate_dvere = pate_dvere
        self.__skryte_dvere = skryte_dvere
        self.dvere = Dvere

    def odchod(self):
        if self.dvere.popis != "Neexistuje":
            cprint("Pokud chceš použít {0}, stiskni 1".format(self.dvere.popis), "green")
        if self.__druhe_dvere.popis != "Neexistuje":
            cprint("Pokud chceš použít {0}, stiskni 2".format(self.__druhe_dvere.popis), "green")
        if self.__treti_dvere.popis != "Neexistuje":
            cprint("Pokud chceš použít {0}, stiskni 3".format(self.__treti_dvere.popis), "green")
        if self.__ctvrte_dvere.popis != "Neexistuje":
            cprint("Pokud chceš použít {0}, stiskni 4".format(self.__ctvrte_dvere.popis), "green")
        if self.__pate_dvere.popis != "Neexistuje":
            cprint("Pokud chceš použít {0}, stiskni 5".format(self.__pate_dvere.popis), "green")
        if self.__skryte_dvere.popis != "Neexistuje" and self.__skryte_dvere.objev in self.hrdinka.inventar:
            cprint("Pokud chceš použít {0}, stiskni S".format(self.__skryte_dvere.popis), "green")
        vyberd = input()
        if vyberd == "1":
            self.dvere.pruchod(self.hrdinka)
        elif vyberd == "2":
            self.__druhe_dvere.pruchod(self.hrdinka)
        elif vyberd == "3":
            self.__treti_dvere.pruchod(self.hrdinka)
        elif vyberd == "4":
            self.__ctvrte_dvere.pruchod(self.hrdinka)
        elif vyberd == "5":
            self.__pate_dvere.pruchod(self.hrdinka)
        elif vyberd == "S":
            self.__skryte_dvere.pruchod(self.hrdinka)
        else:
            self.zustat()

    def predefinovani_dalsich_dveri(self, druhe_dvere, treti_dvere, ctvrte_dvere, pate_dvere, skryte_dvere):
        self.__druhe_dvere = druhe_dvere
        self.__treti_dvere = treti_dvere
        self.__ctvrte_dvere = ctvrte_dvere
        self.__pate_dvere = pate_dvere
        self.__skryte_dvere = skryte_dvere


class Kuchyne(Mistnost):  # Tahle třída je pro speciální případ místnosti
    def __init__(self, duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka,
                 druhy_ukryt,
                 vytah):
        super().__init__(duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka)
        self.__druhy_ukryt = druhy_ukryt
        self.__vytah = vytah

    def prepadeni_zombii(self):
        if self.vyreseni_prvniho == False:
            self.zombie = self.ukryt.ukryta_zombie()
            self.ukryt.vyprazdneni()
            self.zombie.prepad(self.hrdinka, kostka)
        if self.vyreseni_druheho == False:
            self.__druha_zombie = self.__druhy_ukryt.ukryta_zombie()
            self.__druhy_ukryt.vyprazdneni()
            self.__druha_zombie.prepad(self.hrdinka, kostka)
        self.hrdinka.bitva(self.zombie, self.__druha_zombie, kostka)

    def predefinovani_vytahu(self, vytah):
        self.__vytah = vytah

    def vypis_ukrytu(self):
        cprint("Pokud se chceš zaměřit na {0} nebo {1}, stiskni Z".format(self.ukryt.jmeno, self.__druhy_ukryt.jmeno),
               "green")

    @property
    def vyreseni_prvniho(self):
        return self.ukryt.nazivu == False or self.ukryt.zamcene_dvere == True or self.ukryt.plnost == False

    @property
    def vyreseni_druheho(self):
        return self.__druhy_ukryt.nazivu == False or self.__druhy_ukryt.zamcene_dvere == True or self.__druhy_ukryt.plnost == False

    @property
    def bezpecno(self):
        return self.vyreseni_druheho and self.vyreseni_prvniho

    def otevreni_ukrytu(self):
        cprint("Pokud se chceš zabývat malými dvířky, stiskni D, pokud poklopem, stiskni P.", "green")
        volba = input()
        if volba == "D":
            self.ukryt.otevreni()
        if volba == "P":
            self.__druhy_ukryt.otevreni()

    def odchod(self):
        if "výtah." in self.hrdinka.inventar:
            cprint("chceš odejít dveřmi, nebo výtahem? Stiskni D nebo V", "green")
            volba = input()
            if volba == "D":
                self.dvere.pruchod(self.hrdinka)
            else:
                self.__vytah.pruchod(self.hrdinka)
        else:
            self.dvere.pruchod(self.hrdinka)


class Jidelna(Mistnost):  # Tahle třída je pro speciální případ místnosti
    def __init__(self, duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka,
                 vytah):
        super().__init__(duch, zombie, poklad, ukryt, popis, nazev, hrdinka, dvere, druha_zombie, kostka)
        self.__poprve = True
        self.__vytah = vytah

    def vstup(self):
        if self.__poprve:
            print(self.popis)
            print(self.duch.__str__())
            self.duch.rozhovor(self.hrdinka)
            if self.duch.uspokojeni() == False:
                print("Mezzobran vytáhla zbraň a bodla ženu do srdce. Byla tak zesláblá, se ani nepokusila uhnout.")
                self.hrdinka.zabiti()
                self.duch.uspokojeni()
            else:
                self.duch.uspokojeni()
                self.hrdinka.pocitadlo(self.duch)
            print(
                "Z úst ženě vystoupal zelený dým, který se zformoval do podoby tvora s tělem ropuchy, lidskou\n hlavou s kozlími růžky, končetinami opice a ocasem škorpiona.\n\'Tak to ty to tu máš na svědomí?\'\n\'Tak to ty mi tu překážíš,\' zasyčel démon, \'to tě bude mrzet.\'\nMísto odpovědi mu namířila hrot zbraně na tělo.")
            while self.hrdinka.nazivu and self.zombie.nazivu:
                if kostka.hod() + self.zombie.iniciativa <= 16:
                    cprint("Pokud chceš útočit, stiskni U, pokud se chceš jenom bránit, stiskni O", "green")
                    volba = input()
                    self.hrdinka.utok(self.zombie, volba, kostka)
                    if self.zombie.nazivu:
                        self.zombie.utok(self.hrdinka, kostka)
                else:
                    self.zombie.utok(self.hrdinka, kostka)
                    cprint("Pokud chceš útočit, stiskni U, pokud se chceš jenom bránit, stiskni O", "green")
                    volba = input()
                    if self.hrdinka.nazivu:
                        self.hrdinka.utok(self.zombie, volba, kostka)
            if self.hrdinka.nazivu:
                print(
                    "Mezzobran těžce vydechla, otřela z ostří zelenou krev, vyměnila bojové vybavení za zlodějské a\n pomocí paklíčů odemkla dveře jídelny.")
                print("Potom prohledala ženu zhroucenou u stolu.")
                self.hrdinka.sebrani_veci(self.poklad)
                self.dvere.odblokovani()
                cprint("Chceš odejít dveřmi, nebo výtahem? Stiskni D nebo V.", "green")
                volba = input()
                if volba == "D":
                    self.dvere.pruchod(self.hrdinka)
                else:
                    self.__vytah.pruchod(self.hrdinka)
        else:
            cprint("Chceš odejít dveřmi, nebo výtahem? Stiskni D nebo V.", "green")
            volba = input()
            if volba == "D":
                self.dvere.pruchod(self.hrdinka)
            else:
                self.__vytah.pruchod(self.hrdinka)

    def predefinovani_vytahu(self, vytah):
        self.__vytah = vytah
