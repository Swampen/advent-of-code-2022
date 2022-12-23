def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    newLines = set()
    for line in lines:
        x, y, z = line.split(",")
        newLines.add((int(x), int(y), int(z)))
    return newLines


def make_step(s, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(len(grid[i][j])):
                if grid[i][j][k] == s:
                    if i > 0 and grid[i - 1][j][k] == 0:
                        grid[i - 1][j][k] = s + 1
                    if j > 0 and grid[i][j - 1][k] == 0:
                        grid[i][j - 1][k] = s + 1
                    if k > 0 and grid[i][j][k - 1] == 0:
                        grid[i][j][k - 1] = s + 1
                    if i < len(grid) - 1 and grid[i + 1][j][k] == 0:
                        grid[i + 1][j][k] = s + 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1][k] == 0:
                        grid[i][j + 1][k] = s + 1
                    if k < len(grid[i][j]) - 1 and grid[i][j][k + 1] == 0:
                        grid[i][j][k + 1] = s + 1


def second_star(coordinates):
    max_x = max(coordinates, key=lambda item: item[0])[0]
    max_y = max(coordinates, key=lambda item: item[1])[1]
    max_z = max(coordinates, key=lambda item: item[2])[2]

    grid = [[[0 for _ in range(max_x + 2)] for _ in range(max_y + 2)] for _ in range(max_z + 2)]
    for cube in coordinates:
        x, y, z = cube
        grid[z][y][x] = 1
    size = max_x * max_y * max_z
    i = 1
    grid[0][0][0] = 2
    while i < size:
        i += 1
        make_step(i, grid)
    empty = []
    for z in range(len(grid)):
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                if grid[z][y][x] == 0:
                    empty.append((x, y, z))

    for z in grid:
        for y in z:
            print(y)
        print("")
    print(len(empty))
    notSurfaceCount = 0
    for air in empty:
        for i in [1, -1]:
            x, y, z = air
            if (x + i, y, z) in coordinates:
                notSurfaceCount += 1
            if (x, y + i, z) in coordinates:
                notSurfaceCount += 1
            if (x, y, z + i) in coordinates:
                notSurfaceCount += 1
    return first_star(coordinates) - notSurfaceCount


def first_star(coordinates):
    total = 0
    for cube in coordinates:
        faces = 6
        for i in [1, -1]:
            x, y, z = cube
            if (x + i, y, z) in coordinates:
                faces -= 1
            if (x, y + i, z) in coordinates:
                faces -= 1
            if (x, y, z + i) in coordinates:
                faces -= 1
        total += faces
    return total


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
