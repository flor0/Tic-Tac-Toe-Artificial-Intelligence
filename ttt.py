import numpy as np
import sys, random
import pygame
from anytree import Node, RenderTree
sys.setrecursionlimit(255168)
node = Node("origin")
nodes = [node]

spielbrett = [[0,0,0],[0,0,0],[0,0,0]]

rekt = [
    [pygame.Rect(0,0, 500/3, 500/3), pygame.Rect(500/3,0, 500/3,500/3), pygame.Rect(2*500/3,0, 500,500/3)],
    [pygame.Rect(0,500/3, 500/3,500/3), pygame.Rect(500/3,500/3, 500/3,500/3), pygame.Rect(2*500/3,500/3, 500/3,500/3)],
    [pygame.Rect(0,2*500/3, 500/3,500/3), pygame.Rect(500/3,2*500/3, 500/3,500/3), pygame.Rect(2*500/3,2*500/3, 500/3,500/3)]
]

done = False
einheitsmatrix = [[1,0,0],[0,1,0],[0,0,1]]
einheitsmatrix_transp = [[0,0,1],[0,1,0],[1,0,0]]


def checktictactoe(spielbrett1, player):
    spielbrett_temp = spielbrett1.copy()
    spielbrett1_transp = np.matrix.transpose(np.asarray(spielbrett_temp))
    for reihe in range(len(spielbrett_temp)):
        if np.dot(spielbrett_temp[reihe], np.ones((3, 1))) == player * 3 or np.dot(spielbrett1_transp[reihe], np.ones((3, 1))) == player * 3:
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


'''
def minimax(spielbrett1, player, depth=0):
    spielbr = spielbrett1
    spielbr_weiter = spielbr.copy()
    zug_reihe = []
    zug_stelle = []
    possibilities = []
    possibilities_values = []
    possibilities_bretter = []

    for reihe in range(len(spielbr)):
        for spalte in range(len(spielbr[reihe])):
            if spielbr[reihe][spalte] == 0:
                spielbr_weiter[reihe][spalte] = player
                if checktictactoe(spielbr_weiter.copy(), -1):
                    nodee = Node(str(spielbr_weiter))
                    nodee.parent = nodes[len(nodes) - 1]
                    nodes.append(nodee)
                    print("test1 "+str(depth))
                    return [10, spielbr_weiter, reihe, spalte]
                if checktictactoe(spielbr_weiter.copy(), 1):
                    nodee = Node(str(spielbr_weiter))
                    nodee.parent = nodes[len(nodes) - 1]
                    nodes.append(nodee)
                    print("test2 "+str(depth))
                    return [-1, spielbr_weiter, reihe, spalte]
                if checkvollesbrett(spielbr_weiter):
                    nodee = Node(str(spielbr_weiter))
                    nodee.parent = nodes[len(nodes) - 1]
                    nodes.append(nodee)
                    print("test3 "+str(depth))
                    return [0, spielbr_weiter, reihe, spalte]
                temp = minimax(spielbr_weiter.copy(), -player, depth+1)
                possibilities.append(temp)
                possibilities_values.append(temp[0])
                possibilities_bretter.append(temp[1])
                zug_reihe.append(reihe)
                zug_stelle.append(spalte)
                print("test4 "+str(depth))


    print("test5 "+str(depth))
    max_value = max(possibilities_values)
    sum_values = sum(possibilities_values)
    max_brett = possibilities_bretter[possibilities_values.index(max_value)]
    max_reihe = zug_reihe[possibilities_values.index(max_value)]
    max_stelle = zug_stelle[possibilities_values.index(max_value)]
    nodee = Node(str(max_brett))
    nodee.parent = nodes[len(nodes)-1]
    nodes.append(nodee)
    return [sum_values, max_brett, max_reihe, max_stelle]
'''

