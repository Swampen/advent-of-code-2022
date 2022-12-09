def get_input(file):
    return [line.split(" ") for line in open(file).read().splitlines()]


def second_star(moves):
    return


def first_star(moves):
    tailMoves = 1
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
