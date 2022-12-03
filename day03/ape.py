from typing import List


def get_input(file):
    return [line for line in open(file).read().splitlines()]


def split_string(string):
    return string[:int(len(string) / 2)], string[int(len(string) / 2):]


def second_star():
    return


def first_star(rucksacks: List[str]):
    found = []
    for rucksack in rucksacks:
        first, second = split_string(rucksack)
        for x in second:
            if first.find(x) != -1:
                found.append(x)
                break
    return calculate_score(found)


def calculate_score(score):
    totalScore = 0
    for x in score:
        a = ord(x)
        if a <= 90:
            a -= 38
        else:
            a -= 96
        totalScore += a
    return totalScore


if __name__ == "__main__":
    problem = get_input('input.txt')
    print(problem)
    print("First star:", first_star(problem))
    print("Second star:", second_star())
