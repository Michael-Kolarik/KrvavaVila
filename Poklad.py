#!/usr/bin/env python3

class Poklad:
    def __init__(self, pritomnost, rozbitost, vzeti, rozbiti, efekt, popis_efektu, strepy):
        self.__pritomnost = pritomnost
        self.__rozbitost = rozbitost
        self.__vzeti = vzeti
        self.__rozbiti = rozbiti
        self.__efekt = efekt
        self.__popis_efektu = popis_efektu
        self.__strepy = strepy
    @property
    def rozbitost(self):
        return self.__rozbitost
    @property
    def pritomnost(self):
        return self.__pritomnost
    @property
    def strepy(self):
        return self.__strepy
    def vzeti(self, hrdinka):
        print(self.__vzeti)
        self.__pritomnost = False
        if self.__efekt == "zbroj":
            hrdinka.zmena_zbroje()
        if self.__efekt == "lektvar":
            hrdinka.leceni()
            hrdinka.graficky_zivot()
    def rozbiti(self, postava):
        print(self.__rozbiti)
        self.__rozbitost = True
        if self.__efekt == "zbroj":
            print(self.__vzeti)
            postava.zmena_zbroje()
            self.__pritomnost = False