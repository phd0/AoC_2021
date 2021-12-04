import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'day04.txt'
tirage = []
grilles = []


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


def analyse(numm, leTirage):
    '''
    analyse une carte et ajoute le N° tiré
    retourne zero si pas gagné, ou le nombre calculé
    '''
    total = 0
    for x in range(5):
        for y in range(5):
            if (grilles[numm][x][y] != 'X' and int(leTirage) == int(grilles[numm][x][y])):
                # la case est marquée comme gagnée
                grilles[numm][x][y] = 'X'
                # print("data[", numm, " ", x, ",", y, "]=", grilles[numm][x], "  tir=", int(leTirage), sep='')
                # active la case gagnée
                if (isGagnante(grilles[numm])):
                    for xx in range(5):
                        for yy in range(5):
                            if (grilles[numm][xx][yy] != 'X'):
                                total += int(grilles[numm][xx][yy])
                    return int(leTirage)*int(total)
    return 0


def read5lines(thefile):
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
    return grille


# chargement des données en tableau
with open(infile) as file:
    tirage = file.readline().strip().split(',')
    toto = file.readline()
    try:
        for i in range(100):
            grilles.append(read5lines(file))
    except:
        print("except i=", i)


# debut du programme
for tir in range(len(tirage)):
    pass
    for G in range(len(grilles)):
        result = analyse(G, tirage[tir])
        if (result > 0):
            print("tirage N°", tir, " result= ", result, sep='')
