import math


def get_input(file):
    return [line for line in open(file).read().splitlines()]


def second_star(snafus):
    return


def first_star(snafus):
    total = 0
    for snafu in snafus:
        total += from_snafu(snafu)
    return to_snafu(total)


def to_snafu(number: int):
    snafu = ""
    while number > 0:
        number, reminder = divmod(number, 5)
        if reminder in [0, 1, 2]:
            snafu = f"{reminder}{snafu}"
        elif reminder == 3:
            number += 1
            snafu = f"={snafu}"
        elif reminder == 4:
            number += 1
            snafu = f"-{snafu}"
    return snafu


def from_snafu(snafu):
    total = 0
    for i, c in enumerate(snafu):
        power = len(snafu) - 1 - i
        if c == "2":
            total += int(math.pow(5, power) * 2)
        elif c == "1":
            total += int(math.pow(5, power))
        elif c == "-":
            total += int(math.pow(5, power) * -1)
        elif c == "=":
            total += int(math.pow(5, power) * -2)
        elif c == "0":
            continue
    return total


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
