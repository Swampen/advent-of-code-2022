import json
import copy


def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    l = []
    for line in lines:
        if line == "":
            continue
        l.append(json.loads(line))
    return l


def second_star(signal):
    return


def first_star(signal):
    for i in range(0, len(signal), 2):
        left = []
        right = []
        left.append(signal[i])
        right.append(signal[i + 1])
        while len(left) != 0:
            l = left.pop()
            r = right.pop()
            for j in range(len(l)):
                if j >= len(r):
                    break
                if isinstance(l[j], list) or isinstance(r[j], list):
                    if not isinstance(l[j], list):
                        l[j] = [l[j]]
                    if not isinstance(r[j], list):
                        r[j] = [r[j]]
                    right.append(r[j])
                    left.append(l[j])
    matching = []
    currentIndex = 0
    for i in range(0, len(signal), 2):
        currentIndex += 1
        if signal[i] < signal[i + 1]:
            matching.append(currentIndex)

    return sum(matching)


if __name__ == "__main__":
    problem = get_input("test.txt")
    print("First star:", first_star(copy.deepcopy(problem)))
    print("Second star:", second_star(problem))
