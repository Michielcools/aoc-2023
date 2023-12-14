import array


def main():
    file = open("day12/input.txt", "r")
    out = 0
    for line in file:
        line = line.strip("\n")
        line = line.split()
        pos = []
        i = 0
        while i < len(line[0]):
            if line[0][i] == "?":
                pos.append(i)
            i+=1
        config = line[1].split(",")
        config = [int(x) for x in config]
        if len(pos) == 0:
            out += checkvalid(line[0],config)
        else:
            counter = [0]*len(pos)
            carr = 0
            while carr == 0:
                carr = 1
                i = len(pos)-1
                while i >= 0:
                    counter[i] = counter[i] + carr
                    carr = counter[i]//2
                    counter[i] = counter[i] % 2
                    i-=1
                i = 0
                curline = line[0]
                while i < len(pos):
                    if counter[i] == 1:
                        curline = curline[0:pos[i]] + "#" + curline[pos[i]+1:]
                    else:
                        curline = curline[0:pos[i]] + "." + curline[pos[i]+1:]
                    i+= 1 
                out += checkvalid(curline,config.copy())
            print(out)
        
        
def checkvalid(line : list, config : list,i):
    i = 0
    streak = 0
    while i < len(line):
        if line[i] == "#":
            streak  += 1
            if len(config) == 0:
                return 0
        if line[i] == "." and streak > 0:
            if config[0] != streak:
                return 0
            else:
                config.pop(0)
            streak = 0
        i+=1
    if streak != 0 and len(config) == 0:
        return 0
    elif streak == 0 and len(config) == 0:
        return 1
    elif streak == config[0] and len(config) == 1:
        return 1
    return 0
main()
