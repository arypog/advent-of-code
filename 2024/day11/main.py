rocks = []
with open('in/in.pub', 'r') as f:
#with open('in/in.test', 'r') as f:
    for i, line in enumerate(f.readlines()):
        rocks.append(line.strip())
rocks = rocks[0].split(" ")
# n = len(rocks)


def part1(rocks, n):
    for _ in range(n):
        new_rocks = []
        for rock in rocks:
            if rock == "0":
                new_rocks.append("1")
            elif len(rock) % 2 == 0:
                new_rocks.append(str(int(rock[:len(rock) // 2])))
                new_rocks.append(str(int(rock[len(rock) // 2:])))
            else:
                new_rocks.append(str(int(rock) * 2024))
        rocks = new_rocks
    return len(rocks)


from collections import defaultdict


def part2(rocks, n):
    memo = defaultdict(dict)
    total = 0

    for rock in rocks:
        total += n_rock(rock, n, memo)
    
    return total 


def n_rock(rock, n, memo):
    if n == 0:
        return 1
    
    if rock in memo and n in memo[rock]:
        return memo[rock][n]
    
    r = 0
    if rock == "0":
        r = n_rock("1", n - 1, memo)
    elif len(rock) % 2 == 0:
        mid = len(rock) // 2
        r = n_rock(str(int(rock[:mid])), n - 1, memo) + \
            n_rock(str(int(rock[mid:])), n - 1, memo)
    else:
        number = int(rock)
        r = n_rock(str(number * 2024), n - 1, memo)
    
    if rock not in memo:
        memo[rock] = {}
    memo[rock][n] = r
    return r

def part3(rocks, n):
    # Iterative way :c
    return

print(part1(rocks.copy(), 25), part2(rocks.copy(), 75))
print(part3(rocks.copy(), 75))