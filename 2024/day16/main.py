grid = []
with open('in/in.test', 'r') as f:
#with open('in/in.pub', 'r') as f:
    for line in f:
        if line != "\n":
            grid.append(line.strip())


import heapq

def dijkstra(grid, start):
    rows, cols = len(grid), len(grid[0])
    INF = float('inf')

    dist = [[INF] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]]

    pq = [(0, start[0], start[1])]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        d, x, y = heapq.heappop(pq)
        print(x, y, d)

        if grid[x][y] == 'E':
            return d
        if d > dist[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                new_dist = d + grid[nx][ny]

                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
    return dist

def part1():
    start_token = 'S'
    end_token = 'E'

    start_pos = [(i, j)for i, a in enumerate(grid) for j, b in enumerate(a) if b == start_token]
    print(start_pos)
    result = dijkstra(grid, start_pos[0])

    print(result)


part1()

