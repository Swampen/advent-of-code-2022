import copy
from utils.CircularLinkedList.CircularLinkedList import CircularLinkedList, Node


def get_input(file):
    return [(i, int(line)) for i, line in enumerate(open(file).read().splitlines())]


def second_star(sequence):
    decryptionKey = 811589153
    for node in sequence:
        node.data = (node.data[0], node.data[1] * decryptionKey)
    return first_star(sequence, 10)


def first_star(sequence, rounds=1):
    sum = 0
    i = 0
    while i != rounds:
        currentIndex = 0
        while currentIndex != len(sequence):
            index = 0
            for node in sequence:
                if node.data[0] == currentIndex:
                    sequence.remove(index)
                    sequence.insert(node.data, (index + node.data[1]) % len(sequence))
                    currentIndex += 1
                    break
                index += 1
        i += 1
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
    print("First star:", first_star(CircularLinkedList(copy.deepcopy(problem))))
    print("Second star:", second_star(CircularLinkedList(problem)))
