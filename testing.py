import numpy as np
import random, time, sys

def checktictactoe(spielbrett1, player):
    spielbrett_temp = spielbrett1.copy()
    spielbrett1_transp = np.matrix.transpose(np.asarray(spielbrett_temp))
    for reihe in range(len(spielbrett_temp)):
        if np.dot(spielbrett_temp[reihe], np.ones((3, 1))) == player * 3 or np.dot(spielbrett1_transp[reihe], np.ones(
                (3, 1))) == player * 3:
            return True
    if spielbrett_temp[0][0] == player and spielbrett_temp[1][1] == player and spielbrett_temp[2][2] == player:
        return True
    if spielbrett_temp[0][2] == player and spielbrett_temp[1][1] == player and spielbrett_temp[2][0] == player:
        return True
    return False

def checkvollesbrett(brett):
    for i in range(len(brett)):
        for j in range(len(brett[i])):
            if brett[i][j] == 0:
                return False
    return True

# ----------------------------------------------------------------------------------------------------------------------

debug = []

def minimax(brett, player):
    # Check if you can even keep playing
    if checkvollesbrett(brett.copy()):
        print("Brett voll")
        return -1, None, None  # MIN
    if checktictactoe(brett.copy(), player):
        print("WINNER")
        return 1, None, None  # MAX
    if checktictactoe(brett.copy(), -player):
        print("LOSER")
        return -1, None, None  # MIN

    # If you can make a move, try all of them!
    minimaxreturnvalues = []
    zuge = []
    print("CANMOVE")
    for zeile in range(len(brett)):
        for spalte in range(len(brett[zeile])):
            if brett[zeile][spalte] == 0:
                brett_weiter = brett.copy()
                brett_weiter[zeile][spalte] = player
                minimaxreturnvalues.append(minimax(brett_weiter.copy(), -player))
                zuge.append((zeile, spalte))
    print(len(minimaxreturnvalues))
    print("Minimaxes done")
    meinwert = sum([i[0] for i in minimaxreturnvalues])
    max_wert = max([i[0] for i in minimaxreturnvalues])
    meine_zeile = None
    meine_spalte = None
    for i in range(len(minimaxreturnvalues)):
        if minimaxreturnvalues[i][0] == max_wert:
            meine_zeile = zuge[i][0]
            meine_spalte = zuge[i][1]
            break
        else:
            meine_zeile = 69
            meine_spalte = 69

    return meinwert, meine_zeile, meine_spalte

class minimaxer:
    def __init__(self, spielfeld2, spieler2):
        self.spielfeld = spielfeld2
        self.spieler = spieler2
        self.wert, self.zeile, self.spalte = minimax(self.spielfeld, self.spieler)

    def minimax(self, brett, player):
        # Check if you can even keep playing
        if checkvollesbrett(brett.copy()):
            print("Brett voll")
            return -1, None, None  # MIN
        if checktictactoe(brett.copy(), player):
            print("WINNER")
            return 1, None, None  # MAX
        if checktictactoe(brett.copy(), -player):
            print("LOSER")
            return -1, None, None  # MIN

        # If you can make a move, try all of them!
        minimaxreturnvalues = []
        zuge = []
        print("CANMOVE")
        for zeile in range(len(brett)):
            for spalte in range(len(brett[zeile])):
                if brett[zeile][spalte] == 0:
                    brett_weiter = brett.copy()
                    brett_weiter[zeile][spalte] = player
                    minimaxreturnvalues.append(minimax(brett_weiter.copy(), -player))
                    zuge.append((zeile, spalte))
        print(len(minimaxreturnvalues))
        print("Minimaxes done")
        meinwert = sum([i[0] for i in minimaxreturnvalues])
        max_wert = max([i[0] for i in minimaxreturnvalues])
        meine_zeile = None
        meine_spalte = None
        for i in range(len(minimaxreturnvalues)):
            if minimaxreturnvalues[i][0] == max_wert:
                meine_zeile = zuge[i][0]
                meine_spalte = zuge[i][1]
                break
            else:
                meine_zeile = 69
                meine_spalte = 69

        return meinwert, meine_zeile, meine_spalte

    def checktictactoe(self, spielbrett1, player):
        spielbrett_temp = spielbrett1.copy()
        spielbrett1_transp = np.matrix.transpose(np.asarray(spielbrett_temp))
        for reihe in range(len(spielbrett_temp)):
            if np.dot(spielbrett_temp[reihe], np.ones((3, 1))) == player * 3 or np.dot(spielbrett1_transp[reihe],
                                                                                       np.ones(
                                                                                               (3, 1))) == player * 3:
                return True
        if spielbrett_temp[0][0] == player and spielbrett_temp[1][1] == player and spielbrett_temp[2][2] == player:
            return True
        if spielbrett_temp[0][2] == player and spielbrett_temp[1][1] == player and spielbrett_temp[2][0] == player:
            return True
        return False

    def checkvollesbrett(self, brett):
        for i in range(len(brett)):
            for j in range(len(brett[i])):
                if brett[i][j] == 0:
                    return False
        return True




spielbrett = [[0, -1, 0],
              [0, 1, -1],
              [1, -1, 1]]

# Oben links, oben rechts   W
# Oben links, unten links   L

# Oben rechts, oben links   W
# Oben rechts, unten links  L

# Unten links, oben links   L
# Unten links, oben rechts  L


#print(minimax(spielbrett.copy(), -1))

aaa = minimaxer(spielbrett, -1)
print("class")
print(aaa.wert, aaa.zeile, aaa.spalte)
print("/class")

spielbrett = [[0, -1, -1],
              [0, 1, 1],
              [1, -1, 1]]

#print(minimax(spielbrett.copy(), -1))

aaa = minimaxer(spielbrett, -1)
print("class")
print(aaa.wert, aaa.zeile, aaa.spalte)
print("/class")

spielbrett = [[0, 1, -1],
              [0, -1, 1],
              [1, -1, -1]]
#print(minimax(spielbrett.copy(), -1))

aaa = minimaxer(spielbrett, -1)
print("class")
print(aaa.wert, aaa.zeile, aaa.spalte)
print("/class")