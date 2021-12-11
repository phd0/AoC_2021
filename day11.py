lines = list(map(lambda line: list(map(int, line)),
             open('day11.txt').read().split('\n')))

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

ALREADY_FLASHED = 11


def solve(part, items):
    resultat = 0
    for item in range(items):
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                lines[x][y] += 1
        newFlash = True
        while newFlash:
            newFlash = False
            for x in range(len(lines)):
                for y in range(len(lines[x])):
                    if (lines[x][y] == 10):
                        lines[x][y] = ALREADY_FLASHED
                        newFlash = True
                        for d in range(8):
                            x2 = x + dx[d]
                            y2 = y + dy[d]
                            if (x2 >= 0 and y2 >= 0 and x2 < len(lines) and y2 < len(lines[x2]) and lines[x2][y2] < 10):
                                lines[x2][y2] += 1

            if (part == 1 and not newFlash):
                break
        win = 0
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if (lines[x][y] == ALREADY_FLASHED):
                    resultat += 1
                    lines[x][y] = 0
                if (lines[x][y] == 0):
                    win += 1

        if (part == 2 and win >= 90 and win < 100):
            print(item+101, "->", win)
        if (part == 2 and win >= 100):
            return item+101

    return resultat


print(solve(1, 100))
print(solve(2, 1000))
