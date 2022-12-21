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
    number = 0
    for i in range(3093175982400, 100000000000000, 1):
        dictionary_copy = copy.deepcopy(dictionary)
        dictionary_copy["humn"] = i
        get_number(dictionary_copy, "root")
        print(dictionary_copy["root"], i)
        if dictionary_copy["root"][0] == dictionary_copy["root"][2]:
            number = i
            break


    return number


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
    problem = get_input("input.txt")
    print("First star:", first_star(copy.deepcopy(problem)))
    print("Second star:", second_star(problem))
