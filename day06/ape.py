def get_input(file):
    return open(file).read()


def second_star(sequence):
    start = 0
    size = 14
    for i, char in enumerate(sequence):
        subset = set(sequence[i:i + size])
        if len(subset) == size:
            start = i + size
            break
    return start


def first_star(sequence):
    start = 0
    size = 4
    for i, char in enumerate(sequence):
        subset = set(sequence[i:i+size])
        if len(subset) == size:
            start = i+size
            break
    return start


if __name__ == "__main__":
    problem = get_input('input.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
