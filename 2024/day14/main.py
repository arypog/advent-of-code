data = []
#with open('in/in.test', 'r') as f:
with open('in/in.pub', 'r') as f:
    for line in f:
        if line != "\n":
            data.append(line.strip())

robots = []
for line in data: 
    import re
    str_numbers = re.findall(r"-?\d+", line)
    x, y, dx, dy = map(int, str_numbers)
    robots.append((x,y,dx,dy))


def part1():
    t = 100
    a, b, c, d = 0, 0, 0, 0
    for (x, y, dx, dy) in robots:
        nx = (x + t * dx) % w
        if nx < 0 : nx += w

        ny = (y + t * dy) % h
        if ny < 0: ny += h

        cx, cy = w//2, h//2

        if nx == cx or ny == cy: continue
        if nx < cx and ny < cy: a += 1
        if nx > cx and ny > cy: b += 1
        if nx < cx and ny > cy: c += 1
        if nx > cx and ny < cy: d += 1
        
    return a * b * c * d


def part2(): 
    def flood_fill(grid, x, y, visited):
        from collections import deque

        w, h = len(grid[0]), len(grid)
        queue = deque([(x, y)])
        visited[y][x] = True
        area = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            cx, cy = queue.popleft()
            area += 1

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

        return area 


    def getL(grid):
        visited = [[False for _ in range(w)] for _ in range(h)]

        area = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] and not visited[y][x]:
                    n_area = flood_fill(grid, x, y, visited)
                    area = max(area, n_area)

        return area

    
    t = 0
    l_area = 0
    while True:
        grid = [[False for _ in range(w)] for _ in range(h)]

        for (x, y, dx, dy) in robots:
            nx = (x + t*dx) % w
            ny = (y + t*dy) % h

            grid[ny][nx] = True

        area = getL(grid)
        l_area = max(l_area, area)
        if l_area > 30:
            grid = [['.' for _ in range(w)] for _ in range(h)]
            for (x, y, dx, dy) in robots:
                nx = (x + t*dx) % w
                ny = (y + t*dy) % h
                grid[ny][nx] = 'X'

            with open("map", "w") as map_file:
                for row in grid:
                    map_file.write(''.join(row) + '\n')
            break

        t+=1

    return t


#w, h = 11, 7
w, h = 101, 103

print(part1())
print(part2())