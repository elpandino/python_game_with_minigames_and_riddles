#https://github.com/elpandino/python_game_with_minigames_and_riddles.git
#Copyright to Andrea Pandolfini and Leonardo Muschietti Aka. @elpandino @ermuschio
import curses
import random
import time
import os
import pickle
import bisect
import sqlite3
import sys
from copy import deepcopy
from random import randint
from typing import List, Tuple
from random import choice
from turtle import *
from freegames import floor, vector
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("copyright to Andrea Pandolfini and Leonardo Muschietti")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
license = input(
    "Ti informiamo che dal momento in cui questo codice ?? sotto |Copiright 2021|?? ??? e |Licenza moss-pands|, dunque non potrai n?? copiarlo n?? spacciarlo come un codice tuo; acconsenti dunque alla policy? (Ricordiamo che per noi la lettura di della licenza e dei termini di condizione sono molto importanti, inoltre ci sono terze parti a nostra tutela)      si/no       "
)
if license == "si":
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Molto bene, procediamo...")
    print(" ")
    print(" ")
    gfyhguyojuifr = input("Premi invio per iniziare...")
else:
    print(" ")
    print(" ")
    print(
        "Mi dispiace ma ti ?? stato privato di utilizzare il codice e il gioco, (ricordiamo che OpenSource non ?? uguale a il codice ?? mio) grazie e arrivederci; PROCESSO AUTODISTRUZIONE DEL CODICE ATTIVATA                                                                                                                     BOOM"
    )
    exit()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("                 NEL 2021         ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
ghjkgyjiwsksghg = input("Premi invio per continuare...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" DIRETTAMENTE DALL'ITALIA ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
ghjkgyujiwsksghg = input("Premi invio per continuare...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(
    "IL NUOVISSIMO GIOCO TARGATO MossPands, DIRETTAMENTE A CASA VOSTRA SUL VOSTRO DISPOSITIVO"
)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
ghjkgyjiwsksghg = input("Premi invio per continuare...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
hihcf = input("Premi invio per iniziare a giocare...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Tutto nacque un sabato sera, quando tu e la tua migliore amica Ely, volevate divertirvi, e lei ti ha portato in un nuovo posto, visto che ti sei appena trasferito in una nuova citt??, Ely ?? una tua amica, ma tu speri in qualcos'altro... Insieme a voi ?? venuto anche Paolo, un vostro amico, ma tra una birra e l'altra perdi la cognizione del tempo e ti svegli a casa senza ricordi della sera.")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
zero = input("Premi invio per continuare la storia...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
#INZIOGIOCO
print(
    "                           LO SCHERLOCK HOLMES DEGLI INDOVINELLI                         "
)
print(" ")
print(" ")
primo = input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Hey non ti avevo visto arrivare, sei nuovo da queste parti?")
print(" ")
print(" ")
secondo = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    "Io : si sono arrivat* poco tempo fa, ho solo un'amica, lei si chiama Ely ."
)
print(" ")
print(" ")
re = input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Facciamo qualche domanda per conoscerci meglio")
print(" ")
print(" ")
re = input("Premi invio per continuare... ")
print(" ")
print(" ")
#DOMANDE ALL'UTENTE
sesso = input("Computer : Sei Maschio o Femmina? m/f/no      ")
print(" ")
print(" ")
bimbo = input("Computer : Come ti chiami? (METTI SOLO IL NOME )       ")
print(" ")
bimbetto = bimbo.title()
print(" ")
if len(bimbetto) > 6:
    print("i tuoi genitori potevano farlo pi?? corto?")
    print(" ")
    print("Perci?? penso proprio che ti chiamero pinco, o forse no???")
    print("vabbe per rispetto ti chiamero con il tuo vero nome")
    print(" ")
if bimbo == "pinco":
    print(" ")
    bimbetto = "pinco nei tuoi sogni"
    print("seeee, e allora io sono pallino")
if bimbo == "Gumball":
    print(" ")
    bimebetto = "Gumball nei tuoi sogni"
    print("seeee, e allora io sono Darwin")
    print(" ")
if bimbo == "Finn":
    print(" ")
    bimebetto = "Finn nei tuoi sogni"
    print("seeee, e allora io sono jake")
    print(" ")
if bimbo == "Moritz":
    print(" ")
    bimebetto = "Moritz nei tuoi sogni"
    print("seeee, e allora io sono Lennard")
    print(" ")
if bimbo == "Jake":
    print(" ")
    bimbetto = "Jake nei tuoi sogni"
    print("seeee, e allora io sono Finn")
    print(" ")
if bimbo == "Goku":
    print(" ")
    bimebetto = "Goku nei tuoi sogni"
    print("seeee, e allora io sono Vegeta")
    print(" ")
if bimbo == "Franklin":
    print(" ")
    bimebetto = "Franklin nei tuoi sogni"
    print("seeee, e allora io sono Michael")
    print(" ")
if bimbo == "":
    print(" ")
    bimebetto = "Ulisse nei tuoi sogni"
    print("seeee, e allora io sono Nessuno")
    print(" ")
    print("ma stai zitto e gioca nulla")
    print(" ")
if sesso == "m":
    bimbone = len(bimbetto) + 2
    print(" ")
    print(" ")
    print("Vabbene signorino, piacere...")
    print(" ")
    print("???" + "???" * bimbone + "???")
    print("???", bimbetto, "???")
    print("???" + "???" * bimbone + "???")
elif sesso == "f":
    bimbone = len(bimbetto) + 2
    print(" ")
    print(" ")
    print("Vabbene signorina, piacere...")
    print(" ")
    print("???" + "???" * bimbone + "???")
    print("???", bimbetto, "???")
    print("???" + "???" * bimbone + "???")
elif sesso == "no":
    bimbone = len(bimbetto) + 2
    print(" ")
    print(" ")
    print("Vabbene personaccia, piacere...")
    print(" ")
    print("???" + "???" * bimbone + "???")
    print("???", bimbetto, "???")
    print("???" + "???" * bimbone + "???")
else:
    bimbone = len(bimbetto) + 2
    print(" ")
    print(" ")
    print("Vabbene..., piacere...?!")
    print(" ")
    print("???" + "???" * bimbone + "???")
    print("???", bimbetto, "???")
    print("???" + "???" * bimbone + "???")
print(" ")
print("Computer : che figata di nome : stupendo")
print(" ")
print(" ")
rqe = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    "Computer : Dunque, tu devi sapere che Ely ?? scomparsa e l'ultima persona che l'ha vista ?? Paolo e per raggiungerlo, se vorrai parlarci, dovrai affrontare alcune sfide, create da me."
)
print(" ")
print(" ")
rye = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(bimbetto, " : Aspetta ma perch?? fatti da te?  ")
print(" ")
print(" ")
rle = input("Premi invio per continuare... ")
print(" ")
print(" ")
print("Computer : Okay, mi hai scoperto ,l'ho rapita io............ ")
print(" ")
print(" ")
rre = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    "Computer : Sono gentile, ti far?? sentire il suo l'ultimo messaggio vocale, era indirizzato a te... sappi per?? che ora te la dovrai vedere con me!!!"
)
print(" ")
print(" ")
rhe = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    "Ely : Non sar?? io a guidarti, ma uno dei miei amici, ADDIO, forse un giorno ci rincontreremo."
)
print(" ")
print(" ")
rse = input("Premi invio per continuare... ")
print(" ")
print(" ")
gine = input("Scrivi il nome che vorresti che avesse la tua guida :   ")
print(" ")
gine = gino.title()
if gino == "Ely":
    print(" ")
    print("MI dispiace ma ?? impossibile")
    print(" ")
    print(" ")
    print("Digita un nome reale...")
    print(" ")
    gino = input(" ")
    print(" ")
