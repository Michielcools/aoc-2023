from curses.ascii import SP
from numpy import row_stack

def findpos(arr, pos):
    i = 0
    while arr[i] < pos:
        i += 1
    return i


SPACE = 1000000
file = open("day11/input.txt", "r")
input = []
for line in file:
    input.append(line.strip("\n"))
rows = [i for i in range(0,len(input))]
cols = [i for i in range(0, len(input[0]))]
i = 0
while i < len(input):
    j = 0
    while j < len(input):
        if input[i][j] == "#":
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)
        j+=1
    i+=1
rows.append(len(input))
cols.append(len(input[0]))
i = 0
pos = []
while i < len(input):
    j = 0
    while j < len(input[0]):
        if input[i][j] == "#":
            pos.append((i,j))
        j+=1
    i+=1
out = 0
i = 0
while i < len(pos):
    j = i
    while j < len(pos):
        out += abs(pos[j][0] - pos[i][0])
        out += (SPACE-1) * (abs(findpos(rows, pos[j][0]) - findpos(rows, pos[i][0])))
        out += abs(pos[j][1] - pos[i][1])
        out += (SPACE-1) * (abs(findpos(cols, pos[j][1]) - findpos(cols, pos[i][1])))
        j+=1
    i+=1
print(out)