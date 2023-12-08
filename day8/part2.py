from curses.ascii import isalpha
import numpy as np
import re

file = open("day8/input.txt", "r")
text = []
kaart = {}
for line in file:
    text.append(line.strip("\n"))
instructions = text[0]
instructionTranslate = {"R":1, "L":0}
i = 2
for ding in text[2:]:
    ding = re.sub(r'[^A-Za-z0-9 ]+', '', ding)
    ding = ding.split()
    kaart[ding[0]] = (ding[1],ding[2])
i = 0
plaats = []
for index in kaart.keys():
    if index[2] == "A":
        plaats.append(index)
kvg = [0]*len(plaats)
done = False
while not done:
    j = 0
    while j < len(plaats):
        plaats[j] = kaart[plaats[j]][instructionTranslate[instructions[i%len(instructions)]]]
        j+=1
    done = True
    j = 0
    while j < len(plaats):
        if plaats[j][2] == "Z" and kvg[j] == 0:
            kvg[j] = i+1
        j+=1
    for getal in kvg:
        if getal == 0:
            done = False
    i+=1
x = np.lcm.reduce(np.array(kvg))
print(x)