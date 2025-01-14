from collections import deque

grid = []
with open('in/in.test', 'r') as f:
#with open('in/in.pub', 'r') as f:
    for line in f:
        grid.append(line.strip())

n, m = len(grid), len(grid[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
regions = set()


def flood_fill(grid, x, y, visited, plant_type):
    queue = deque([(x, y)])
    visited[x][y] = True

    area = 0
    perimeter = 0


    while queue:
        cx, cy = queue.popleft()
        area += 1
        regions.add((cx, cy))

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == plant_type and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter


def part1():
    visited = [[False for _ in range(m)] for _ in range(n)]
    total_price = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                plant_type = grid[i][j]
                area, perimeter, _ = flood_fill(grid, i, j, visited, plant_type)
                total_price += area * perimeter

    return total_price


def part2():
    visited = [[False for _ in range(m)] for _ in range(n)]
    total_price = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                plant_type = grid[i][j]
                area, _, sides = flood_fill(grid, i, j, visited, plant_type)
                print(area, sides)
                total_price += area * sides

    return total_price

   


#print(part1())
print(part2())


