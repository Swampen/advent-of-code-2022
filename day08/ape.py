import re


def get_input(file):
    return [list(line) for line in open(file).read().splitlines()]


def second_star(trees):
    return


def is_visible_from_edge(row, column, trees):
    tree = trees[row][column]
    i = row - 1
    visible = True
    # Up
    while i >= 0:
        if tree <= trees[i][column]:
            visible = False
            break
        i -= 1
    if visible:
        return True

    i = row + 1
    visible = True
    # Down
    while i < len(trees):
        if tree <= trees[i][column]:
            visible = False
            break
        i += 1
    if visible:
        return True

    i = column - 1
    visible = True
    # Left
    while i >= 0:
        if tree <= trees[row][i]:
            visible = False
            break
        i -= 1
    if visible:
        return True

    i = column + 1
    visible = True
    # Right
    while i < len(trees[row]):
        cTree = trees[row][i]
        if tree <= trees[row][i]:
            visible = False
            break
        i += 1
    return visible


def first_star(trees):
    count = len(trees) * 2 + len(trees[0][1:-1]) * 2
    for row in range(1, len(trees) - 1):
        for column in range(1, len(trees[row]) - 1):
            count += 1 if is_visible_from_edge(row, column, trees) else 0

    return count


if __name__ == "__main__":
    problem = get_input('input.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
