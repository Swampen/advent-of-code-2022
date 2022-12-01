def get_input(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
        return [int(line) if line != "" else "" for line in lines]


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
    ints = get_input('input.txt')
    print("First star:", first_start(ints))
