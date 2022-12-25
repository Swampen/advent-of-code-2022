import copy


def get_input(file):
    lines = [list(line) for line in open(file).read().splitlines()]
    start = (lines[0].index("."), 0)
    end = (lines[-1].index("."), len(lines) - 1)
    d = {}
    right, down, left, up = [], [], [], []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            match lines[y][x]:
                case ">":
                    right.append((x, y))
                case "v":
                    down.append((x, y))
                case "<":
                    left.append((x, y))
                case "^":
                    up.append((x, y))
    d["start"] = start
    d["end"] = end
    d["width"] = len(lines[0])
    d["height"] = len(lines)
    d["right"] = right
    d["down"] = down
    d["left"] = left
    d["up"] = up
    return d


def second_star(positions):
    return

def first_star(positions):
    start = positions["start"]
    currentPositions = [start]
    end = positions["end"]
    width = positions["width"]
    height = positions["height"]
    right = positions["right"]
    down = positions["down"]
    left = positions["left"]
    up = positions["up"]
    minutes = 0
    while True:
        nextBlizzards = set()
        nextRight = []
        nextUp = []
        nextLeft = []
        nextDown = []
        for pos in right:
            if pos[0] + 1 == width - 1:
                nextRight.append((1, pos[1]))
            else:
                nextRight.append((pos[0] + 1, pos[1]))
        for pos in down:
            if pos[1] + 1 == height - 1:
                nextDown.append((pos[0], 1))
            else:
                nextDown.append((pos[0], pos[1] + 1))
        for pos in left:
            if pos[0] - 1 == 0:
                nextLeft.append((width - 2, pos[1]))
            else:
                nextLeft.append((pos[0] - 1, pos[1]))
        for pos in up:
            if pos[1] - 1 == 0:
                nextUp.append((pos[0], height - 2))
            else:
                nextUp.append((pos[0], pos[1] - 1))
        nextBlizzards.update(nextRight)
        nextBlizzards.update(nextDown)
        nextBlizzards.update(nextLeft)
        nextBlizzards.update(nextUp)

        nextPositions = [start]
        for pos in currentPositions:
            r = (pos[0] + 1, pos[1])
            d = (pos[0], pos[1] + 1)
            l = (pos[0] - 1, pos[1])
            u = (pos[0], pos[1] - 1)
            if canMove(pos, nextBlizzards, nextPositions, width, height, end):
                nextPositions.append(pos)
            if canMove(r, nextBlizzards, nextPositions, width, height, end):
                nextPositions.append(r)
            if canMove(d, nextBlizzards, nextPositions, width, height, end):
                nextPositions.append(d)
            if canMove(l, nextBlizzards, nextPositions, width, height, end):
                nextPositions.append(l)
            if canMove(u, nextBlizzards, nextPositions, width, height, end):
                nextPositions.append(u)
        minutes += 1
        # print(minutes)
        # for y in range(height):
        #     for x in range(width):
        #         pos = (x, y)
        #         if pos in nextPositions:
        #             print("E", end="")
        #         elif pos in nextRight:
        #             print(">", end="")
        #         elif pos in nextDown:
        #             print("v", end="")
        #         elif pos in nextLeft:
        #             print("<", end="")
        #         elif pos in nextUp:
        #             print("^", end="")
        #         else:
        #             print(".", end="")
        #     print("")
        if end in nextPositions:
            break
        right = copy.deepcopy(nextRight)
        down = copy.deepcopy(nextDown)
        left = copy.deepcopy(nextLeft)
        up = copy.deepcopy(nextUp)
        currentPositions = copy.deepcopy(nextPositions)

    return minutes


def canMove(position, blizzards, newPositions, width, height, end):
    if position == end:
        return True
    if position in newPositions:
        return False
    elif position[0] < 1 or position[0] >= width - 1:
        return False
    elif position[1] < 1 or position[1] >= height - 1:
        return False
    elif position not in blizzards:
        return True
    else:
        return False


if __name__ == "__main__":
    problem = get_input("test.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
