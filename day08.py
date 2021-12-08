import sys


def analyse(data):
    total = 0
    line = data.split(' ')
    for i in line:
        if (len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7):
            total += 1
    return total


infile = sys.argv[1] if len(sys.argv) > 1 else 'day08.txt'
with open(infile) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

result = 0
for i in range(len(lines)):
    result += analyse(lines[i].split(' | ')[1])
print("part 1=", result)
