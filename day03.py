import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'day03.txt'

with open(infile) as file:
    map = file.readlines()
    map = [line.strip() for line in map]

XN0 = {}
XN1 = {}
for ligne in map:
    for i in range(len(ligne)):
      #  print(i, ligne[i])
        ind = int(ligne[i:i+1])
        if i not in XN0:
            XN0[i] = 0
        if i not in XN1:
            XN1[i] = 0
        # ensuite
        if (ind == 0):
            XN0[i] += 1
        else:
            XN1[i] += 1

print("XN0", XN0)
print("XN1", XN1)

A = list(map)
B = list(map)
result = ''
for i in range(XN0.__len__()):
    # part one
    if (XN0[i] < XN1[i]):
        result = result+'1'
    else:
        result = result+'0'
    # part two  -- voir la video sur https://www.youtube.com/watch?v=bFpsqFSCCsM (merci)
    if (len(A) > 1):
        a0 = len([x for x in A if x[i] == '0'])
        a1 = len([x for x in A if x[i] == '1'])
        if a1 >= a0:
            A = [x for x in A if x[i] == '1']
        else:
            A = [x for x in A if x[i] == '0']

    if (len(B) > 1):
        b0 = len([x for x in B if x[i] == '0'])
        b1 = len([x for x in B if x[i] == '1'])
        if b1 >= b0:
            B = [x for x in B if x[i] == '0']
        else:
            B = [x for x in B if x[i] == '1']
    #print(A, B)
    #print("a0", a0, "a1", a1, "| b0", b0, "b1", b1)

x = int(result, 2)
# Convert a binary string to a decimal int.
y = int(result, 2) ^ int('111111111111', 2)
#print(x, bin(x)[2:].zfill(len(result)))
#print(y, bin(y)[2:].zfill(len(result)))
print("")
print("result part one:", x, "*", y, "=", x*y)
print("result part two:", int(A[0], 2), "*",
      int(B[0], 2), "=", int(A[0], 2)*int(B[0], 2))
