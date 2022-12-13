import json
import copy
import functools


def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    l = []
    for line in lines:
        if line == "":
            continue
        l.append(json.loads(line))
    return l

def second_star(signal):
    signal.append([[2]])
    signal.append([[6]])
    sorted_l = sorted(signal, key=functools.cmp_to_key(compare_lines))
    first = 0
    second = 0
    for i, l in enumerate(sorted_l):
        if len(l) == 1 and isinstance(l, list):
            t = l
            while not isinstance(t, int) and len(t) == 1:
                t = t[0]
            if t == 2:
                first = i+1
            elif t == 6:
                second = i+1

    return first * second


def compare_lines(line1, line2):
    make_lines_equal(line1, line2)
    if line1 == line2:
        return -1
    if line1 > line2:
        return 1
    else:
        return -1


def make_lines_equal(line1, line2):
    left = []
    right = []
    left.append(line1)
    right.append(line2)
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


def first_star(signal):
    for i in range(0, len(signal), 2):
        make_lines_equal(signal[i], signal[i + 1])

    matching = []
    currentIndex = 0
    for i in range(0, len(signal), 2):
        currentIndex += 1
        if signal[i] < signal[i + 1]:
            matching.append(currentIndex)

    return sum(matching)


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(copy.deepcopy(problem)))
    print("Second star:", second_star(problem))
