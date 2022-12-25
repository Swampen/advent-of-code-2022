import re


def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    d = {}
    for line in lines:
        number, oreOreCost, clayOreCost, obsidianOreCost, obsidianClayCost, geodeOreCost, geodeObsidianCost = \
            map(int, re.findall(r"(\d+)", line))
        d[number] = {
            "oreRobot": oreOreCost,
            "clayRobot": clayOreCost,
            "obsidianRobot": (obsidianOreCost, obsidianClayCost),
            "geodeRobot": (geodeOreCost, geodeObsidianCost)
        }
    return d


def second_star(blueprints):
    return


def first_star(blueprints):
    total = 0
    for number, blueprint in blueprints.items():
        oreCount, clayCount, obsidianCount, geodeCount = 0, 0, 0, 0
        oreProducers, clayProducers, obsidianProducers, geodeProducers = 1, 0, 0, 0
        oreMax = max(blueprint["oreRobot"], blueprint["clayRobot"], blueprint["obsidianRobot"][0],
                     blueprint["geodeRobot"][0])
        clayMax = blueprint["obsidianRobot"][1]
        obsidianMax = blueprint["geodeRobot"][1]
        for _ in range(24):
            isOreRobotCreated, isClayRobotCreated, isObsidianRobotCreated, isGeodeRobotCreated = \
                [False for _ in range(4)]
            # Geode
            if oreCount >= blueprint["geodeRobot"][0] and obsidianCount >= blueprint["geodeRobot"][1]:
                isGeodeRobotCreated = True
                oreCount -= blueprint["geodeRobot"][0]
                obsidianCount += blueprint["geodeRobot"][1]
            # Obsidian
            elif oreCount >= blueprint["obsidianRobot"][0] and clayCount >= blueprint["obsidianRobot"][1] and \
                    obsidianProducers <= obsidianMax:
                isObsidianRobotCreated = True
                oreCount -= blueprint["obsidianRobot"][0]
                clayCount += blueprint["obsidianRobot"][1]
            # Clay
            elif oreCount >= blueprint["clayRobot"] and clayProducers <= clayMax:
                isClayRobotCreated = True
                oreCount -= blueprint["clayRobot"]
            # Ore
            elif oreCount >= blueprint["oreRobot"] and oreProducers <= oreMax:
                isOreRobotCreated = True
                oreCount -= blueprint["oreRobot"]
            oreCount += oreProducers
            clayCount += clayProducers
            obsidianCount += obsidianProducers
            geodeCount += geodeProducers
            if isGeodeRobotCreated:
                geodeProducers += 1
            if isObsidianRobotCreated:
                obsidianProducers += 1
            if isClayRobotCreated:
                clayProducers += 1
            if isOreRobotCreated:
                isOreRobotCreated += 1

        print(geodeCount * number)
        total += geodeCount * number
    return total


if __name__ == "__main__":
    problem = get_input("test.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
