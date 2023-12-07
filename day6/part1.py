file = open("day6/input.txt", "r")
input = []
for line in file:
    input.append(line.split()[1:])
i = 0
out = 1
temp = 0
while i < len(input[0]):
    temp = 0
    maxd = int(input[1][i])
    for nr in range(0,int(input[0][i])):
        d = nr * (int(input[0][i])- nr)
        if d > maxd:
            temp += 1
    if temp >= 1:
        out *= temp
    i+=1
print(out)