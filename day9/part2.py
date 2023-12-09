file = open("day9/input.txt", "r")
out = 0
for line in file:
    line = line.split()
    arr = [[ int(x) for x in line ]]
    stop = False
    while not stop:
        newarr = []
        i=1
        while i < len(arr[-1]):
            newarr.append(arr[-1][i]-arr[-1][i-1])
            i+=1
        arr.append(newarr)
        stop = True
        for nr in arr[-1]:
            if nr != 0:
                stop = False
    arr[-1].insert(0,0)
    i = len(arr) - 2
    while i >= 0:
        arr[i].insert(0, arr[i][0] - arr[i+1][0])
        i -= 1
    out += arr[0][0]
print(out)