print(" ")
rdfge = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    gino,
    " : Perfetto d'ora in poi non potrai pi?? tirarti indietro, se pensi di non potercela fare chiudi il gioco, non cerchiamo persone deboli..."
)
print(" ")
print(" ")
rwe = input("Premi invio per continuare... ")
print(" ")
print(" are yuo stipig or dumg")
print(
    gino,
    " : Via con il primo indovinello, e ricordati che a ogni errore dovrai ricominciare"
)
print(" ")
print(" ")
klre = input("Premi invio per continuare... ")
print(" ")
print(" ")
sgg = input(
    "Computer : Se la usi ha sei gambe, altrimenti ne ha quattro, che cos'??? (scrivi solo il nome tutto in minuscolo) : "
)
print(" ")
print(" ")
if sgg == "sedia":
    print(gino, " : RISPOSTA CORRETTA, COMPLIMENTI!!! ")
else:
    print(
        gino,
        " : MI DISPIACE LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'sedia'"
    )
    print("                               GAME OVER")
    print(" ")
    print(" ")
    kqlrre = input("Premi invio per finire... ")
    exit()
print(" ")
print(" ")
kqlre = input("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    gino,
    " : Via con il secondo indovinello, altro giro altra corsa................... "
)
print(" ")
print(" ")
klsre = input("Premi invio per continuare... ")
print(" ")
print(" ")
fjyf = input(
    "Computer : Cos'?? che ?? caldo quando ?? fresco? (scrivi solo il nome in minuscolo) : "
)
print(" ")
print(" ")
if fjyf == "pane":
    print(gino, "RISPOSTA CORRETTA, COMPLIMENTI!!!")
else:
    print(
        gino,
        "MI DISPIACE, LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'pane'"
    )
    print("            GAME OVER")
    sfd = input("Premi invio per finire...")
    exit()
print(" ")
print(" ")
print(gino,
      " : molto bene, adesso ti aspettera un momento ricreativo, sei pronto?")
print(" ")
print(" ")
fgfgfgfgfgfgfgfgfgfg = input("Premi invio per continuare...")
print(" ")
print(" ")
print(
    "Computer : solo per te ho trovato questo sudoku, sono sicuro che ti divertirai, sappi per?? che se non lo finisci rimarrai a questo livello"
)
print(" ")
print(" ")
gigghgh = input("Premi invio per continuare...")
print(" ")
print(" ")


#Arkanoid
class Block(object):
    """Store a single 3x3 block in the complete field."""
    def __init__(self):
        self._block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __setitem__(self, point, value):
        """Set the value, check that value is not already in the block."""
        # n == -n, as n < 0 means user generated abs(n).
        if abs(self._block[point[1] + 3 * point[0]]) == abs(value):
            self._block[point[1] + 3 * point[0]] = value
            return
        if value != 0 and (value in self._block or -value in self._block):
            raise ValueError("Block already contains %d" % value)
        self._block[point[1] + 3 * point[0]] = value

    def __getitem__(self, point):
        """Return the value at the given point."""
        return self._block[point[1] + 3 * point[0]]


class Block(object):
    """Store a single 3x3 block in the complete field."""
    def __init__(self):
        self._block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __setitem__(self, point, value):
        """Set the value, check that value is not already in the block."""
        # n == -n, as n < 0 means user generated abs(n).
        if abs(self._block[point[1] + 3 * point[0]]) == abs(value):
            self._block[point[1] + 3 * point[0]] = value
            return
        if value != 0 and (value in self._block or -value in self._block):
            raise ValueError("Block already contains %d" % value)
        self._block[point[1] + 3 * point[0]] = value

    def __getitem__(self, point):
        """Return the value at the given point."""
        return self._block[point[1] + 3 * point[0]]


