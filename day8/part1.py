from curses.ascii import isalpha
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
plaats = "AAA"
while plaats != "ZZZ":
    plaats = kaart[plaats][instructionTranslate[instructions[i%len(instructions)]]]
    i+=1
print(i)