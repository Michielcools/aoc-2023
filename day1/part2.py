from curses.ascii import isdigit
numbers = {"zero": 0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
file = open("input.txt", "r")
final = ""
output = 0
numfound = False
for line in file:
    numfound = False
    final = ""
    i = 0
    cur = ""
    while i < len(line) and not numfound:
        if isdigit(line[i]):
            final += line[i]
            break
        else:
            cur += line[i]
            for numb in numbers:
                if numb in cur:
                    numfound = True
                    final += str(numbers[numb])
                    break
        i += 1
    i = -1
    numfound = False
    cur = ""
    while abs(i) <= len(line) and not numfound:
        if isdigit(line[i]):
            final += line[i]
            break
        else:
            cur = line[i] + cur
            for numb in numbers:
                cur += line[i]
                if numb in cur:
                    numfound = True
                    final += str(numbers[numb])
                    break
        i -= 1
    output += int(final)
print(output)