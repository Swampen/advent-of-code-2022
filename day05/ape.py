import copy


def get_input(file):
    return [line.split(" ") for line in open(file).read().splitlines()]


def second_star():
    return


def first_star(lines):
    splitIndex = lines.index([""])
    stacks = lines[:splitIndex]
    instructions = lines[splitIndex + 1:]
    for inst in instructions:
        amount = int(inst[1])
        i = int(inst[3]) - 1
        j = int(inst[5]) - 1
        fromStack = stacks[i]
        toStack = stacks[j]

        for k in range(amount):
            toStack.append(fromStack.pop())
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    problem = get_input('test.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star())
