from curses.ascii import isdigit

def checksurround(i,j,text):
    if j > 0:
        k = i-1
        while k <= i+1:
            if checksq(k,j-1,text):
                return True
            k += 1
    k = i-1
    while k <= i+1:
        if checksq(k,j,text):
            return True
        k += 1
    if j < len(text[i])-1:
        k = i-1
        while k <= i+1:
            if checksq(k,j+1,text):
                return True
            k += 1    

def checksq(i,j,text):
    if text[i][j] != "." and not isdigit(text[i][j]):
        return True
    return False


file = open("day3/input.txt", "r")
text = []
for line in file:
    newline = line.strip("\n")
    text.append(newline)
text.append("."*len(text[0]))
text.insert(0,"."*len(text[0]))
i = 0
out = 0
nr = ""
while i < len(text):
    surround = False
    nr = ""
    j = 0
    while j < len(text[i]):
        if isdigit(text[i][j]):
            nr += text[i][j]
            if checksurround(i,j,text):
                surround = True
        else:
            if nr != "" and surround:
                print(nr)
                out += int(nr)
                nr = ""
                surround = False
            else:
                nr = ""
                surround = False
        j+=1
    if nr != "" and surround:
        print(nr)
        out += int(nr)
        nr = ""
        surround = False
    else:
        nr = ""
        surround = False
    i+=1
print(out)
