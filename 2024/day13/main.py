import re

grid = []
#with open('in/in.test', 'r') as f:
with open('in/in.pub', 'r') as f:
    for line in f:
        if line != "\n":
            grid.append(line.strip())
n, m = len(grid), len(grid[0])


def find_min(ax, ay, bx, by, x, y):
    for i in range(101):
        for j in range(100):
            px = (i * ax) + (j * bx)
            py = (i * ay) + (j * by)
            if px == x and py == y:
                return i*3 + j*1

    return 0

# Diophantine
def smart_find(ax, ay, bx, by, x, y):
    cost = 0
    denomk1 = bx*ay - by*ax
    if denomk1 != 0 and bx != 0:
        k1num = y*bx - by*x
        if k1num % denomk1 == 0:
            k1 = k1num // denomk1
            k2num = x - (ax*k1)
            if k2num % bx == 0:
                k2 = k2num // bx
                cost = k1 * 3 + k2
    
    return cost

def smart_find_B(ax, ay, bx, by, x, y):
    det = ax * by - ay * bx
    a = (x * by - y * bx) // det
    b = (ax * y - ay * x) // det
    if ax * a + bx * b == x and ay * a + by * b == y:
        return a * 3 + b
    else:
        return 0

total, total2, total3 = 0, 0, 0
lines = iter(grid)
for line in lines:
    ax, ay = re.findall(r"\d+", line)
    bx, by = re.findall(r"\d+", next(lines))
    x, y = re.findall(r"\d+", next(lines))

    ax, ay, bx, by, x, y = int(ax), int(ay), int(bx), int(by), int(x), int(y) 
    total += find_min(ax, ay, bx, by, x, y)

    k = 10_000_000_000_000
    total2 += smart_find(ax, ay, bx, by, x+k, y+k)
    total3 += smart_find_B(ax, ay, bx, by, x, y)


print(total, total2, total3)



