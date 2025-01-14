# gabrielzshcingfdstsz
import sys
from collections import deque

debug = False

def check_debug_flag(input_str):
    global debug
    pos = input_str.rfind('/')
    last_part = input_str if pos == -1 else input_str[pos + 1:]
    if last_part == "test":
        debug = True

# Directions for flood-fill (up, down, left, right)
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# Directions for corners
corner_directions = [(0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]

def is_in_bounds(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def sides(region):
    sides_count = 0
    corners = set()

    for cx, cy in region:
        for dx, dy in corner_directions:
            corners.add((cx + dx, cy + dy))

    for cx, cy in corners:
        adj_cells = [False] * 4
        n_adj = 0

        for i in range(4):
            nx = cx + corner_directions[i][0]
            ny = cy + corner_directions[i][1]
            adj_cells[i] = (int(nx), int(ny)) in region
            if adj_cells[i]:
                n_adj += 1

        if n_adj == 1 or n_adj == 3:
            sides_count += 1
        elif adj_cells == [True, False, True, False] or adj_cells == [False, True, False, True]:
            sides_count += 2

    return sides_count

def flood_fill(x, y, plants, visited, plant_type, region):
    m = len(plants)
    n = len(plants[0])
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        region.add((cx, cy))

        if debug:
            print(f"Visited: ({cx}, {cy})")

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_in_bounds(nx, ny, m, n) and not visited[nx][ny] and plants[nx][ny] == plant_type:
                visited[nx][ny] = True
                q.append((nx, ny))
                if debug:
                    print(f"Added to queue: ({nx}, {ny})")

    if debug:
        print(f"Region flood-filled. Total cells: {len(region)}")

def main():
    global debug
    user_input = sys.argv[1] if len(sys.argv) == 2 else "in/in.pub"
    check_debug_flag(user_input)

    try:
        with open(user_input, 'r') as input_file:
            plants = [list(line.strip()) for line in input_file.readlines()]
    except FileNotFoundError:
        print(f"FILE {user_input} UNAVAILABLE!")
        return

    m = len(plants)
    n = len(plants[0])
    visited = [[False] * n for _ in range(m)]
    total = 0

    for x in range(m):
        for y in range(n):
            if not visited[x][y]:
                plant_type = plants[x][y]
                region = set()

                if debug:
                    print(f"Starting flood fill for plant: {plant_type} at ({x}, {y})")
                flood_fill(x, y, plants, visited, plant_type, region)

                area = len(region)
                perimeter = 4 * area - len(region)
                region_sides = sides(region)

                total += area * region_sides
                if debug:
                    print(f"Region ({plant_type}) - Area: {area}, Sides: {region_sides}, Perimeter: {perimeter}")

    print(f"ANSWER: {total}")

if __name__ == "__main__":
    main()

