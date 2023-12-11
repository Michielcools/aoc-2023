import sys


def main():
    sys.setrecursionlimit(20000)
    file = open("day10/input.txt", "r")
    map = []
    for line in file:
        map.append("." + line.strip("\n") + ".")
    map.insert(0,"."*len(map[0]))
    map.append("."*len(map[0]))
    i = 0
    start = ()
    while i < len(map):
        j = 0
        while j < len(map[0]):
            if map[i][j] == "S":
                start = (i,j)
            j+=1
        i+=1
    visited = [start]
    loop = findloop(map,(start[0]+1,start[1]),1,visited)
    if len(loop) == 0:
        loop = findloop(map,(start[0]-1,start[1]),3,visited)
    if len(loop)== 0:
        loop = findloop(map,(start[0],start[1]+1),4,visited)
    if len(loop) == 0:
        loop = findloop(map,(start[0],start[1]-1),2,visited)
    i = 0
    out = 0
    while i < len(map):
        j = 0
        binnen = False
        boven = False
        beneden = False
        while j < len(map[0]):
            if (i,j) in loop:
                if map[i][j] == "|":
                    binnen = not binnen
                elif map[i][j] == "L":
                    boven = True
                elif map[i][j] == "F":
                    beneden = True
                elif map[i][j] == "7" and boven:
                    binnen = not binnen
                    boven = False
                elif map[i][j] == "7" and not boven:
                    beneden = False
                elif map[i][j] == "J" and beneden:
                    beneden = False
                    binnen = not binnen
                elif map[i][j] == "J" and not beneden:
                    boven = False
            else:
                if binnen:
                    out+=1
            j+=1
        i+=1
    print(out)

    
def findloop(map, curr, camefr, visited):
    if map[curr[0]][curr[1]] == "S": 
        return visited
    if map[curr[0]][curr[1]] == ".":
        return []
    visited.append(curr)
    if camefr == 1:
        if map[curr[0]][curr[1]] == "|":
            return findloop(map,(curr[0]+1,curr[1]), 1, visited)
        if map[curr[0]][curr[1]] == "L":
            return findloop(map,(curr[0],curr[1]+1), 4, visited)
        if map[curr[0]][curr[1]] == "J":
            return findloop(map,(curr[0],curr[1]-1), 2, visited)
    if camefr == 2:
        if map[curr[0]][curr[1]] == "-":
            return findloop(map,(curr[0],curr[1]-1), 2, visited)
        if map[curr[0]][curr[1]] == "L":
            return findloop(map,(curr[0]-1,curr[1]), 3, visited)
        if map[curr[0]][curr[1]] == "F":
            return findloop(map,(curr[0]+1,curr[1]), 1, visited)
    if camefr == 3:
        if map[curr[0]][curr[1]] == "|":
            return findloop(map,(curr[0]-1,curr[1]), 3, visited)
        if map[curr[0]][curr[1]] == "F":
            return findloop(map,(curr[0],curr[1]+1), 4, visited)
        if map[curr[0]][curr[1]] == "7":
            return findloop(map,(curr[0],curr[1]-1), 2, visited)
    if camefr == 4:
        if map[curr[0]][curr[1]] == "-":
            return findloop(map,(curr[0],curr[1]+1), 4, visited)
        if map[curr[0]][curr[1]] == "J":
            return findloop(map,(curr[0]-1,curr[1]), 3, visited)
        if map[curr[0]][curr[1]] == "7":
            return findloop(map,(curr[0]+1,curr[1]), 1, visited)

main()
