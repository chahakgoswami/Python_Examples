def rot_oranges(grid):
    rows = len(grid)
    cols = len(grid[0])
    changed = False
    no = 2

    while True:
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == no:
                    if is_safe(i + 1, j) and grid[i + 1][j] == 1:
                        grid[i + 1][j] = grid[i][j] + 1
                        changed = True
                    if is_safe(i - 1, j) and grid[i - 1][j] == 1:
                        grid[i - 1][j] = grid[i][j] + 1
                        changed = True
                    if is_safe(i, j + 1) and grid[i][j + 1] == 1:
                        grid[i][j + 1] = grid[i][j] + 1
                        changed = True
                    if is_safe(i, j - 1) and grid[i][j - 1] == 1:
                        grid[i][j - 1] = grid[i][j] + 1
                        changed = True

        if not changed:
            break

        changed = False
        no += 1

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return -1

    return no - 2

def is_safe(i, j):
    return 0 <= i < R and 0 <= j < C

# Example usage
R = 3
C = 5
v = [[2, 1, 0, 2, 1],
     [1, 0, 1, 2, 1],
     [1, 0, 0, 2, 1]]

print(rot_oranges(v))
