grid = []
with open('in/in.test', 'r') as f:
#with open('in/in.pub', 'r') as f:
    for line in f:
        grid.append(line.strip())

perimeter = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1':
            # Check top edge
            if i == 0 or (i > 0 and grid[i-1][j] == '0'):
                perimeter += 1
            # Check bottom edge
            if i == len(grid) - 1 or (i < len(grid)-1 and grid[i+1][j] == '0'):
                perimeter += 1
            # Check left edge
            if j == 0 or (j > 0 and grid[i][j-1] == '0'):
                perimeter += 1
            # Check right edge
            if j == len(grid[0]) - 1 or (j < len(grid[0])-1 and grid[i][j+1] == '0'):
                perimeter += 1

print(perimeter)