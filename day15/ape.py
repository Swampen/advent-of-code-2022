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
    return


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
        for j in range(a, b+1):
            notBeacon.add(j)

    return len(notBeacon - notPossible)


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
