import copy

def get_input(file):
    return [line.split(" ") for line in open(file).read().splitlines()]


def second_star(moves):
    tailPos = (0, 0)
    tailPlaces = [tailPos]
    ropePos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    ropePreviousPos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    x, y = 0, 0
    for move in moves:

        for i in range(int(move[1])):
            print(ropePreviousPos)
            print(ropePos)
            print()
            headPreviousPos = (x, y)
            ropePreviousPos = copy.deepcopy(ropePos)
            match move[0]:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
            ropePos[0] = (x, y)
            for i, knot in enumerate(ropePos):
                if i == 0: continue
                if abs(ropePos[i - 1][0] - knot[0]) > 1 or abs(ropePos[i - 1][1] - knot[1]) > 1:
                    ropePos[i] = ropePreviousPos[i - 1]
                    if i == 9 and knot not in tailPlaces:
                        tailPlaces.append(tailPos)
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
    problem = get_input('test.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
