def main():
    file = open("day4/input.txt","r")
    out = 0
    amount = {}
    size = len(file.readlines())
    i = 1
    while i <= size:
        amount[i] = 1
        i+=1
    file = open("day4/input.txt","r")
    for line in file:
        newline = line.strip("\n")
        parts = newline.split("|")
        newpart = parts[0].split(":")
        gamenr = newpart[0].strip("Card")
        gamenr = gamenr.replace(" ", "")
        gamenr = int(gamenr)
        parts[0] = newpart[1]
        parsed = []
        for part in parts:
            parsed.append(part.split(" "))
        win = 0
        for nr in parsed[0]:
            if nr in parsed[1] and nr != "":
                win+=1
        i = 1
        while i <= win:
            amount[gamenr+i] += amount[gamenr]
            i+=1
    for ding in amount:
        out += amount[ding]
    print(out)
main()