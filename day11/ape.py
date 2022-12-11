import math
import copy


def get_input(file):
    lines = [line.strip() for line in open(file).read().splitlines()]
    monkeys = {}
    currentMonkey = 0
    currentData = {}
    for i, line in enumerate(lines):
        if i % 7 == 0:
            currentData["count"] = 0
        elif i % 7 == 1:
            currentData["items"] = [int(num) for num in line.split(": ")[-1].split(", ")]
        elif i % 7 == 2:
            currentData["operation"] = line.split("= ")[-1]
        elif i % 7 == 3:
            currentData["test"] = int(line.split(" ")[-1])
        elif i % 7 == 4:
            currentData["true"] = int(line.split(" ")[-1])
        elif i % 7 == 5:
            currentData["false"] = int(line.split(" ")[-1])
            monkeys[currentMonkey] = currentData.copy()
            currentMonkey += 1
    return monkeys


def second_star(monkeys):
    currentRound = 1
    breakRound = 10000
    divs = []
    for data in monkeys.values():
        divs.append(data["test"])
    lcm = math.lcm(*divs)
    while True:
        for data in monkeys.values():
            if len(data["items"]) == 0:
                continue
            for item in data["items"]:
                data["count"] += 1
                worryLevel = eval(data["operation"].replace("old", f"{item}"))
                # modify
                worryLevel = worryLevel % lcm
                if worryLevel % data["test"] == 0:
                    monkeys[data["true"]]["items"].append(worryLevel)
                else:
                    monkeys[data["false"]]["items"].append(worryLevel)
            data["items"] = []
        if currentRound == breakRound:
            largest = [0, 0]
            for monkey, data in monkeys.items():
                for i, x in enumerate(largest):
                    if data["count"] > x:
                        largest[i] = data["count"]
                        break
                largest.sort()
            break
        currentRound += 1
    return math.prod(largest)


def first_star(monkeys):
    currentRound = 1
    while True:
        for monkey, data in monkeys.items():
            if len(data["items"]) == 0:
                continue
            for item in data["items"]:
                data["count"] += 1
                worryLevel = eval(data["operation"].replace("old", f"{item}"))
                worryLevel = int(worryLevel / 3)
                if worryLevel % data["test"] == 0:
                    monkeys[data["true"]]["items"].append(worryLevel)
                else:
                    monkeys[data["false"]]["items"].append(worryLevel)
            data["items"] = []
        if currentRound == 20:
            largest = [0, 0]
            for monkey, data in monkeys.items():
                for i, x in enumerate(largest):
                    if data["count"] > x:
                        largest[i] = data["count"]
                        break
                largest.sort()
            break
        currentRound += 1
    return math.prod(largest)


if __name__ == "__main__":
    problem = get_input("input.txt")
    problem2 = copy.deepcopy(problem)
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem2))
