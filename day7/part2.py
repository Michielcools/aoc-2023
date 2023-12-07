repl = {"2": 2, "3": 3, "4": 4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9,"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}

def main():
    file = open("day7/input.txt" , "r")
    games = []
    for line in file:
        games.append(line.split())
    for game in games:
        amount = [0]*15
        for card in game[0]:
            amount[repl[card]] += 1
        max = amount[1]
        secmax = 0
        i = 0
        while i < len(amount):
            getal = amount[i]
            if getal + amount[1] > max and i != 1:
                secmax = max - amount[1]
                max = getal + amount[1]
            elif getal > secmax:
                secmax = getal
            i+=1
        if max == 3 and secmax == 2:
            game.append(4)
        elif max == 2 and secmax == 2:
            game.append(2)
        elif max >= 4:
            game.append(max+1)
        elif max == 3:
            game.append(max)
        else:
            game.append(max-1)
    games = sortgames(games)
    out = 0
    i = 1
    while i-1 < len(games):
        out += int(games[i-1][1]) * i
        i+= 1
    print(out)

def sortgames(games):
    order = []
    while 0 < len(games):
        j = 0
        mintype = 7
        bottom = []
        while j < len(games):
            if games[j][2] < mintype:
                mintype = games[j][2]
                bottom = []
                bottom.append(games[j])
            elif games[j][2] == mintype:
                bottom.append(games[j])
            j+=1
        for ding in bottom:
            games.remove(ding)
        while 0 < len(bottom):
            j = 0
            toCheck = bottom
            while len(toCheck) > 1:
                small = 15
                for kaart in toCheck:
                    if repl[kaart[0][j]] < small:
                        small = repl[kaart[0][j]]
                newToCheck = toCheck.copy()
                for kaart in toCheck:
                    if repl[kaart[0][j]] > small:
                        newToCheck.remove(kaart)
                toCheck = newToCheck
                j+=1
            order.append(toCheck[0])
            bottom.remove(toCheck[0])
    return order

main()

