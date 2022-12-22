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


def second_star(dictionary):
    return


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
