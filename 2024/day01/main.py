path = 'in/in.pub'

l1 = []
l2 = []

with open(path, 'r') as f: 
    for line in f:
       parts = line.strip().split(' ')
       l1.append(int(parts[0]))
       l2.append(int(parts[-1]))

l1.sort()
l2.sort()

def part1():
    total = 0
    for i, j in zip(l1, l2):
        d = abs(i - j)
        total = total + d
    return total


def part2():
    total = 0
    for i in l1:
        c = 0
        for j in l2: 
            if i == j :
                c += 1
        total = total + ( i * c )
    return total

# total = part1()
total = part2()
print(total)