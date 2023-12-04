file = open("day2/input.txt", "r")
gamenr = 0
maxcubes = {"red": 12, "blue": 14, "green": 13}
out = 0
for line in file:
    goodgame = True
    line = line.strip("\n")
    cleanline = line.split(":")
    gamenr += 1
    sets = cleanline[1].split(";")
    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            color = cube.split(" ")
            if maxcubes[color[2]] < int(color[1]):
                goodgame = False
    if goodgame == True:
        out += gamenr
print(out)
        