import re


def get_input(file):
    return [line.split(" ") for line in open(file).read().splitlines()]


def second_star(commands):
    return


def first_star(commands):
    maxSize = 100000
    totalSize = 0
    directories = []
    currentDirectory = ""
    currentSize = 0
    stack = []
    for command in commands:
        if command[1] == "cd":
            if command[2] == "..":
                if currentSize < maxSize:
                    totalSize += currentSize
                d, s = stack.pop()
                currentSize += s
            else:
                stack.append((currentDirectory, currentSize))
                currentDirectory = command[2]
                currentSize = 0
            continue

        match = re.search(r"(^\d+) (.*)", " ".join(command))
        if match:
            currentSize += int(match.group(1))
    return totalSize


if __name__ == "__main__":
    problem = get_input('test.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
