def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    newLines = set()
    for line in lines:
        x, y, z = line.split(",")
        newLines.add((int(x), int(y), int(z)))
    return newLines


def second_star(coordinates):
    return


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
