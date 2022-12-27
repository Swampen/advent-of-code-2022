import re


def get_input(file):
    lines = [line for line in open(file).read().splitlines()]
    sensors = []
    beacons = []
    for line in lines:
        x = list(map(int, re.findall(r"x=(-?\d+)", line)))
        y = list(map(int, re.findall(r"y=(-?\d+)", line)))
        sensors.append((x[0], y[0]))
        beacons.append((x[1], y[1]))

    return {"beacons": beacons, "sensors": sensors}


def second_star(coordinates):
    sensors = coordinates["sensors"]
    beacons = coordinates["beacons"]
    maxY = 4000000
    pos = (0, 0)
    for y in range(maxY + 1):
        ranges = []
        for i in range(len(beacons)):
            b = beacons[i]
            s = sensors[i]
            length = abs(b[0] - s[0]) + abs(b[1] - s[1])
            offset = length - abs(s[1] - y)
            if offset < 0:
                continue

            a = s[0] - offset
            b = s[0] + offset

            ranges.append((a, b))
        ranges.sort()

        rowRanges = []
        for x1, x2 in ranges:
            if len(rowRanges) == 0:
                rowRanges.append([x1, x2])
            elif x1 > rowRanges[-1][1] + 1:
                rowRanges.append([x1, x2])
            elif x2 > rowRanges[-1][1]:
                rowRanges[-1][1] = x2
        if len(rowRanges) > 1:
            pos = (rowRanges[-1][0] - 1, y)
            break

    return 4000000 * pos[0] + pos[1]


def first_star(coordinates):
    sensors = coordinates["sensors"]
    beacons = coordinates["beacons"]
    checkLine = 2000000
    notBeacon = set()
    notPossible = set()
    for i in range(len(beacons)):
        b = beacons[i]
        s = sensors[i]
        length = abs(b[0] - s[0]) + abs(b[1] - s[1])
        offset = length - abs(s[1] - checkLine)
        if offset < 0:
            continue

        a = s[0] - offset
        b = s[0] + offset

        if b[1] == checkLine:
            notPossible.add(b[0])
        for j in range(a, b + 1):
            notBeacon.add(j)

    return len(notBeacon - notPossible)


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
