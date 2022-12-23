import copy
import re


def get_input(file):
    lines = [list(line) for line in open(file).read().splitlines()]
    positions = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                positions.add((x, y))
    return positions


def second_star(positions):
    return


def visualize(positions: set):
    max_x = max(positions, key=lambda item: item[0])[0]
    min_x = min(positions, key=lambda item: item[0])[0]
    max_y = max(positions, key=lambda item: item[1])[1]
    min_y = min(positions, key=lambda item: item[1])[1]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()


def first_star(positions):
    nOrder = 0
    sOrder = 1
    wOrder = 2
    eOrder = 3
    for j in range(10):
        currentPos = []
        newPos = []
        dupList = []
        for x, y in positions:
            n = {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)}
            s = {(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}
            w = {(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)}
            e = {(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)}
            directions = [("n", n, nOrder), ("s", s, sOrder), ("w", w, wOrder), ("e", e, eOrder)]
            directions.sort(key=lambda item: item[2])
            surroundings = n | s | w | e
            # No other elf around
            pos = (x, y)
            currentPos.append(pos)
            if not surroundings & positions:
                newPos.append(pos)
                continue
            for d, s, _ in directions:
                if not s & positions:
                    match d:
                        case "n":
                            pos = (x, y - 1)
                            break
                        case "s":
                            pos = (x, y + 1)
                            break
                        case "w":
                            pos = (x - 1, y)
                            break
                        case "e":
                            pos = (x + 1, y)
                            break

            if pos in newPos:
                dupList.append(pos)
            newPos.append(pos)
        for i, pos in enumerate(newPos):
            if pos in dupList:
                newPos[i] = currentPos[i]
        positions = set(newPos)
        nOrder = (nOrder - 1) % 4
        sOrder = (sOrder - 1) % 4
        wOrder = (wOrder - 1) % 4
        eOrder = (eOrder - 1) % 4

    max_x = max(positions, key=lambda item: item[0])[0]
    min_x = min(positions, key=lambda item: item[0])[0]
    max_y = max(positions, key=lambda item: item[1])[1]
    min_y = min(positions, key=lambda item: item[1])[1]
    return (max_x + 1 - min_x) * (max_y + 1 - min_y) - len(positions)


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
