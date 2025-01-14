from collections import deque


def count_reachable_height_9(grid, start_x, start_y):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start_x][start_y] = True

    reachable_height_9_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                current_height = int(grid[x][y])
                next_height = int(grid[nx][ny])

                if next_height == 9 and current_height == 8:
                    reachable_height_9_count += 1

                if next_height == current_height + 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return reachable_height_9_count


def count_distinct_trails_to_height_9(grid, start_x, start_y):
    rows = len(grid)
    cols = len(grid[0])
    unique_trails = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque([[(start_x, start_y)]])

    while q:
        trail = q.popleft()
        x, y = trail[-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                current_height = int(grid[x][y])
                next_height = int(grid[nx][ny])

                if next_height == 9 and current_height == 8:
                    new_trail = trail + [(nx, ny)]
                    unique_trails.add(tuple(new_trail))

                elif next_height == current_height + 1 and (nx, ny) not in trail:
                    new_trail = trail + [(nx, ny)]
                    q.append(new_trail)

    return len(unique_trails)


grid = []
#with open('in/in.test', 'r') as f:
with open('in/in.pub', 'r') as f:
    for line in f.readlines():
        grid.append(line.strip())

total_p1 = 0
total_p2 = 0

rows = len(grid)
cols = len(grid[0])
for a in range(rows):
    for b in range(cols):
        if grid[a][b] == '0':
            total_p1 += count_reachable_height_9(grid, a, b)
            total_p2 += count_distinct_trails_to_height_9(grid, a, b)

print(total_p1, total_p2)
