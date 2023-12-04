from curses.ascii import isdigit

def checksurround(i,j,text):
    out = 0
    parts = []
    if j > 0:
        k = i-1
        while k <= i+1:
            a = checksq(k,j-1,text)
            if  not a in parts and a != "":
                parts.append(a)
            k += 1
    k = i-1
    while k <= i+1:
        a = checksq(k,j,text)
        if not a in parts and a != "":
            parts.append(a)
        k+=1
    if j < len(text[i])-1:
        k = i-1
        while k <= i+1:
            a = checksq(k,j+1,text)
            if  not a in parts and a != "":
                parts.append(a)
            k += 1
    if len(parts) == 2:
        out = 1
        for ding in parts:
            out *= int(ding)
    return out  

def checksq(i,j,text):
    ret = ""
    if isdigit(text[i][j]):
        ret += text[i][j]
        k = j-1
        while k >= 0 and isdigit(text[i][k]):
            ret = text[i][k] + ret
            k-=1
        k = j+1
        while k <= len(text[i])-1 and isdigit(text[i][k]):
            ret += text[i][k]
            k+=1
    return ret




def main():
    out = 0
    file = open("day3/input.txt", "r")
    text = []
    for line in file:
        newline = line.strip("\n")
        text.append(newline)
    text.append("."*len(text[0]))
    text.insert(0,"."*len(text[0]))
    i = 0
    while i < len(text):
        j = 0
        while j < len(text[i]):
            if text[i][j] == "*":
                out += checksurround(i,j,text)
            j+=1
        i+=1
    print(out)


main()