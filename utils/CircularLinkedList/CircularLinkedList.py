class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.previous: Node | None = None

    def __repr__(self):
        return str(self.data)


class CircularLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.count = 0
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.count = 1
            previous = node
            for elem in nodes:
                if self.head == node:
                    node.previous = None
                else:
                    node.previous = previous
                node.next = Node(data=elem)
                previous = node
                node = node.next
                self.count += 1
            node.previous = previous
            node.next = self.head
            self.head.previous = node

    def __len__(self):
        return self.count

    def __iter__(self):
        starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def __repr__(self):
        starting_point = self.head
        node = starting_point
        nodes = []
        while node is not None and (node.next != starting_point):
            nodes.append(node)
            node = node.next
        nodes.append(node)
        nodes.append("Head")
        return " -> ".join(map(str, nodes))

    def add_first(self, node):
        node.next = self.head
        node.previous = self.head.previous
        self.head.previous = node
        self.head = node
        self.count += 1

    def move_node(self, node: Node, spaces: int):
        if spaces == 0:
            return node
        elif spaces > 0:
            if node == self.head:
                self.head = node.next
            node.previous.next = node.next
            node.next.previous = node.previous
            current = node.next
            for i in range(spaces - 1):
                current = current.next
            node.next = current.next
            node.previous = current
            current.next.previous = node
            current.next = node
        elif spaces < 0:
            if node == self.head:
                self.head = node.next
            node.previous.next = node.next
            node.next.previous = node.previous
            current = node.previous
            for i in range(abs(spaces) - 1):
                current = current.previous
            node.next = current
            node.previous = current.previous
            current.previous.next = node
            current.previous = node

        return node

    def add_before(self, target_node_data, new_node):
        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

    def remove_node(self, target_node_data):
        if self.head.data == target_node_data:
            node = self.head
            self.head.next.previous = node.previous
            self.head.previous.next = node.next
            self.head = node.next
            return node
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                node.next.previous = node.previous
                previous_node.next = node.next
                return node
            previous_node = node

    def insert(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        if self.head is None:
            self.head = Node(data)
            self.count = 1
            return

        temp = self.head
        if index == 0:
            temp = temp.previous
        else:
            for _ in range(index - 1):
                temp = temp.next

        temp.next.previous = Node(data)
        temp.next.previous.next, temp.next.previous.previous = temp.next, temp
        temp.next = temp.next.previous
        if index == 0:
            self.head = self.head.previous
        self.count += 1
        return

    def remove(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        if self.count == 1:
            self.head = None
            self.count = 0
            return

        target = self.head
        for _ in range(index):
            target = target.next

        if target is self.head:
            self.head = self.head.next

        target.previous.next, target.next.previous = target.next, target.previous
        self.count -= 1
