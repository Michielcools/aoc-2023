from curses.ascii import isdigit


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
min = 0
for seed in seeds:
    nr = seed
    i = 0
    while i < len(maps):
        j = 0
        while j < len(maps[i]):
            if nr >= maps[i][j][1] and nr < maps[i][j][1] + maps[i][j][2]:
                nr = maps[i][j][1] + (maps[i][j][0] - maps[i][j][1]) + (nr - maps[i][j][1])
                j = len(maps[i])
            j+=1
        i+=1
    if int(nr) < min or min == 0:
        min = int(nr)
print(min)
    