def minimax(brett, player):
    # Check if you can even keep playing
    if checkvollesbrett(brett.copy()):
        return -1, None, None  # MIN
    if checktictactoe(brett.copy(), player):
        return 1, None, None  # MAX
    if checktictactoe(brett.copy(), -player):
        return -1, None, None  # MIN

    # If you can make a move, try all of them!
    minimaxreturnvalues = []
    zuge = []
    for zeile in range(len(brett)):
        for spalte in range(len(brett[zeile])):
            if brett[zeile][spalte] == 0:
                brett_weiter = brett.copy()
                brett_weiter[zeile][spalte] = player
                minimaxreturnvalues.append(minimax(brett_weiter.copy(), -player))
                zuge.append((zeile, spalte))
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

def drawboard():

    pygame.draw.line(screen, (0,0,0), (500/3, 20), (500/3, (500-20)))
    pygame.draw.line(screen, (0,0,0), (2*(500/3), 20), (2*500/3, 500-20))
    pygame.draw.line(screen, (0,0,0), (20, 500/3), (500-20, 500/3))
    pygame.draw.line(screen, (0,0,0), (20, 2*500/3), (500-20, 2*500/3))


def drawstatus(board):
    for reihe in range(len(spielbrett)):
        for spalte in range(len(spielbrett[reihe])):
            if spielbrett[reihe][spalte] == 1:
                drawcircle((reihe, spalte))
            elif spielbrett[reihe][spalte] == -1:
                drawcross((reihe, spalte))


def drawcross(pos):
    dx = 250//3
    center = (dx+pos[1]*500//3, dx+pos[0]*500//3)
    pygame.draw.line(screen, (10,100,200), (center[0]-40, center[1]-40), (center[0]+40, center[1]+40), 10)
    pygame.draw.line(screen, (10,100,200), (center[0]+40, center[1]-40), (center[0]-40, center[1]+40), 10)


def drawcircle(pos):
    dx = 250 // 3
    center = (dx + pos[1] * 500 // 3, dx + pos[0] * 500 // 3)
    pygame.draw.circle(screen,(190,10,10),center, 50)
    pygame.draw.circle(screen, (225,225,225), center, 45)


def getclickindex(clickpos):
    for i in range(len(rekt)):
        for j in range(len(rekt[i])):
            if rekt[i][j].collidepoint(clickpos[0], clickpos[1]):
                return i, j
    return False


pygame.init()
screen = pygame.display.set_mode((500, 500))

screen.fill((225,225,225))
drawboard()

pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            index = getclickindex(pos)
            if not index:
                break
            print(index)
            # Spieler zug
            print(spielbrett)
            # index1 = int(input("reihe: "))
            # index2 = int(input("spalte: "))
            index1 = index[0]
            index2 = index[1]
            spielbrett[index1][index2] = 1
            drawboard()
            drawstatus(spielbrett)
            pygame.display.flip()
            print("Spieler 3: {}".format(checktictactoe(spielbrett.copy(), 1)))
            spielbrett_save1 = spielbrett.copy()

            if checkvollesbrett(spielbrett_save1):
                print("DRAW!")
                print(spielbrett_save1)
                done = True
            elif checktictactoe(spielbrett_save1, 1):
                print("Spieler Gewinnt!")
                print(spielbrett_save1)
                done = True

            # KI
            ai_value, ai_reihe, ai_stelle = minimax(spielbrett_save1.copy(), -1)

            print("AI moves to: {}/{}".format(ai_reihe, ai_stelle))
            spielbrett[ai_reihe][ai_stelle] = -1
            print("AI done")
            print("AI 3: {}".format(checktictactoe(spielbrett.copy(), -1)))

            if checkvollesbrett(spielbrett.copy()):
                print("DRAW!")
                print(spielbrett)
                drawboard()
                drawstatus(spielbrett)
                done = True
            if checktictactoe(spielbrett.copy(), 1):
                print("Spieler gewinnt!")
                print(spielbrett)
                drawboard()
                drawstatus(spielbrett)
                done = True
            elif checktictactoe(spielbrett.copy(), -1):
                print("KI gewinnt!")
                print(spielbrett)
                drawboard()
                drawstatus(spielbrett)
                done = True
            drawboard()
            drawstatus(spielbrett)
            pygame.display.flip()
            print(spielbrett)
            print(RenderTree(nodes[0]))
