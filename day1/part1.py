from curses.ascii import isdigit


file = open("input.txt", "r")
final = ""
output = 0
for line in file:
    final = ""
    i = 0
    while i < len(line):
        if isdigit(line[i]):
            final += line[i]
            break
        i += 1
    i = -1
    while abs(i) <= len(line):
        if isdigit(line[i]):
            final += line[i]
            break
        i -= 1
    
    output += int(final)
print(output)