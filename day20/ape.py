import copy
from utils.CircularLinkedList.CircularLinkedList import CircularLinkedList, Node


def get_input(file):
    return CircularLinkedList([(i, int(line)) for i, line in enumerate(open(file).read().splitlines())])


def second_star(sequence):
    return


def first_star(sequence):
    sum = 0
    i = 0
    currentIndex = 0
    while currentIndex != len(sequence):
        index = 0
        for node in sequence:
            if node.data[0] == currentIndex:
                sequence.remove(index)
                sequence.insert(node.data, (index+node.data[1]) % len(sequence))
                currentIndex += 1
                break
            index += 1
    i = 0
    node = sequence.head
    while node.data[1] != 0:
        node = node.next
    while i <= 3000:
        if i in [1000, 2000, 3000]:
            sum += node.data[1]
        node = node.next
        i += 1
    return sum


if __name__ == "__main__":
    problem = get_input("input.txt")
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
