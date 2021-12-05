import sys
import pygame
import math
from pygame.locals import*

screen_size = (1100, 650)
Color_screen = (30, 30, 30)
pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(Color_screen)
pygame.display.flip()
myfont10 = pygame.font.SysFont('Arial', 10)
myfont30 = pygame.font.SysFont('Arial', 30)

infile = sys.argv[1] if len(sys.argv) > 1 else 'day04.txt'
tirage = []
grilles = []


def writeX(i, x, y, data):
    '''
    affiche en rouge le data aux coord x,y de la grille i 
    '''
    textsurface = myfont10.render(str(data), False, (255, 0, 0))
    XX = int(5 + math.trunc(i / 8) * 80) + x*15
    YY = int(5 + ((i*80) % 640)) + y*15
    screen.blit(textsurface, (XX, YY))
    pygame.display.flip()
    pass


def writeText(i, y, data):
    '''
    affiche en blanc le chiffre data aux coord x,y de la grille i 
    data = [0, 0, 0, 0, 0, False]
    '''
    for x in range(5):
        textsurface = myfont10.render(str(data[x]), False, (255, 255, 255))
        XX = int(5 + math.trunc(i / 8) * 80) + x*15
        YY = int(5 + ((i*80) % 640)) + y*15
        screen.blit(textsurface, (XX, YY))
    pygame.display.flip()
    pass


def writeGG(i, tir):
    textsurface = myfont30.render(
        str(winNumber), False, (255, 255-round(tir*2.5), 255))
    XX = int(3 + math.trunc(i / 8) * 80)
    YY = int(3 + ((i*80) % 640))
    pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(XX, YY, 76, 76), 1)
    screen.blit(textsurface, (XX+20, YY+20))
    pygame.display.flip()
    pass


def isGagnante(data):
    winX = 0
    for x in range(5):
        if (data[x][0] == 'X' and data[x][1] == 'X' and data[x][2] == 'X' and data[x][3] == 'X' and data[x][4] == 'X'):
            winX = 5
    winY = 0
    for y in range(5):
        if (data[0][y] == 'X' and data[1][y] == 'X' and data[2][y] == 'X' and data[3][y] == 'X' and data[4][y] == 'X'):
            winY = 5
    if (data[5] == False and (winX == 5 or winY == 5)):
        data[5] = True
        return True
    return False


def analyse(G, leTirage):
    '''
    analyse une carte N°G et ajoute le N° tiré
    retourne zero si pas gagné, ou le nombre calculé
    '''
    total = 0
    for x in range(5):
        for y in range(5):
            if (grilles[G][x][y] != 'X' and int(leTirage) == int(grilles[G][x][y])):
                # la case est marquée comme gagnée
                grilles[G][x][y] = 'X'
                writeX(G, x, y, 'XX')
                # print("data[", G, " ", x, ",", y, "]=", grilles[G][x], "  tir=", int(leTirage), sep='')
                # active la case gagnée
                if (isGagnante(grilles[G])):
                    for xx in range(5):
                        for yy in range(5):
                            if (grilles[G][xx][yy] != 'X'):
                                total += int(grilles[G][xx][yy])
                    return int(leTirage)*int(total)
    return 0


def read5lines(i, thefile):
    '''
    pour le chargement des données
    le False sert à savoir si la grille a déja gagné une fois
    '''
    grille = [0, 0, 0, 0, 0, False]
    grille[0] = thefile.readline().strip().split()
    grille[1] = thefile.readline().strip().split()
    grille[2] = thefile.readline().strip().split()
    grille[3] = thefile.readline().strip().split()
    grille[4] = thefile.readline().strip().split()
    toto = thefile.readline()  # ligne la ligne vide entre deux grilles
    writeText(i, 0, grille[0])
    writeText(i, 1, grille[1])
    writeText(i, 2, grille[2])
    writeText(i, 3, grille[3])
    writeText(i, 4, grille[4])
    return grille


# chargement des données en tableau
with open(infile) as file:
    tirage = file.readline().strip().split(',')
    toto = file.readline()
    for i in range(100):
        grilles.append(read5lines(i, file))


# debut du programme
winNumber = 0
for tir in range(len(tirage)):
    for G in range(len(grilles)):
        result = analyse(G, tirage[tir])
        if (result > 0):
            winNumber += 1
            writeGG(G, winNumber)
            print("tirage N°", tir, " result= ", result, sep='')


while True:
    for events in pygame.event.get():
        if events.type == QUIT:
            sys.exit(0)
