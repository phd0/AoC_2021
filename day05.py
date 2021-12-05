# with the source code part 1 of
# https://github.com/kodsnack/advent_of_code_2021/blob/main/cernael-python/5a.py
# for help me ...

def solve(part, lines):
    points, p = {}, []
    for l in lines:
        x1, y1, x2, y2 = [int(i) for i in l.replace(' -> ', ',').split(',')]
        if (y1 == y2):
            if x1 < x2:
                # hor, asc
                p = [(r, y2) for r in range(x1, x2 + 1)]
            else:
                # hor, desc
                p = [(r, y2) for r in range(x2, x1 + 1)]
        elif (x1 == x2):
            if y1 > y2:
                # ver, desc
                p = [(x1, r) for r in range(y2, y1 + 1)]
            else:
                # ver, asc
                p = [(x1, r) for r in range(y1, y2 + 1)]

        # part 2 add
        if (abs(x1-x2) == abs(y1-y2) and part == 2):
            if x1 < x2 and y1 < y2:
                p = [(x1+r, y1+r) for r in range(0, abs(x1-x2) + 1)]
            if x1 > x2 and y1 < y2:
                p = [(x1-r, y1+r) for r in range(0, abs(x1-x2) + 1)]
            if x1 < x2 and y1 > y2:
                p = [(x1+r, y1-r) for r in range(0, abs(x1-x2) + 1)]
            if x1 > x2 and y1 > y2:
                p = [(x1-r, y1-r) for r in range(0, abs(x1-x2) + 1)]

        for i in p:
            if i in points.keys():
                points[i] += 1
            else:
                points[i] = 1
        p = []
    return len(list(filter(lambda x: x >= 2, points.values())))


if __name__ == '__main__':
    lines = []
    with open('day05.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    print("Part 1=", solve(1, lines), sep='')
    print("Part 2=", solve(2, lines), sep='')
