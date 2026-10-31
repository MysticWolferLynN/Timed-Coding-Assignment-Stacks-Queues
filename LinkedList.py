from Node import Node

class LinkedList:
    def __init__(self):
        self. head = None
        self. tail = None
        self. size = 0

    def is_empty(self):
        return self.head is None

    def is_empty(self):
        return self.head is None
    def __len__(self):
        return self.size

    def enqeue(self, data):
        new_node = None(data)

        if self. is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

            self.size += 1

            def dequeue(self):
                if self.is_empty():
                    return None

                removed_data = self.head.data
                self.head = self.head.next

                self.size -=1

                if self.head is None:
                    self.tail = None

                return removed_data

            def push(self, data):
                new_node = Node(data)

                new_node.next = self.head
                self.head = new_node

                if self.tail is None:
                    self.tail = new_node

                    self.size +=1

                def pop(self):
                    return self.dequeue()

                def peek(self):
                    if self.is_empty():
                        return None

                    return self.head.data

                def display(self):
                    items = []
                    current = self.head

                    while current is not None:
                        items.append(current.data)
                        current = current.next

                    return items