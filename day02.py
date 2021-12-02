avance = 0
depth = 0
aim = 0

with open('day02.txt') as file:
    map = file.readlines()

for ligne in map:
    #    analyse(ligne)
    mouvement = ligne[0:-3]
    NN = int(ligne[-2:-1])
#   print(mouvement, NN, "", sep="|")
    if (mouvement == 'forward'):
        avance = avance + NN
    if (mouvement == "up"):
        depth = depth - NN
    if (mouvement == "down"):
        depth = depth + NN

# resultat phase 01
print("phase 01", avance*depth)

avance = 0
depth = 0
aim = 0

for ligne in map:
    mouvement = ligne[0:-3]
    NN = int(ligne[-2:-1])
    if (mouvement == 'forward'):
        avance = avance + NN
        depth = depth + (NN*aim)
    if (mouvement == "up"):
        aim = aim - NN
    if (mouvement == "down"):
        aim = aim + NN

# resultat phase 02
print("phase 02", avance*depth)
