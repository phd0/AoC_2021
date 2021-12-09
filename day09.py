import math

debug =False
points={}

def solve(part,data):
    total=0
    for i in range(len(data)):
        for c in range(len(data[i])):
            XY=int(data[i][c])
            if (c < len(data[i])-1):
                XP=int(data[i][c+1])
            else:
                XP=9
            if (c > 0):
                XM=int(data[i][c-1])
            else:
                XM=9
            if (i < len(data)-1):
                YP=int(data[i+1][c])
            else:
                YP=9
            if (i > 0):
                YM=int(data[i-1][c])
            else:
                YM=9
            if (part==1 and XY < 9 and XY < XP and XY< XM and XY < YM and XY < YP):
                total += XY+1
                points[(i,c)]=XY
                win = True 
            else:
                win=False
            if (win and debug):
                print(" ",YM," ",sep='')
                print(XM,XY,XP,sep='')
                print(" ",YP," ",sep='')
            pass
    return total


if __name__ == '__main__':
    lines = []
    with open('day09.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print("Part 1=", solve(1, lines), sep='')
    print("Part 2=", solve(2, lines), sep='')
    
    #print(points)