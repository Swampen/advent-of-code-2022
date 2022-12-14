import json
import copy


def get_input(file):
    return [[[int(x) for x in coordinate.split(",")] for coordinate in line.split(" -> ")] for line in
            open(file).read().splitlines()]


def second_star(coordinates):
    return


def draw_walls(coordinates):
    furthestRight = 500
    furthestLeft = 500
    deepest = 0
    for wall in coordinates:
        for pos in wall:
            x, y = pos
            if x > furthestRight:
                furthestRight = x
            if x < furthestLeft:
                furthestLeft = x
            if y > deepest:
                deepest = y
    drawing = []
    for i in range(deepest + 1):
        drawing.append([0] * (furthestRight - furthestLeft + 1))
    for wall in coordinates:
        for i in range(len(wall) - 1):
            x1, y1 = wall[i]
            x2, y2 = wall[i + 1]
            while x1 != x2:
                drawing[y1][x1 - furthestLeft] = 1
                x1 = x1 - 1 if x1 > x2 else x1 + 1
            while y1 != y2:
                drawing[y1][x1 - furthestLeft] = 1
                y1 = y1 - 1 if y1 > y2 else y1 + 1

    return drawing, furthestLeft


def first_star(coordinates):
    """
    Sand: Down, down-left, down-right
    """
    drawing, furthestLeft = draw_walls(coordinates)
    sandxStart, sandyStart = 500 - furthestLeft, 0
    sandx, sandy = sandxStart, sandyStart
    drawing[sandy][sandx] = 2
    sandIsFalling = False
    while not sandIsFalling:
        sandy += 1
        while drawing[sandy][sandx] not in (1, 2):
            sandy += 1
        if drawing[sandy][sandx] == 1:
            drawing[sandy - 1][sandx] = 2
        elif drawing[sandy][sandx] == 2:
            if drawing[sandy][sandx - 1] not in (1, 2):
                drawing[sandy][sandx - 1] = 2
            elif drawing[sandy][sandx + 1] not in (1, 2):
                drawing[sandy][sandx + 1] = 2
            else:
                drawing[sandy-1][sandx] = 2
        sandx, sandy = sandxStart, sandyStart
    return drawing[0]


if __name__ == "__main__":
    problem = get_input("test.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
