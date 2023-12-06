from curses.ascii import isdigit

from numpy import minimum


file = open("day5/input.txt", "r")
maps = []
lines = [line.rstrip() for line in file]
seeds = lines[0].split(" ")[1:]
seeds = list(map(int,seeds))
conv = []
for line in lines[2:]:
    if len(line) == 0:
        maps.append(conv)
        conv = []
    elif isdigit(line[0]):
        nrs = line.split(" ")
        nrs = list(map(int,nrs))
        conv.append(nrs)
maps.append(conv)
k = 0
toConv = []
totoConv = []
conv = []
while k < len(seeds):
    toConv.append((seeds[k], seeds[k+1]))
    k += 2
i = 0
while i < len(maps):
    j = 0
    while j < len(maps[i]):
        z = 0
        while z < len(toConv):
            if not (maps[i][j][1] + maps[i][j][2] < toConv[z][0] or maps[i][j][1] > toConv[z][0] + toConv[z][1]):
                start = max([maps[i][j][1], toConv[z][0]])
                end = min([maps[i][j][1] + maps[i][j][2], toConv[z][0] + toConv[z][1]])
                if start > toConv[z][0]:
                    totoConv.append((toConv[z][0], start - toConv[z][0]))
                conv.append((start - (maps[i][j][1] - maps[i][j][0]), end-start))
                if end > toConv[z][0] + toConv[z][1]:
                    totoConv.append((end, toConv[z][1] - end))
            else:
                totoConv.append((toConv[z][0], toConv[z][1]))
            z += 1
        toConv = totoConv
        totoConv = []
        j+=1
    toConv = toConv + conv
    conv = []
    i+=1
out = 0
for ding in toConv:
    if ding[0] < out or out == 0:
        out = ding[0]
print(out)