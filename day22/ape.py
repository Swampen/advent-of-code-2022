import copy
import re


def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    l = []
    d = {}
    for i in range(len(lines)):
        if lines[i] == "":
            steps = [int(step) for step in re.split(r"[RL]", lines[i + 1])]
            t = re.split(r"\d+", lines[i + 1])
            d["steps"] = steps
            d["dir"] = t
            break
        l.append(lines[i])
    longest = 0
    for line in l:
        if len(line) > longest:
            longest = len(line)
    for i, line in enumerate(l):
        if len(line) != longest:
            l[i] = line + " " * (longest - len(line))
    d["map"] = l
    return d


def get_next(x, y, direction, size):
    # 1
    if size * 2 <= x < size * 3 and y < size:
        match direction:
            case 0:
                x = size * 2 - 1
                y = size * 3 - 1 - (y % size)
                return x, y, 2
            case 1:
                y = size + (x % size)
                x = size * 2 - 1
                return x, y, 2
            case 3:
                y = size * 4 - 1
                x = x % size
                return x, y, 3
            case _:
                raise Exception("Not correct direction")
    # 2
    elif size <= x < size * 2 and y < size:
        match direction:
            case 2:
                y = size * 3 - 1 - (y % size)
                x = 0
                return x, y, 0
            case 3:
                y = size * 3 + (x % size)
                x = 0
                return x, y, 0
            case _:
                raise Exception("Not correct direction")
    # 3
    elif size <= x < size * 2 and size <= y < size * 2:
        match direction:
            case 0:
                x = size * 2 + (y % size)
                y = size - 1
                return x, y, 3
            case 2:
                x = y % size
                y = size * 2
                return x, y, 1
            case _:
                raise Exception("Not correct direction")
    # 4
    elif size <= x < size * 2 and size * 2 <= y < size * 3:
        match direction:
            case 0:
                y = size - 1 - (y % size)
                x = size * 3 - 1
                return x, y, 2
            case 1:
                y = size * 3 + (x % size)
                x = size - 1
                return x, y, 2
            case _:
                raise Exception("Not correct direction")
    # 5
    elif x < size and size * 2 <= y < size * 3:
        match direction:
            case 2:
                x = size
                y = size - 1 - (y % size)
                return x, y, 0
            case 3:
                y = size + x
                x = size
                return x, y, 0
            case _:
                raise Exception("Not correct direction")
    # 6
    elif x < size and size * 3 <= y < size * 4:
        match direction:
            case 0:
                x = size + (y % size)
                y = size * 3 - 1
                return x, y, 3
            case 1:
                y = 0
                x = size * 2 + x
                return x, y, 1
            case 2:
                x = size + (y % size)
                y = 0
                return x, y, 1
            case _:
                raise Exception("Not correct direction")
    raise Exception("Not inside a face")


