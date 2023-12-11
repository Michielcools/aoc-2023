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
        while j < len(map):
            if map[i][j] == "S":
                start = (i,j)
            j+=1
        i+=1
    out = 0
    visited = [start]
    out = findloop(map,(start[0]+1,start[1]),1,visited)
    if out == 0:
        out = findloop(map,(start[0]-1,start[1]),3,visited)
    if out == 0:
        out = findloop(map,(start[0],start[1]+1),4,visited)
    if out == 0:
        out = findloop(map,(start[0],start[1]-1),2,visited)
    print(out)
    
def findloop(map, curr, camefr, visited):
    if map[curr[0]][curr[1]] == "S": 
        return len(visited) // 2
    if map[curr[0]][curr[1]] == ".":
        return 0
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