class Sudoku(object):
    def __init__(self):
        self._field = [Block() for i in range(9)]
        # Cached values used in solve() and populate()
        self._values = list(range(1, 10))
        self._points = [(x, y) for y in range(9) for x in range(9)]

    def clear(self):
        """Reset the game to empty."""
        for b in self._field:
            b._block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def candidates(self, point):
        """Return all candidates at the point (x, y)."""
        candidates = set()
        previous = self[point]
        for i in self._values:
            try:
                self[point] = i
            except ValueError:
                pass
            else:
                candidates.add(i)
        self[point] = previous
        return candidates

    def populate(self, n=36):
        """Populate ca. n fields of the Sudoku.
        Clear the Sudoku, run the solver using random values and
        remove as many values as possible.
        """
        # Randomize the list of points and values
        random.shuffle(self._points)
        random.shuffle(self._values)
        self.clear()
        self.solve()

        for point in self._points:
            if self[point] == 0:
                continue
            val = self[point]
            for v in self.candidates(point):
                if v == val:
                    continue
                self[point] = v
                if self.solve(True):
                    self[point] = val
                    break
            else:
                if (81 - sum(b._block.count(0) for b in self._field) < n):
                    self[point] = val
                    break
                self[point] = 0

        for point in self._points:
            self[point] *= -1

    def __str__(self):
        """Represent the Sudoku as a string (for debugging purposes)."""
        s = ""
        for y in range(9):
            for x in range(9):
                s += '%d ' % self[x, y]
                if (x + 1) % 3 == 0:
                    s += " "
            s += "\n"
            if (y + 1) % 3 == 0:
                s += "\n"
        return s.strip()

    def __getitem__(self, p):
        pb = (p[0] // 3, p[1] // 3)
        block = self._field[pb[1] + 3 * pb[0]]

        return block[p[0] % 3, p[1] % 3]

    def __setitem__(self, p, val):
        if self[p] < 0 and val >= 0:
            raise ValueError("Value at point %s is pre-defined" % str(p))
        if val != 0:
            for i in range(9):
                if i != p[1] and abs(self[p[0], i]) == abs(val):
                    raise ValueError("Already in column: %d" % val)
                if i != p[0] and abs(self[i, p[1]]) == abs(val):
                    raise ValueError("Already in row: %d" % val)

        pb = (p[0] // 3, p[1] // 3)
        block = self._field[pb[1] + 3 * pb[0]]

        block[p[0] % 3, p[1] % 3] = val

    def is_solved(self):
        return all(0 not in self._field[i]._block for i in range(0, 9))

    def solve(self, reset=False):
        """Solve the Sudoku.
        If 'reset' is True, just check whether the sudoku can be solved,
        after return the sudoku will be identical to before the call.
        """
        if self.is_solved():
            return True

        field = None
        for x in range(9):
            if field is not None:
                break
            for y in range(9):
                if self[x, y] == 0:
                    field = (x, y)
                    break

        if field is None:
            return True

        for new in self._values:
            try:
                self[field] = new
            except ValueError:
                continue
            else:
                if self.solve(reset):
                    if reset:
                        self[field] = 0
                    return True
                else:
                    self[field] = 0


class CursesUI(object):
    """Command-line 'curses' interface."""
    def __init__(self):
        self._screen = curses.initscr()
        self._sudoku = Sudoku()

        # Draw the borders
        self._screen.vline(0, 4 * 3 - 2, curses.ACS_VLINE, 2 * 9 - 1)
        self._screen.vline(0, 4 * 6 - 2, curses.ACS_VLINE, 2 * 9 - 1)
        self._screen.hline(2 * 3 - 1, 0, curses.ACS_HLINE, 4 * 9 - 3)
        self._screen.hline(2 * 6 - 1, 0, curses.ACS_HLINE, 4 * 9 - 3)
        self._screen.addch(2 * 3 - 1, 4 * 3 - 2, curses.ACS_PLUS)
        self._screen.addch(2 * 3 - 1, 4 * 6 - 2, curses.ACS_PLUS)
        self._screen.addch(2 * 6 - 1, 4 * 3 - 2, curses.ACS_PLUS)
        self._screen.addch(2 * 6 - 1, 4 * 6 - 2, curses.ACS_PLUS)
        self._draw_sudoku()
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(1)

    def __enter__(self, *a):
        return self

    def __exit__(self, *a):
        curses.nocbreak()
        self._screen.keypad(0)
        curses.echo()
        curses.endwin()

    def _draw_sudoku(self):
        for y in range(0, 9):
            for x in range(0, 9):
                value = self._sudoku[x, y]
                attr = curses.A_BOLD if value < 0 else 0
                # Mark cells with only one possible solution.
                #if len(self._sudoku.candidates((x,y))) == 1:
                #    attr  |= curses.A_UNDERLINE
                self._screen.addch(2 * y, 4 * x, ord('0') + abs(value), attr)

    def _print_string(self, string):
        self._screen.move(20, 0)
        self._screen.deleteln()
        self._screen.addstr(string)

    def _help(self):
        self._print_string("Commands: (q)uit, (p)opulate, (P)opulate, "
                           "(r)eset, (c)andidates, (s)olve")

    def main(self):
        x = 0
        y = 0
        self._help()
        while True:
            self._screen.move(y, x)
            c = chr(self._screen.getch())
            if c == ':':
                self._print_string(":")
                curses.echo()
                #self._screen.move(20, 0)
                c = self._screen.getstr()
                curses.noecho()
            if c == 'q':
                break  # Exit the while()
            elif c == 'h':
                self._help()
            elif c in ('p', 'P'):
                if c == 'P':
                    self._print_string("Enter number of fields: ")
                    curses.echo()
                    n = int(self._screen.getstr())
                    curses.noecho()
                else:
                    n = 36
                start = time.time()
                self._sudoku.populate(n)
                end = time.time()
                self._draw_sudoku()
                self._print_string("Populated with %d fields in %.3f seconds" %
                                   (n, end - start))
            elif c == 's':
                if not self._sudoku.solve():
                    self._print_string("Could not solve sudoku")
                self._draw_sudoku()
            elif c == 'r':
                self._sudoku = Sudoku()
                self._draw_sudoku()
            elif c == 'c':
                point = (x // 4, y // 2)
                self._print_string("Candidates for %s are: %s" %
                                   (point, self._sudoku.candidates(point)))
            elif c == chr(curses.KEY_LEFT):
                x -= x >= 4 and 4 or 0
            elif c == chr(curses.KEY_RIGHT):
                x += x + 4 < 4 * 9 and 4 or 0
            elif c == chr(curses.KEY_UP):
                y -= y >= 2 and 2 or 0
            elif c == chr(curses.KEY_DOWN):
                y += y + 2 < 2 * 9 and 2 or 0
            elif c in "0123456789":
                try:
                    self._sudoku[x // 4, y // 2] = ord(c) - ord('0')
                    self._screen.addch(y, x, c)
                    # If single-candidate cells should be highlighted, use the
                    # following instead of self._screen.addch():
                    #self._draw_sudoku()
                except Exception as e:
                    self._print_string(str(e))
                else:
                    if self._sudoku.is_solved():
                        self._print_string("Solved")
                    else:
                        self._print_string("")
            else:
                self._print_string("Error: Invalid command '%s'" % c)


if __name__ == '__main__':
    with CursesUI() as ui:
        ui.main()

print(" ")
print(" ")
domandaovvia = input(
    "Computer : non mi aspettavo che tu fossi cos?? tanto inteligente, comunque ti sei divertito?  si/si  "
)
print(" ")
print(" ")
print(
    "Computer : sono molto contento, ma adesso ti aspetta il terzo indovinello il quale aumenter?? di difficolt??!!!!"
)
print(" ")
print(" ")
h = input("Premi invio per continuare...")
print(" ")
print(" ")
print(gino, "via con il terzo indovinello, buona fortuna")
print(" ")
print(" ")
ballo = input(
    "Computer : non hanno lancette, ma fanno rumore allo scoccare di ogni ora, cosa sono? (scrivi solo il nome al plurale in minuscolo) :    "
)
print(" ")
print(" ")
if ballo == "campane":
    print(gino, "RISPOSTA CORRETTA, COMPLIMENTI!!!")
else:
    print(
        gino,
        "MI DISPIACE, LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'campane'"
    )
    print("         GAME OVER")
    exit()
print(" ")
print(" ")
print("Computer : okay, siamo solo agli inizi, ci sar?? modo di farti perdere")
print(" ")
print(" ")
ghuug = input("Premi invio per continuare...")
print(" ")
print(" ")
print(gino, " : Via con il quarto indovinello... ")
print(" ")
print(" ")
jygg0 = input(
    "Computer : Si spoglia quando ha freddo, che cos'??? (scrivi solo il nome in minuscolo) : "
)
print(" ")
print(" ")
if jygg0 == "albero":
    print(gino, "RISPOSTA CORRETTA, COMPLIMENTI!!! ")
else:
    print(
        gino,
        "MI DISPIACE, LA RISPOSTA NON E' CORRETTA, la risposta corretta era : 'albero'"
    )
    print("         GAME OVER")
    exit()
print(" ")
print(" ")
uykguhg = input("Premi invio per continuare")
print(" ")
print(" ")
db = sqlite3.connect('database.db')
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()


def welcome(name, highscore):  # Display the welcoming message
    print(
        "                    Ciao {} ! \n\n         Benvenuto nei giochi matematici \n\n                    Il tuo punteggio pi?? alto ?? : {}\n\n____________________________________________________________\n\n"
        .format(name, highscore))
    input("Premi invio per iniziare")


def main():
    print(
        "____________________________________________________________\n\n                         [Giochi Matematici]\n\n____________________________________________________________\n"
    )
    data = c.execute("SELECT * FROM data")

    # Count the number of the table's rows
    x = 0
    for i in data:
        x = x + 1

    if x == 0:  # If empty (first run)
        # Ask about the user name
        ask = True
        while ask:
            try:
                name = input("Per favore reinserisci il tuo nome : ")
                if name == "" or len(name) == 0:
                    print("Metti un nome valido !")
                else:
                    ask = False
            except valueError:
                print("Please Enter a valid value")
                askName()

        print(
            "\n___________________________________________________________\n")
        c.execute("INSERT INTO data VALUES(?,?)",
                  (name, "0"))  # Set the name in database
        db.commit()
        welcome(name, "0")
        highscore = 0

    else:  # User played before
        data = c.execute("SELECT * FROM data")
        for i in data:  # Get the name and highscore
            name = i[0]
            highscore = i[1]
        welcome(name, highscore)

    score = 0
    lose = False
    while lose != True:
        calc = random.randint(
            0, 1)  # Generate a random calculation type 0=[+] 1=[*]

        if calc == 0:  #(+)
            fnum = random.randint(2, 50)  # First number
            snum = random.randint(2, 50)  # Second number
            result = fnum + snum
            inp = "[+] {} + {} = "  # User input text

        else:  #(*)
            fnum = random.randint(1, 10)
            snum = random.randint(1, 10)
            result = fnum * snum
            inp = "[+] {} * {} ="

        def askUser():  # Ask user what is the result
            userInput = input(inp.format(fnum, snum))
            try:
                userInput = int(userInput)  # Try to make input as int
                return userInput
            except:  # If user input a text or leaft it empty
                print("Inserisci una risposta valida..")
                askUser()  # Reask again

        userInput = askUser()

        if userInput == result:  # Correct answer
            score = score + 1
            if score > highscore:  # If this score is the high score
                c.execute("UPDATE data SET highscore =  ? WHERE name = ?",
                          (score, name))  # Change highscore in database
                db.commit()
                print(
                    "Giusto ! , punteggio pi?? alto raggiunto ! il tuo punteggio : {} "
                    .format(score))  # Show message
            else:  # The score is not the highscore
                print("Giusto ! il tuo punteggio ?? di : {}".format(score))

        else:  # Wrong answer
            score = 0
            print("Oops ! Risposta Sbagliata!")
            userAgain = input("[+] Vuoi giocare di nuovo? (s,n) : ").lower()
            if userAgain == "n":
                print("alla prossima !")
                db.close()
                lose = True


main()
print(" ")
print(" ")
print(
    gino,
    " : Ti sei divertito, io si solo a guardarti.... Comunque adesso ti dovrai impegnare ancora di pi?? se vuoi sopravvivere, a te la scelta : mica sei venuto qui per giocare !1!1!"
)
print(" ")
print(" ")
hfr = input("Premi invio per continuare...")
print(" ")
print(" ")
domandaovvissima = input(
    "Computer : sei pronto per il quinto indovinello? si/si ")
print(" ")
print(" ")
print("Computer : Perfetto!!")
print(" ")
print(" ")
rh = input("Premi invio per continuare...")
print(" ")
print(" ")
print("Computer : Ecco a te il prossimo indovinello")
print(" ")
print(" ")
eh = input("Premi invio per continuare...")
print(" ")
print(" ")
print(
    "Computer : Serve solo quando si getta, cosa ??? (scrivi in minuscolo solo il nome)               "
)
terza = input("  ")
if terza == "ancora":
    print(
        "Computer : molto bene, adesso ti aspetta il sesto indovinello, che sar?? molto pi?? difficile."
    )
    print(" ")
    print(" ")
    th = input("Premi invio per continuare...")
    print(" ")
    print(" ")
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era 'ancora' ")
    print(" ")
    print(" ")
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ")
    print("Computer : Ritenta e sarai pi?? fortuato")
    print(" ")
    print(" ")
    hthhfv = input("Premi invio per finire...")
    exit()
print(" ")
print(" ")
print(gino, " : e via con il sesto, so che puoi farcela!!!")
print(" ")
print(" ")
print("Premi invio per continuare... ")
print(" ")
print(" ")
terzhh = input(
    "Computer : Una volta scoperto non esiste pi??. Cos?????? (scrivi in minuscolo e solamente il nome)   "
)
print(" ")
print(" ")
if terzhh == "segreto":
    print(
        "Computer : MOLTO BENE, adesso ti ho riservato una sorpresa."
    )
    print(" ")
    print(" ")
    th = input("Premi invio per continuare...")
    print(" ")
    print(" ")
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era segreto")
    print(" ")
    print(" ")
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ")
    print("Premi invio per uscire")
    print(" ")
    exit()

print(" ")
print(" ")

print(
    "Visto il tuo impegno costante, adesso ci sar?? un piccolo giochino come ricompensa..."
)
print(" ")
print(" ")
jhklhkjhkjh = input("Premi invio per iniziare il gioco...")
print(" ")
print(" ")
# DECLARE ALL THE CONSTANTS
BOARD_SIZE = 20
# Extra two are for the walls, playing area will have size as BOARD_SIZE
EFF_BOARD_SIZE = BOARD_SIZE + 2

PIECES = [[[1], [1], [1], [1]], [[1, 0], [1, 0], [1, 1]],
          [[0, 1], [0, 1], [1, 1]], [[0, 1], [1, 1], [1, 0]], [[1, 1], [1, 1]]]

# Constants for user input
MOVE_LEFT = 'a'
MOVE_RIGHT = 'd'
ROTATE_ANTICLOCKWISE = 'w'
ROTATE_CLOCKWISE = 's'
NO_MOVE = 'e'
QUIT_GAME = 'q'


def print_board(board, curr_piece, piece_pos, error_message=''):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Details:
    --------
    Prints out the board, piece and playing instructions to STDOUT
    If there are any error messages then prints them to STDOUT as well
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Text mode version of the TETRIS game\n\n")

    board_copy = deepcopy(board)
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board_copy[piece_pos[0] +
                       i][piece_pos[1] +
                          j] = curr_piece[i][j] | board[piece_pos[0] +
                                                        i][piece_pos[1] + j]

    # Print the board to STDOUT
    for i in range(EFF_BOARD_SIZE):
        for j in range(EFF_BOARD_SIZE):
            if board_copy[i][j] == 1:
                print("*", end='')
            else:
                print(" ", end='')
        print("")

    print("Quick play instructions:\n")
    print(" - a (return): move piece left")
    print(" - d (return): move piece right")
    print(" - w (return): rotate piece counter clockwise")
    print(" - s (return): rotate piece clockwise")

    # In case user doesn't want to alter the position of the piece
    # and he doesn't want to rotate the piece either and just wants to move
    # in the downward direction, he can choose 'f'
    print(" - e (return): just move the piece downwards as is")

    if error_message:
        print(error_message)
    print("Your move:", )


def init_board():
    """
    Parameters:
    -----------
    None
    Returns:
    --------
    board - the matrix with the walls of the gameplay
    """
    board = [[0 for x in range(EFF_BOARD_SIZE)] for y in range(EFF_BOARD_SIZE)]
    for i in range(EFF_BOARD_SIZE):
        board[i][0] = 1
    for i in range(EFF_BOARD_SIZE):
        board[EFF_BOARD_SIZE - 1][i] = 1
    for i in range(EFF_BOARD_SIZE):
        board[i][EFF_BOARD_SIZE - 1] = 1
    return board


def get_random_piece():
    """
    Parameters:
    -----------
    None
    Returns:
    --------
    piece - a random piece from the PIECES constant declared above
    """
    idx = random.randrange(len(PIECES))
    return PIECES[idx]


def get_random_position(curr_piece):
    """
    Parameters:
    -----------
    curr_piece - piece which is alive in the game at the moment
    Returns:
    --------
    piece_pos - a randomly (along x-axis) chosen position for this piece
    """
    curr_piece_size = len(curr_piece)

    # This x refers to rows, rows go along y-axis
    x = 0
    # This y refers to columns, columns go along x-axis
    y = random.randrange(1, EFF_BOARD_SIZE - curr_piece_size)
    return [x, y]


def is_game_over(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if game is over
    False - if game is live and player can still move
    """
    # If the piece cannot move down and the position is still the first row
    # of the board then the game has ended
    if not can_move_down(board, curr_piece, piece_pos) and piece_pos[0] == 0:
        return True
    return False


def get_left_move(piece_pos):
    """
    Parameters:
    -----------
    piece_pos - position of piece on the board
    Returns:
    --------
    piece_pos - new position of the piece shifted to the left
    """
    # Shift the piece left by 1 unit
    new_piece_pos = [piece_pos[0], piece_pos[1] - 1]
    return new_piece_pos


def get_right_move(piece_pos):
    """
    Parameters:
    -----------
    piece_pos - position of piece on the board
    Returns:
    --------
    piece_pos - new position of the piece shifted to the right
    """
    # Shift the piece right by 1 unit
    new_piece_pos = [piece_pos[0], piece_pos[1] + 1]
    return new_piece_pos


def get_down_move(piece_pos):
    """
    Parameters:
    -----------
    piece_pos - position of piece on the board
    Returns:
    --------
    piece_pos - new position of the piece shifted downward
    """
    # Shift the piece down by 1 unit
    new_piece_pos = [piece_pos[0] + 1, piece_pos[1]]
    return new_piece_pos


def rotate_clockwise(piece):
    """
    Paramertes:
    -----------
    piece - matrix of the piece to rotate
    Returns:
    --------
    piece - Clockwise rotated piece
    Details:
    --------
    We first reverse all the sub lists and then zip all the sublists
    This will give us a clockwise rotated matrix
    """
    piece_copy = deepcopy(piece)
    reverse_piece = piece_copy[::-1]
    return list(list(elem) for elem in zip(*reverse_piece))


def rotate_anticlockwise(piece):
    """
    Paramertes:
    -----------
    piece - matrix of the piece to rotate
    Returns:
    --------
    Anti-clockwise rotated piece
    Details:
    --------
    If we rotate any piece in clockwise direction for 3 times, we would eventually
    get the piece rotated in anti clockwise direction
    """
    piece_copy = deepcopy(piece)
    # Rotating clockwise thrice will be same as rotating anticlockwise :)
    piece_1 = rotate_clockwise(piece_copy)
    piece_2 = rotate_clockwise(piece_1)
    return rotate_clockwise(piece_2)


def merge_board_and_piece(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    None
    Details:
    --------
    Fixes the position of the passed piece at piece_pos in the board
    This means that the new piece will now come into the play
    We also remove any filled up rows from the board to continue the gameplay
    as it happends in a tetris game
    """
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            board[piece_pos[0] +
                  i][piece_pos[1] +
                     j] = curr_piece[i][j] | board[piece_pos[0] +
                                                   i][piece_pos[1] + j]

    # After merging the board and piece
    # If there are rows which are completely filled then remove those rows

    # Declare empty row to add later
    empty_row = [0] * EFF_BOARD_SIZE
    empty_row[0] = 1
    empty_row[EFF_BOARD_SIZE - 1] = 1

    # Declare a constant row that is completely filled
    filled_row = [1] * EFF_BOARD_SIZE

    # Count the total filled rows in the board
    filled_rows = 0
    for row in board:
        if row == filled_row:
            filled_rows += 1

    # The last row is always a filled row because it is the boundary
    # So decrease the count for that one
    filled_rows -= 1

    for i in range(filled_rows):
        board.remove(filled_row)

    # Add extra empty rows on the top of the board to compensate for deleted rows
    for i in range(filled_rows):
        board.insert(0, empty_row)


def overlap_check(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if piece do not overlap with any other piece or walls
    False - if piece overlaps with any other piece or board walls
    """
    curr_piece_size_x = len(curr_piece)
    curr_piece_size_y = len(curr_piece[0])
    for i in range(curr_piece_size_x):
        for j in range(curr_piece_size_y):
            if board[piece_pos[0] + i][piece_pos[1] +
                                       j] == 1 and curr_piece[i][j] == 1:
                return False
    return True


def can_move_left(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if we can move the piece left
    False - if we cannot move the piece to the left,
            means it will overlap if we move it to the left
    """
    piece_pos = get_left_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_move_right(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if we can move the piece left
    False - if we cannot move the piece to the right,
            means it will overlap if we move it to the right
    """
    piece_pos = get_right_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_move_down(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if we can move the piece downwards
    False - if we cannot move the piece to the downward direction
    """
    piece_pos = get_down_move(piece_pos)
    return overlap_check(board, curr_piece, piece_pos)


def can_rotate_anticlockwise(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if we can move the piece anti-clockwise
    False - if we cannot move the piece to anti-clockwise
            might happen in case rotating would overlap with any existing piece
    """
    curr_piece = rotate_anticlockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)


def can_rotate_clockwise(board, curr_piece, piece_pos):
    """
    Parameters:
    -----------
    board - matrix of the size of the board
    curr_piece - matrix for the piece active in the game
    piece_pos - [x,y] co-ordinates of the top-left cell in the piece matrix
                w.r.t. the board
    Returns:
    --------
    True - if we can move the piece clockwise
    False - if we cannot move the piece to clockwise
            might happen in case rotating would overlap with any existing piece
    """
    curr_piece = rotate_clockwise(curr_piece)
    return overlap_check(board, curr_piece, piece_pos)


def play_game():
    """
    Parameters:
    -----------
    None
    Returns:
    --------
    None
    Details:
    --------
    - Initializes the game
    - Reads player move from the STDIN
    - Checks for the move validity
    - Continues the gameplay if valid move, else prints out error msg
      without changing the board
    - Fixes the piece position on board if it cannot be moved
    - Pops in new piece on top of the board
    - Quits if no valid moves and possible for a new piece
    - Quits in case user wants to quit
    """

    # Initialize the game board, piece and piece position
    board = init_board()
    curr_piece = get_random_piece()
    piece_pos = get_random_position(curr_piece)
    print_board(board, curr_piece, piece_pos)

    # Get player move from STDIN
    player_move = input()
    while (not is_game_over(board, curr_piece, piece_pos)):
        ERR_MSG = ""
        do_move_down = False
        if player_move == MOVE_LEFT:
            if can_move_left(board, curr_piece, piece_pos):
                piece_pos = get_left_move(piece_pos)
                do_move_down = True
            else:
                ERR_MSG = "Cannot move left!"
        elif player_move == MOVE_RIGHT:
            if can_move_right(board, curr_piece, piece_pos):
                piece_pos = get_right_move(piece_pos)
                do_move_down = True
            else:
                ERR_MSG = "Cannot move right!"
        elif player_move == ROTATE_ANTICLOCKWISE:
            if can_rotate_anticlockwise(board, curr_piece, piece_pos):
                curr_piece = rotate_anticlockwise(curr_piece)
                do_move_down = True
            else:
                ERR_MSG = "Cannot rotate anti-clockwise !"
        elif player_move == ROTATE_CLOCKWISE:
            if can_rotate_clockwise(board, curr_piece, piece_pos):
                curr_piece = rotate_clockwise(curr_piece)
                do_move_down = True
            else:
                ERR_MSG = "Cannot rotate clockwise!"
        elif player_move == NO_MOVE:
            do_move_down = True

        else:
            ERR_MSG = "That is not a valid move!"

        if do_move_down and can_move_down(board, curr_piece, piece_pos):
            piece_pos = get_down_move(piece_pos)

        # This means the current piece in the game cannot be moved
        # We have to fix this piece in the board and generate a new piece
        if not can_move_down(board, curr_piece, piece_pos):
            merge_board_and_piece(board, curr_piece, piece_pos)
            curr_piece = get_random_piece()
            piece_pos = get_random_position(curr_piece)

        # Redraw board
        print_board(board, curr_piece, piece_pos, error_message=ERR_MSG)

        # Get player move from STDIN
        player_move = input()

    print("GAME OVER!")


if __name__ == "__main__":
    play_game()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
tgtgt = input("Premi invio per continuare...")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(gino,
      " : Sappi che d'ora in poi gli indovinelli saranno molto difficili, vai e vinci!!!")
print(" ")
print(" ")
print("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    "Computer : Sa tante cose ma non sa parlare, ha tante ali ma non pu?? volare. Cos??????  (scrivi in minuscolo e solamente il nome)  "
)
print(" ")
terzdhdh = input("  ")
print(" ")
print(" ")
if terzdhdh == "libro":
    print(
        "Computer : WOW, sei davvero molto bravo! Sei sicuro che questa non ?? la prima volta che ci provi? Comunque COMPLIMENTI."
    )
    print(" ")
    print(" ")
    th = input("Premi invio per continuare...")
    print(" ")
    print(" ")
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era 'libro' ")
    print(" ")
    print(" ")
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ")
    print("Premi invio per uscire")
    print(" ")
    exit()

print(gino,
      " : Sappi che d'ora in poi saranno molto difficili, vai e vinci!!!")
print(" ")
print(" ")
print("Premi invio per continuare... ")
print(" ")
print(" ")
print(
    "Computer : La mia vita pu?? durare qualche ora, quello che produco mi divora. Sottile sono veloce, grossa sono lenta e il vento molto mi spaventa. Chi sono? (scrivi in minuscolo e solamente il nome e al singolare)   "
)
print(" ")
tergzhdh = input("  ")
print(" ")
print(" ")
if tergzhdh == "candela":
    print(
        "Computer : MOLTO BENE, adesso ti aspetta il nono indovinello, che sar?? molto pi?? difficile."
    )
    print(" ")
    print(" ")
    th = input("Premi invio per continuare...")
    print(" ")
    print(" ")
else:
    print("Computer : RISPOSTA SBAGLIATA, quella corretta era candela")
    print(" ")
    print(" ")
    print("            GAME OVER!!!!!!!")
    print(" ")
    print(" ")
    print("Premi invio per uscire")
    print(" ")
    exit()
print(" ")
print(" ")
print(
    gino,
    "Ben fatto uomo ?? cos?? che ti voglio, sinceramente nessuno credeva in te")
print(" ")
print(" ")
hfgghfhgfghfghhhhhhhgff = input("Premi invio per continuare")
print(" ")
print(" ")
print(
    "Computer : non lasciarti ingannare da qualche insuccesso, ?? molto facile smarrire la retta via e spesso non ce ne accorgiamo nemmeno quando succede, un tempo successe anche a me..."
)
print(" ")
print(" ")
storia = input(
    "Se vuoi sentire la storia di Computer digita : 'si' altrimenti scrivi 'no'...         "
)
print(" ")
print(" ")
if storia == "no":
    print(
        "Cosa hai detto, ma hai per caso rifiutato la mia offerta di raccontarti la storia... lo ritengo inaccettabile, adesso vado a uccidere subito ely e tu non potrai fare pi?? niente per evitarlo"
    )
    print(" ")
    print(" ")
    print(" ")
    print(
        "Ely : ma perche gli hai detto di no, adesso mi uccider??, sei proprio uno stupido!!!"
    )
    print(" ")
    print(" ")
    print(" ")
    print("GAME OVER!!!!!")
    exit()
score = 0
if storia == "si":
    print(
        "Computer : Bhe, mi fa piacere raccontare di com'ero un tempo sai, ti assomigliavo quasi, per?? avevo molti amici che nel tempo iniziarono a separarsi..."
    )
    print(" ")
    print(" ")
    hffhdffffsfsggggf = input("Premi invio per continuare la storia...")
    print(" ")
    print(" ")
    print(
        "Computer : Dovevo decidere con chi stare e scelsi il gruppo peggiore, quello degli atleti, loro bullizzavano tutta la scuola e poi diventai proprio come loro..."
    )
    print(" ")
    print(" ")
    hffgghdffffsfsf = input("Premi invio per continuare la storia...")
    print(" ")
    print(" ")
    print(
        "Computer : Dopo molto tempo capii che ormai ero cambiato e tornare indietro pi?? non potevo, decisi di cambiare nome e di mascherarmi... "
    )
    print(" ")
    print(" ")
    hffhdffffsfgsf = input("Premi invio per continuare la storia...")
    print(" ")
    print(" ")
    print(
        "Computer : Nonostante ci?? sono rimasto com'ero e non so se riuscir?? mai a tornare quello di una volta..."
    )
    print(" ")
    print(" ")
    hffhghdffgffsfsf = input("Premi invio per continuare la storia...")
    print(" ")
    print(" ")
    print(
        "Computer : GRAZIE, mi ha fatto bene parlarne, mi sento libero, perci?? ti far?? due doni..."
    )
    print(" ")
    print(" ")
    hffhhdgffsfsf = input("Premi invio per continuare la storia...")
    print(" ")
    print(" ")
    print(
        "Computer : Per prima cosa ti dir?? il mio nome : Marc, e si sono il fratello di ELy..."
    )
    print(" ")
    print(" ")
    hffghghdffsfsf = input("Premi invio per continuare la storia...")
    print(" ")
    print(" ")
    print(
        "Marc : Come ultimo dono ti far?? saltare un indovinello, ma il resto dovrai finirlo da solo"
    )
    print(" ")
    print(" ")
    prikhhkk = input("Premi invio per continuare...")
    print(" ")
    print(" ")
    print(
        "Marc : visto che hai appena saltato il nono indovinello, ecco a te un giochino"
    )
    print(" ")
    print(" ")
    hjcjdjjddjj = input("Premi invio per iniziare a giocare...")
    print(" ")
    print(" ")


def line_shift(line):
    global score
    new_row = []
    for num_line in line:
        if num_line != 0:
            if len(new_row) > 0:
                if new_row[-1][1] == 0:
                    if new_row[-1][0] == num_line:
                        new_row[-1] = [num_line * 2, 1]
                        score += num_line * 2
                    else:
                        new_row.append([num_line, 0])
                else:
                    new_row.append([num_line, 0])

            else:
                new_row.append([num_line, 0])

    # convert in stack
    stack_row = []
    for nun in new_row:
        if nun[0] != 0:
            stack_row.append(nun[0])
    size = 4 - len(stack_row)
    for num_line in range(size):
        stack_row.append(0)
    return stack_row


def gen_num():
    num = (random.choices([4, 2], weights=[10, 90]))[0]
    return num


def place_num_on_the_board():
    place_list = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                place_list.append((i, j))
    if len(place_list) == 0:
        print('GAME OVER!!!')
        exit(0)
    place = random.choice(place_list)
    board[place[0]][place[1]] = gen_num()


def gen_start_board(size_row=4, size_col=4):
    board2048 = [[i * 0] * size_row for i in range(size_col)]
    while True:
        gen_coordinate_num1 = [random.randint(0, 3), random.randint(0, 3)]
        gen_coordinate_num2 = [random.randint(0, 3), random.randint(0, 3)]
        if gen_coordinate_num1 != gen_coordinate_num2:
            break
    board2048[gen_coordinate_num1[0]][gen_coordinate_num1[1]] = gen_num()
    board2048[gen_coordinate_num2[0]][gen_coordinate_num2[1]] = gen_num()
    return board2048


def x_move(move_side):
    for index, row in enumerate(board):
        if move_side == 'left':
            board[index] = line_shift(row)
        if move_side == 'right':
            board[index] = line_shift(row[::-1])[::-1]


def y_move(move_side):
    for col_board in range(4):
        line = []
        for row_board in range(4):
            line.append(board[row_board][col_board])
        if move_side == 'down':
            line = line_shift(line[::-1])[::-1]
        if move_side == 'up':
            line = line_shift(line)
        for row_board in range(4):
            board[row_board][col_board] = line[row_board]


def print_game_screen():
    # clear console
    if platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

    print(f'{"*" * 5} x - exit, r - restart {"*" * 5}')
    print('move: left, right, up, down')
    print(f'Score: {score}')
    for i in board:
        print(i)


board = gen_start_board()
while True:
    print_game_screen()
    step = input('Enter move: ').lower()
    tmp_board = [row[:] for row in board]
    if step in ('right', 'left'):
        x_move(step)
    elif step in ('down', 'up'):
        y_move(step)
    elif step == 'r':  # restart
        board = gen_start_board()
        score = 0
        continue
    elif step == 'x':
        print('You pressed x - exit the game')
        exit(0)
    else:
        continue
    if tmp_board == board:  # The move did not change the board
        continue
    place_num_on_the_board()
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
pjjjkkkkkk = input("Premi invio per continuare...")
print(" ")
print(" ")
print(
    gino,
    " : SAI, NON MI SEI MAI PIACIUTO QUEL DI MARC NON E' RIUSCITO NEMMENO A fARTI UN PAIO DI INDOVINELLI, QUANDO ERA CON NOI, TI AVREBBE UCCISO A VISTA"
)
print(" ")
print(" ")
ujhkhljhkjh = input("Premi invio per continuare...")
print(" ")
print(" ")
print(
    gino,
    "SONO STATO IO A TRASFORMARLO E ADESSO FINIRO' DA SOLO CIO' CHE HO INIZIATO "
)
print(" ")
print(" ")
yuueuuuuuuuuu = input("Premi invio per passare all'ultimo indovinello...")
print(" ")
print(" ")
print(
    gino,
    "?? l???unica via dove ancora nessuno ci ha mai passeggiato. Qual ??? (scrivi solo le due parole senza articolo in minuscolo  "
)
if yuueuuuuuuuuu == "via lattea":
    print(" ")
    print(" ")
    print(" TATARATATATARATA")
    print(" ")
    print(" TATARATATATARATA")
    print(" ")
    print(
        "COMPLIMENTIIIII, HAI VINTO E PERCIO' HAI SALVATO ELY, ADESSO PER PREMIO TI FARO' GIOCARE CON LA TUA AMICA ELY PER QUANTO VORRAI"
    )
    print(" ")
    print(" ")
    ufufufufufufufufuf = input(
        "Premi inio per salvare ELY e giocare con lei...")

else:
    print(": RISPOSTA SBAGLIATA, quella corretta era 'via lattea' ")
    print(" ")
    print("            GAME OVER!!!!!!!       TI MANCAVA POCO!!!!!!!!!")
    print(" ")
    print(" ")
    print("Premi invio per uscire")
    print(" ")
    exit()
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")

print(" zzzz  ")
print("   ")
print("   ")
print("  zzz ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("  zzzzzzz ")
print("   ")
print("   ")
print("z   ")
print("z   ")
print("Finalmente ho ripreso il controllo del gioco, ho rischiato molto ma finalmente ho ucciso il buon computer, e io, ilvirus, ha preso il controllo... ")
print("   ")
print("  ")
print("   ")
inputprint=input("Premi invio per continuare...")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("Adesso le sfide saranno molto pi?? difficili... BUONA FORTUNA muahhhahaha...")
print("   ")
print("   ")
print("   ")
print("   ")
inputfprint=input("Premi invio per continuare...")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
print("Gioco in BETA")







class Field:
    def __init__(self, size):
        self.size = size
        self.icons = {
            0: ' . ',
            1: ' * ',
            2: ' # ',
            3: ' & ',
        }
        self.snake_coords = []
        self._generate_field()
        self.add_entity()

    def add_entity(self):

        while (True):
            i = randint(0, self.size - 1)
            j = randint(0, self.size - 1)
            entity = [i, j]

            if entity not in self.snake_coords:
                self.field[i][j] = 3
                break

    def _generate_field(self):
        self.field = [[0 for j in range(self.size)] for i in range(self.size)]

    def _clear_field(self):
        self.field = [[j if j != 1 and j != 2 else 0 for j in i]
                      for i in self.field]

    def render(self, screen):
        size = self.size
        self._clear_field()

        # Render snake on the field
        for i, j in self.snake_coords:
            self.field[i][j] = 1

        # Mark head
        head = self.snake_coords[-1]
        self.field[head[0]][head[1]] = 2

        for i in range(size):
            row = ''
            for j in range(size):
                row += self.icons[self.field[i][j]]

            screen.addstr(i, 0, row)

    def get_entity_pos(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 3:
                    return [i, j]

        return [-1, -1]

    def is_snake_eat_entity(self):
        entity = self.get_entity_pos()
        head = self.snake_coords[-1]
        return entity == head


class Snake:
    def __init__(self, name):
        self.name = name
        self.direction = curses.KEY_RIGHT

        # Init basic coords
        self.coords = [[0, 0], [0, 1], [0, 2], [0, 3]]

    def set_direction(self, ch):

        # Check if wrong direction
        if ch == curses.KEY_LEFT and self.direction == curses.KEY_RIGHT:
            return
        if ch == curses.KEY_RIGHT and self.direction == curses.KEY_LEFT:
            return
        if ch == curses.KEY_UP and self.direction == curses.KEY_DOWN:
            return
        if ch == curses.KEY_DOWN and self.direction == curses.KEY_UP:
            return

        self.direction = ch

    def level_up(self):
        # get last point direction
        a = self.coords[0]
        b = self.coords[1]

        tail = a[:]

        if a[0] < b[0]:
            tail[0] -= 1
        elif a[1] < b[1]:
            tail[1] -= 1
        elif a[0] > b[0]:
            tail[0] += 1
        elif a[1] > b[1]:
            tail[1] += 1

        tail = self._check_limit(tail)
        self.coords.insert(0, tail)

    def is_alive(self):
        head = self.coords[-1]
        snake_body = self.coords[:-1]
        return head not in snake_body

    def _check_limit(self, point):
        # Check field limit
        if point[0] > self.field.size - 1:
            point[0] = 0
        elif point[0] < 0:
            point[0] = self.field.size - 1
        elif point[1] < 0:
            point[1] = self.field.size - 1
        elif point[1] > self.field.size - 1:
            point[1] = 0

        return point

    def move(self):
        # Determine head coords
        head = self.coords[-1][:]

        # Calc new head coords
        if self.direction == curses.KEY_UP:
            head[0] -= 1
        elif self.direction == curses.KEY_DOWN:
            head[0] += 1
        elif self.direction == curses.KEY_RIGHT:
            head[1] += 1
        elif self.direction == curses.KEY_LEFT:
            head[1] -= 1

        # Check field limit
        head = self._check_limit(head)

        del (self.coords[0])
        self.coords.append(head)
        self.field.snake_coords = self.coords

        if not self.is_alive():
            sys.exit()

        # check if snake eat an entity
        if self.field.is_snake_eat_entity():
            curses.beep()
            self.level_up()
            self.field.add_entity()

    def set_field(self, field):
        self.field = field


def main(screen):
    # Configure screen
    screen.timeout(0)

    # Init snake & field
    field = Field(10)
    snake = Snake("Joe")
    snake.set_field(field)

    while (True):
        # Get last pressed key
        ch = screen.getch()
        if ch != -1:
            # If some arrows did pressed - change direction
            snake.set_direction(ch)

        # Move snake
        snake.move()

        # Render field
        field.render(screen)
        screen.refresh()

        time.sleep(.4)


if __name__ == '__main__':
    curses.wrapper(main)













































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































