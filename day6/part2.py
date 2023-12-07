file = open("day6/input.txt", "r")
input = []
for line in file:
    input.append(int("".join(line.split()[1:])))
maxd = input[1]
i = 0
while i * (input[0]-i) < maxd:
    i+=1
print(input[0]- 2*i +1)