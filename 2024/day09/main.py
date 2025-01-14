disk = []

with open('in/in.test', 'r') as f:
#with open('in/in.pub', 'r') as f:
    for line in f.readlines():
        disk.append(line.strip())

disk = disk[0]
class block:
    index : int
    used : int
    free : int

def part1():
    new_disk = []
    for i, di in enumerate(disk):
        if i % 2 == 0:
            g = []
            for _ in range(int(di)):
                new_disk.append(int(i/2))
        else:
            for _ in range(int(di)):
                new_disk.append(-1)

    print(new_disk)

    # soter
    for i in range(len(new_disk)):
        if new_disk[i] == -1:
            for j in range(len(new_disk) -1, i, -1):
                if new_disk[j] != -1:
                    new_disk[i], new_disk[j] = new_disk[j],new_disk[i]
                    break

    print(new_disk)
    total = 0
    for i, x in enumerate(new_disk):
        if x != -1:
            total += i * x

def part2():
    new_disk = []
    i = 0
    j = len(disk) - 1

    while i <= j:
        block = []
        used = 0
        free = 0
        for  
        

    for i, di in enumerate(disk):
        if i % 2 == 0:
            block = []
            free = 0
            used = 0
            for _ in range(int(di)):
                block.append(int(i/2))
            used += 1
        else:
            for _ in range(int(di)):
                free += 1
        new_disk.append((used,free,block))
        
        print(new_disk)

part2()