def second_star(dictionary, size=50):
    currentDirection = 0
    x, y = 0, 0
    m = dictionary["map"]
    for i, col in enumerate(m[0]):
        if col == ".":
            x = i
            break
    for i, steps in enumerate(dictionary["steps"]):
        currentDirection = turn(currentDirection, dictionary["dir"][i])
        currentSteps = 0
        while currentSteps != steps:
            # Right
            if currentDirection == 0:
                nextStep = x + 1
                if nextStep < len(m[y]) and m[y][nextStep] == "#":
                    break
                elif nextStep < len(m[y]) and m[y][nextStep] == ".":
                    x = nextStep
                    currentSteps += 1
                else:
                    tempx, tempy, tempDirection = get_next(x, y, currentDirection, size)
                    if m[tempy][tempx] == "#":
                        break
                    else:
                        x, y, currentDirection = tempx, tempy, tempDirection
                        currentSteps += 1
            # Left
            elif currentDirection == 2:
                nextStep = x - 1
                if nextStep >= 0 and m[y][nextStep] == "#":
                    break
                elif nextStep >= 0 and m[y][nextStep] == ".":
                    x = nextStep
                    currentSteps += 1
                else:
                    tempx, tempy, tempDirection = get_next(x, y, currentDirection, size)
                    if m[tempy][tempx] == "#":
                        break
                    else:
                        x, y, currentDirection = tempx, tempy, tempDirection
                        currentSteps += 1
            # Down
            elif currentDirection == 1:
                nextStep = y + 1
                if nextStep < len(m) and m[nextStep][x] == "#":
                    break
                elif nextStep < len(m) and m[nextStep][x] == ".":
                    y = nextStep
                    currentSteps += 1
                else:
                    tempx, tempy, tempDirection = get_next(x, y, currentDirection, size)
                    if m[tempy][tempx] == "#":
                        break
                    else:
                        x, y, currentDirection = tempx, tempy, tempDirection
                        currentSteps += 1
            # Up
            elif currentDirection == 3:
                nextStep = y - 1
                if nextStep >= 0 and m[nextStep][x] == "#":
                    break
                elif nextStep >= 0 and m[nextStep][x] == ".":
                    y = nextStep
                    currentSteps += 1
                else:
                    tempx, tempy, tempDirection = get_next(x, y, currentDirection, size)
                    if m[tempy][tempx] == "#":
                        break
                    else:
                        x, y, currentDirection = tempx, tempy, tempDirection
                        currentSteps += 1

    return 1000 * (y + 1) + 4 * (x + 1) + currentDirection


def turn(currentDirection, direction):
    if direction == "L":
        return (currentDirection - 1) % 4
    if direction == "R":
        return (currentDirection + 1) % 4
    return currentDirection


def first_star(dictionary):
    currentDirection = 0
    x, y = 0, 0
    m = dictionary["map"]
    for i, col in enumerate(m[0]):
        if col == ".":
            x = i
            break
    for i, steps in enumerate(dictionary["steps"]):
        currentDirection = turn(currentDirection, dictionary["dir"][i])
        currentSteps = 0
        while currentSteps != steps:
            # Right
            if currentDirection == 0:
                nextStep = (x + 1) % len(m[y])
                if m[y][nextStep] == "#":
                    break
                elif m[y][nextStep] == ".":
                    x = nextStep
                    currentSteps += 1
                else:
                    temp = nextStep
                    while m[y][temp] == " ":
                        temp = (temp + 1) % len(m[y])
                    if m[y][temp] == "#":
                        break
                    else:
                        x = temp
                        currentSteps += 1
            # Left
            elif currentDirection == 2:
                nextStep = (x - 1) % len(m[y])
                if m[y][nextStep] == "#":
                    break
                elif m[y][nextStep] == ".":
                    x = nextStep
                    currentSteps += 1
                else:
                    temp = nextStep
                    while m[y][temp] == " ":
                        temp = (temp - 1) % len(m[y])
                    if m[y][temp] == "#":
                        break
                    else:
                        x = temp
                        currentSteps += 1
            # Down
            elif currentDirection == 1:
                nextStep = (y + 1) % len(m)
                if m[nextStep][x] == "#":
                    break
                elif m[nextStep][x] == ".":
                    y = nextStep
                    currentSteps += 1
                else:
                    temp = nextStep
                    while m[temp][x] == " ":
                        temp = (temp + 1) % len(m)
                    if m[temp][x] == "#":
                        break
                    else:
                        y = temp
                        currentSteps += 1
            # Up
            elif currentDirection == 3:
                nextStep = (y - 1) % len(m)
                if m[nextStep][x] == "#":
                    break
                elif m[nextStep][x] == ".":
                    y = nextStep
                    currentSteps += 1
                else:
                    temp = nextStep
                    while m[temp][x] == " ":
                        temp = (temp - 1) % len(m)
                    if m[temp][x] == "#":
                        break
                    else:
                        y = temp
                        currentSteps += 1

    return 1000 * (y + 1) + 4 * (x + 1) + currentDirection


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
