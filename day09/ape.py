import copy


def get_input(file):
    return [line.split(" ") for line in open(file).read().splitlines()]


def move_knot(this, prev):
    x = this[0] - prev[0]
    y = this[1] - prev[1]
    if abs(x) <= 1 and abs(y) <= 1:
        return prev
    elif abs(x) >= 2 and abs(y) >= 2:
        if prev[0] < this[0]:
            x = this[0] - 1
        else:
            x = this[0] + 1
        if prev[1] < this[1]:
            y = this[1] - 1
        else:
            y = this[1] + 1
        return x, y
    elif abs(x) >= 2:
        if prev[0] < this[0]:
            x = this[0] - 1
        else:
            x = this[0] + 1
        return x, this[1]
    elif abs(y) >= 2:
        if prev[1] < this[1]:
            y = this[1] - 1
        else:
            y = this[1] + 1
        return this[0], y


def second_star(moves):
    ropePos = [(0, 0) for _ in range(9)]
    x, y = 0, 0
    tailPlaces = {(x, y)}
    for move in moves:
        for _ in range(int(move[1])):
            match move[0]:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
            ropePos[0] = move_knot((x, y), ropePos[0])
            for i, knot in enumerate(ropePos):
                if i == 0: continue
                ropePos[i] = move_knot(ropePos[i - 1], knot)
            tailPlaces.add(ropePos[-1])
    return len(tailPlaces)


def first_star(moves):
    tailPos = (0, 0)
    tailPlaces = [tailPos]
    x, y = 0, 0
    for move in moves:
        for i in range(int(move[1])):
            headPreviousPos = (x, y)
            match move[0]:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
            if abs(x - tailPos[0]) > 1 or abs(y - tailPos[1]) > 1:
                tailPos = headPreviousPos
                if tailPos not in tailPlaces:
                    tailPlaces.append(tailPos)
    return len(tailPlaces)


if __name__ == "__main__":
    problem = get_input('input.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
