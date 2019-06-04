import numpy as np
import copy

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
# TODO: BROKEN!
def checkvollesbrett(brett):
    for i in range(3):
        for j in range(3):
            if brett[i][j] == 0:
                return False
    return True



class minimaxer:
    def __init__(self, spielfeld2, spieler2):
        self.spielfeld = spielfeld2
        self.spieler = spieler2
        self.wert, self.zeile, self.spalte = self.minimax(self.spielfeld, self.spieler, 0)

    def minimax(self, brett, player, recursion):
        # Check if you can even keep playing
        if checktictactoe(brett.copy(), -1):
            print("WINNER {}".format(recursion))
            return 1, None, None  # MAX
        if checktictactoe(brett.copy(), 1):
            print("LOSER {}".format(recursion))
            return -1, None, None  # MIN
        if checkvollesbrett(brett.copy()):
            print("DRAW {}".format(recursion))
            return 0, None, None  # MIN

        # If you can make a move, try all of them!
        minimaxreturnvalues = []
        zuge = []
        n = 0
        print("ACTUALLY MOVED PAST THE INITIAL STAGE, DOES MINIMAX!")
        for zeile in range(len(brett)):
            for spalte in range(len(brett[zeile])):
                if brett[zeile][spalte] == 0:
                    brett_weiter = copy.deepcopy(brett)
                    brett_weiter[zeile][spalte] = player
                    minimaxreturnvalues.append(self.minimax(brett_weiter, -player, recursion+1))
                    print(brett_weiter)
                    n += 1
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
        spielbrett1 = spielbrett1.copy()
        spielbrett1_transp = np.matrix.transpose(np.asarray(spielbrett1))
        for reihe in range(len(spielbrett1)):
            if np.dot(spielbrett1[reihe], np.ones((3, 1))) == player * 3 or np.dot(spielbrett1_transp[reihe],
                                                                                   np.ones((3, 1))) == player * 3:
                return True
        if spielbrett1[0][0] == player and spielbrett1[1][1] == player and spielbrett1[2][2] == player:
            return True
        if spielbrett1[0][2] == player and spielbrett1[1][1] == player and spielbrett1[2][0] == player:
            return True
        return False

    def checkvollesbrett(self, brett):
        for i in range(len(brett)):
            for j in range(len(brett[i])):
                if brett[i][j] == 0:
                    return False
        return True

