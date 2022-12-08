import re


def get_input(file):
    return [list(line) for line in open(file).read().splitlines()]


def second_star(trees):
    highest = 0
    for row in range(1, len(trees) - 1):
        for column in range(1, len(trees[row]) - 1):
            treeScenicScore = calculate_scenic_score(row, column, trees)
            if treeScenicScore > highest:
                highest = treeScenicScore
    return highest


def calculate_scenic_score(row, column, trees):
    tree = trees[row][column]
    i = row - 1
    uscore = 0
    # Up
    while i >= 0:
        uscore += 1
        if tree <= trees[i][column]:
            break
        i -= 1

    i = row + 1
    dscore = 0
    # Down
    while i < len(trees):
        dscore += 1
        if tree <= trees[i][column]:
            break
        i += 1

    i = column - 1
    lscore = 0
    # Left
    while i >= 0:
        lscore += 1
        if tree <= trees[row][i]:
            break
        i -= 1

    i = column + 1
    rscore = 0
    # Right
    while i < len(trees[row]):
        rscore += 1
        if tree <= trees[row][i]:
            break
        i += 1
    return uscore * dscore * lscore * rscore


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
