import numpy as np
import sys, random
import pygame
from anytree import Node, RenderTree
from minmax import *
import minmax_alpha_beta
import copy
import time

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


def drawboard():

    pygame.draw.line(screen, (0,0,0), (500/3, 20), (500/3, (500-20)))
    pygame.draw.line(screen, (0,0,0), (2*(500/3), 20), (2*500/3, 500-20))
    pygame.draw.line(screen, (0,0,0), (20, 500/3), (500-20, 500/3))
    pygame.draw.line(screen, (0,0,0), (20, 2*500/3), (500-20, 2*500/3))


def drawstatus():
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
            drawstatus()
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
            t = time.time()
            minimaxe = minimaxer(copy.deepcopy(spielbrett_save1), -1)
            ai_value, ai_reihe, ai_stelle = minimaxe.wert, minimaxe.zeile, minimaxe.spalte
            print("Minimax done in "+str(time.time()-t))

            t = time.time()
            minimaxx = minmax_alpha_beta.minimaxer(copy.deepcopy(spielbrett_save1), -1)
            ai_value1, ai_reihe1, ai_stelle1 = minimaxx.wert, minimaxx.zeile, minimaxx.spalte
            print("Alpha-Beta done in "+str(time.time()-t))

            print("COMPARISON: "+str(ai_value)+":"+str(ai_value1)+"/"+str(ai_stelle)+" "+str(ai_reihe)+":"+str(ai_stelle1)+str(ai_reihe1))

            print("Ai Value: {}".format(ai_value))

            print("Wins: {}, Losses: {}, Draws: {}".format(minimaxe.nr_win, minimaxe.nr_lose, minimaxe.nr_draw))

            print("AI moves to: {}/{}".format(ai_reihe, ai_stelle))
            spielbrett[ai_reihe1][ai_stelle1] = -1
            print("AI done")
            print("AI 3: {}".format(checktictactoe(spielbrett.copy(), -1)))

            if checkvollesbrett(spielbrett.copy()):
                print("DRAW!")
                print(spielbrett)
                drawboard()
                drawstatus()
                done = True
            if checktictactoe(spielbrett.copy(), 1):
                print("Spieler gewinnt!")
                print(spielbrett)
                drawboard()
                drawstatus()
                done = True
            elif checktictactoe(spielbrett.copy(), -1):
                print("KI gewinnt!")
                print(spielbrett)
                drawboard()
                drawstatus()
                done = True
            drawboard()
            drawstatus()
            pygame.display.flip()
            print(spielbrett)
            print(RenderTree(nodes[0]))


# Exit loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
            sys.exit(0)
