def get_input(file):
    return [line.split(" ") for line in open(file).read().splitlines()]


def second_star(operations):
    return


def first_star(operations):
    registerValue = 1
    cycle = 0
    s = {}
    for opt in operations:
        cycle += 1
        s[cycle] = registerValue
        if opt[0] == "noop":
            continue
        cycle += 1
        s[cycle] = registerValue
        registerValue += int(opt[1])
    sum = s[20] * 20
    sum += s[60] * 60
    sum += s[100] * 100
    sum += s[140] * 140
    sum += s[180] * 180
    sum += s[220] * 220
    return sum


if __name__ == "__main__":
    problem = get_input('test.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
