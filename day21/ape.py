import copy


def get_input(file):
    d = {}
    for line in open(file).read().splitlines():
        key, value = line.split(": ")
        values = value.split(" ")
        if len(values) == 1:
            d[key] = int(values[0])
        else:
            d[key] = values
    return d


def second_star(dictionary):
    return


def first_star(dictionary):
    get_number(dictionary, "root")
    return eval("".join(str(x) for x in dictionary["root"]))


def get_number(dictionary, key):
    value = dictionary[key]
    if isinstance(value, int) or isinstance(value, float):
        return value
    else:
        value[0] = get_number(dictionary, value[0])
        value[2] = get_number(dictionary, value[2])
    return eval("".join(str(x) for x in value))


if __name__ == "__main__":
    problem = get_input("test.txt")
    print("First star:", first_star(copy.deepcopy(problem)))
    print("Second star:", second_star(problem))
