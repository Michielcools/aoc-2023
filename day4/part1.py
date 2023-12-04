def main():
    file = open("day4/input.txt","r")
    out = 0
    for line in file:
        newline = line.strip("\n")
        parts = newline.split("|")
        parts[0] = parts[0].split(":")[1]
        parsed = []
        for part in parts:
            parsed.append(part.split(" "))
        win = 0
        for nr in parsed[0]:
            if nr in parsed[1] and nr != "":
                win+=1
        if win > 0:
            out+= 2**(win-1)
    print(out)

main()