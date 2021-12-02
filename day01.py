last = 0
result_A = 0
result_B = 0
numlist = []

try:
    liste1 = open("day01.txt", "r")
except:
    print("fichier introuvable")
else:
    for laliste in liste1:
        numlist.append(int(laliste))

    print(numlist.__len__(), "echantillons")
    for number in numlist:
        if (last == 0):
            last = number
        elif (last < number):
            last = number
            result_A = result_A + 1
        else:
            last = number
    print("result day01.A=", result_A, sep="")
    # 2eme partie
    NN = 0
    NN1 = 0
    NN2 = 0
    for NN in range(numlist.__len__()):
        try:
            NN1 = numlist[NN]+numlist[NN+1]+numlist[NN+2]
            NN2 = numlist[NN+1]+numlist[NN+2]+numlist[NN+3]
            if (NN2 > NN1):
                result_B = result_B + 1
                # print("->", NN, NN1, NN2, result_B, sep=" ")
        except:
            pass
            #print("exception NN=", NN)
    print("result day01.B=", result_B, sep="")
