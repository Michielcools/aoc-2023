file = open("day11/input.txt", "r")
input = []
for line in file:
    input.append(line.strip("\n"))
rows = [i for i in range(0,len(input))]
cols = [i for i in range(0, len(input[0]))]
i = 0
while i < len(input):
    j = 0
    while j < len(input):
        if input[i][j] == "#":
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)
        j+=1
    i+=1
i = 0
for row in rows:
    input.insert(row+i,input[row+i])
    i+=1
i = 0
for col in cols:
    j = 0
    while j < len(input):
        input[j] = input[j][:col+i] + input[j][col+i] + input[j][col+i:]  
        j+=1
    i+=1
pos = []
i = 0
while i < len(input):
    j = 0
    while j < len(input[0]):
        if input[i][j] == "#":
            pos.append((i,j))
        j+=1
    i+=1
out = 0
i = 0
while i < len(pos):
    j = i
    while j < len(pos):
        out += abs(pos[j][0] - pos[i][0])
        out += abs(pos[j][1] - pos[i][1])
        j+=1
    i+=1
print(out)