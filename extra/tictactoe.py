#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:07:33 2024

@author: alexa
"""

# tic tac toe

# 1. Brett erstellen
def brett_erstellen():
    brett = []
    spieler ="X"
    for i in range(3):
        zeile = [" ", " ", " "]
        brett.append(zeile)
    return brett, spieler


# 2. Brett hübsch drucken
def brett_drucken(brett):
    for zeile in brett:
        print("|".join(zeile))
        print("-----")

# 3. Zug machen
def zug(brett, spieler):
    print(f"Hey Spieler {spieler}")
    while True:  # Schleife bis gültiger Input erfolgt
       try:
           zeile = int(input("Welche Zeile? (0-2) "))
           spalte = int(input("Welche Spalte? (0-2) "))
           
           # gültiger Bereich?
           if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
               print("Ungültige Eingabe. Zahlen müssen zwischen 0 und 2 liegen.")
               continue
           
           # Feld frei?
           if brett[zeile][spalte] != " ":
               print("Dieses Feld ist bereits belegt! Wähle ein anderes.")
               continue
           
           # falls gültiger Zug
           brett[zeile][spalte] = spieler
           break  # Schleife beenden
       except ValueError:  # Falls der Nutzer keine Zahl eingibt
           print("Bitte gib Zahlen zwischen 0 und 2 ein!")
    return brett

# 4. Gewinn prüfen
def gewinn_test(brett, spieler):
    for zeile in brett: # testet horizontal
        if "".join(zeile) == 3*spieler:
            print(f"{spieler} hat gewonnen h")
            return True
    for spalte in range(3): #testet vertikal
        erste_elements = [zeile[spalte] for zeile in brett]
        if "".join(erste_elements) == 3*spieler:
            print(f"{spieler} hat gewonnen v")
            return True
    if spieler == brett[0][0] == brett[1][1] == brett[2][2]:
        print(f"{spieler} hat gewonnen d1")
        return True
    elif spieler == brett[2][0] == brett[1][1] == brett[0][2]:
        print(f"{spieler} hat gewonnen d2")
        return True
    else:
        return False

# 5. Unentschieden prüfen
def unentschieden_test(brett, spieler):
    for zeile in brett:
        if " " not in zeile:
            print("Unentschieden!")
            return True
        else:
            return False
        
# 6. Spieler wechsel
def spieler_wechsel(spieler):
    if spieler == "X":
        spieler = "O"
    else:
        spieler = "X"
    return spieler
        

# main game
def tictactoe():
    brett, spieler = brett_erstellen()
    gewinn = False
    unentschieden = False
    while gewinn == False and unentschieden == False:
        brett = zug(brett, spieler)
        brett_drucken(brett)
        gewinn = gewinn_test(brett, spieler)
        unentschieden = unentschieden_test(brett, spieler)
        spieler = spieler_wechsel(spieler)

tictactoe()        

