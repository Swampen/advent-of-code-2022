def get_input(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
        return [int(line) if line != "" else "" for line in lines]


def second_start(ints):
    highest = [0, 0, 0]
    totalCalories = 0
    for calories in ints:
        if calories == "":
            for i, x in enumerate(highest):
                if totalCalories > x:
                    highest[i] = totalCalories
                    highest.sort()
                    break
            totalCalories = 0
            continue
        totalCalories += calories
    return sum(highest)


def first_start(ints):
    highest = 0
    totalCalories = 0
    for calories in ints:
        if calories == "":
            if highest < totalCalories:
                highest = totalCalories
            totalCalories = 0
            continue
        totalCalories += calories
    return highest


if __name__ == "__main__":
    lines = get_input('input.txt')
    print("First star:", first_start(lines))
    print("Second star:", second_start(lines))
