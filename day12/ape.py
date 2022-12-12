def get_input(file):
    return [[ord(letter) - 96 for letter in list(line)] for line in open(file).read().splitlines()]


def second_star(elevation):
    return


def make_step(k, m, e):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                current = e[i][j]
                if i > 0 and m[i - 1][j] == 0 and \
                        e[i - 1][j] - current <= 1:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and \
                        e[i][j - 1] - current <= 1:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and \
                        e[i + 1][j] - current <= 1:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and \
                        e[i][j + 1] - current <= 1:
                    m[i][j + 1] = k + 1


def first_star(elevation):
    start = (0, 0)
    end = (0, 0)
    for i, row in enumerate(elevation):
        for j, column in enumerate(row):
            if chr(column + 96) == "S":
                elevation[i][j] = 1
                start = (i, j)
            if chr(column + 96) == "E":
                elevation[i][j] = ord("z") + 1 - 96
                end = (i, j)
    m = []
    for i in range(len(elevation)):
        m.append([])
        for j in range(len(elevation[i])):
            m[-1].append(0)
    m[start[0]][start[1]] = 1
    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k, m, elevation)
    print(k)
    i, j = end
    k = m[i][j]
    path = [(i, j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k - 1:
            i, j = i - 1, j
            path.append((i, j))
            k -= 1
        elif j > 0 and m[i][j - 1] == k - 1:
            i, j = i, j - 1
            path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and m[i + 1][j] == k - 1:
            i, j = i + 1, j
            path.append((i, j))
            k -= 1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
            i, j = i, j + 1
            path.append((i, j))
            k -= 1
    return len(path) - 1


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
