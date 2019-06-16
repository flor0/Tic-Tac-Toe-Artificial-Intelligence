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
        self.opponent = 1 if self.spieler == 2 else 2
        self.nr_lose = 0
        self.nr_win = 0
        self.nr_draw = 0
        self.wert, self.zeile, self.spalte = self.minimax(self.spielfeld, self.spieler, 0)

    def minimax(self, brett, player, recursion):
        # Check if you can even keep playing
        if self.checktictactoe(brett.copy(), -1):
            print("WINNER {}".format(recursion))
            self.nr_win += 1
            return 5, None, None  # MAX
        if self.checktictactoe(brett.copy(), 1):
            print("LOSER {}".format(recursion))
            self.nr_lose += 1
            return -5, None, None  # MIN
        if self.checkvollesbrett(brett.copy()):
            print("DRAW {}".format(recursion))
            self.nr_draw += 1
            return 1, None, None  # MIN


        # If you can make a move, try all of them!
        minimaxreturnvalues = []
        zuge = []
        n = 0
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
        meinwert = sum([i[0] for i in minimaxreturnvalues])
        max_wert = max([i[0] for i in minimaxreturnvalues])
        meine_zeile = None
        meine_spalte = None
        for i in range(len(minimaxreturnvalues)):
            if minimaxreturnvalues[i][0] == max_wert:
                meine_zeile = zuge[i][0]
                meine_spalte = zuge[i][1]
                break


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

    def checkzweier(self, brett, spieler):
        for i in range(3):
            if (brett[i][1] == brett[i][0] or brett[i][1] == brett[i][2]) and brett[i][1] == spieler:
                return True
        for i in range(3):
            if (brett[0][i] == brett[1][i] or brett[2][i] == brett[1][i]) and brett[1][i] == spieler:
                return True
        if brett[1][1] == spieler and (brett[1][1] == brett[0][0] or brett[1][1] == brett[2][2]):
            return True
        if brett[1][1] == spieler and (brett[1][1] == brett[0][2] or brett[1][1] == brett[2][0]):
            return True
        return False
