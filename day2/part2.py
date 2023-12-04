file = open("day2/input.txt", "r")
gamenr = 0
out = 0
for line in file:
    mincubes = {"red": 0, "blue": 0, "green": 0}
    goodgame = True
    line = line.strip("\n")
    cleanline = line.split(":")
    gamenr += 1
    sets = cleanline[1].split(";")
    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            color = cube.split(" ")
            if mincubes[color[2]] < int(color[1]):
                mincubes[color[2]] = int(color[1])
    out += mincubes["red"]*mincubes["blue"]*mincubes["green"]
print(out)
        