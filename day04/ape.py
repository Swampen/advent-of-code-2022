from typing import List, Tuple


def get_input(file):
    lines = [line.split(",") for line in open(file).read().splitlines()]
    return [(format_range(line[0].split("-")), format_range(line[1].split("-"))) for line in lines]


def format_range(strings):
    return [int(strings[0]), int(strings[1])]


def second_star(pairs: List[Tuple[List[int], List[int]]]):
    doOverlap = 0
    for first, second in pairs:
        firstStartOverlap = first[0] - second[1]
        firstEndOverlap = first[1] - second[0]
        if firstStartOverlap <= 0 <= firstEndOverlap:
            doOverlap += 1

    return doOverlap


def first_star(pairs: List[Tuple[List[int], List[int]]]):
    fullOverlaps = 0
    for first, second in pairs:
        startCompare = first[0] - second[0]
        endCompare = first[1] - second[1]
        if startCompare >= 0 >= endCompare or startCompare <= 0 <= endCompare:
            fullOverlaps += 1

    return fullOverlaps


if __name__ == "__main__":
    problem = get_input('input.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
