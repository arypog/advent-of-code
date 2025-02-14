grid = []
moves = []
mov = False
with open('in/in.test', 'r') as f:
#with open('in/in.pub', 'r') as f:
    for line in f:
        if line == "\n":
            mov = True
        if mov:
            moves.append(line.strip())
        else:
            grid.append(line.strip())

grid = [list(row) for row in grid]
moves = moves[1:]
linear_moves = [move for row in moves for move in row]


directions = {
    '^' : (0, -1),   #up
    '>' : (1, 0),    #right
    '<' : (-1, 0),   #left
    'v' : (0, 1),    #bottom
}


n = len(grid[0])
m = len(grid)
def part1():
    px, py = next(
                    (i, j)  for i, row in enumerate(grid) 
                            for j, c in enumerate(row) if c == '@'
                )

    bas = 0
    for y in grid:
        for x in y:
            if x == 'O':
                bas+=1


    for move in linear_moves:
        d = directions[move]
        
        nx, ny = px , py
        while grid[ny][nx] != '#':
            if grid[ny][nx] == 'O' and grid[ny + d[1]][nx + d[0]] != '#':
                grid[ny - d[1]][nx - d[0]] = '.'
                grid[ny][nx] = '@'
                grid[ny + d[1]][nx + d[0]] = 'O'

            nx += d[0]
            ny += d[1]

        px, py = nx, ny

    
    total = 0
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == 'O':
                total += 100 * i + j

    bae = 0
    for y in grid:
        for x in y:
            if x == 'O':
                bae+=1

    for row in grid:
        print(str(row))
    print(total, bas, bae)


part1()