def get_input(file):
    return [[[int(x) for x in coordinate.split(",")] for coordinate in line.split(" -> ")] for line in
            open(file).read().splitlines()]


def second_star(coordinates):
    return


def get_walls(coordinates):
    walls = set()
    for wall in coordinates:
        for i in range(len(wall) - 1):
            x1, y1 = wall[i]
            x2, y2 = wall[i + 1]
            while x1 != x2:
                walls.add((x1, y1))
                x1 = x1 - 1 if x1 > x2 else x1 + 1
            walls.add((x1, y1))
            while y1 != y2:
                walls.add((x1, y1))
                y1 = y1 - 1 if y1 > y2 else y1 + 1
            walls.add((x1, y1))
    return walls


def first_star(coordinates):
    walls = get_walls(coordinates)
    max_y = max(walls, key=lambda item: item[1])[1]
    sandxStart, sandyStart = 500, 0
    sands = set()
    sandIsFalling = False
    while not sandIsFalling:
        sandx, sandy = sandxStart, sandyStart
        while True:
            if (sandx, sandy + 1) not in (walls | sands):
                sandy += 1
                if sandy > max_y+1:
                    sandIsFalling = True
                    break
                continue
            else:
                if (sandx - 1, sandy + 1) not in (walls | sands):
                    sandx -= 1
                    sandy += 1
                    continue
                elif (sandx + 1, sandy + 1) not in (walls | sands):
                    sandx += 1
                    sandy += 1
                    continue

            sands.add((sandx, sandy))
            break
    return len(sands)


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
