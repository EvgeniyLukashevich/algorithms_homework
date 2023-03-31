# Реализовать метод разворота связного списка (двухсвязного или односвязного на выбор)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_first(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print(self):
        curr_node = self.head
        string = ""
        while curr_node:
            string = string + " " + str(curr_node.data)
            curr_node = curr_node.next
        print(string)


my_list = LinkedList()
my_list.add_first(5)
my_list.add_first(4)
my_list.add_first(33)
my_list.add_first(2)
my_list.add_first(1)
my_list.print()

my_list.reverse()
my_list.print()
