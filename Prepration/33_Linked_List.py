class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("Linked List is Empty")
        else:
            current = self.head
            while current:
                print(current.val, end=" => ")
                current = current.next
            print("None")

    def insert_at(self, index, val):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            current = self.head
            count = 0

            while current and count < index:
                prev = current
                current = current.next
                count += 1
            prev.next = new_node
            new_node.next = current

    def delete_index(self, index):
        if index == 0:
            current = self.head
            self.head = current.next
        else:
            prev = None
            current = self.head
            count = 0
            while current and count < index:
                prev = current
                current = current.next
                count += 1

            if current:
                prev.next = current.next
                return current.val
            else:
                print("Index Doesn't Exist")

    def delete_val(self, val):
        prev = None
        current = self.head
        while current:
            if current.val == val:
                if not prev:
                    self.head = current.next
                else:
                    prev.next = current.next
                return current.val
            else:
                prev = current
                current = current.next
        else:
            print("Value Doesn't Exist")


sll = SinglyLinkedList()

sll.insert(0)
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.insert(6)
sll.traverse()

# sll.delete_index(1)
sll.delete_val(0)
sll.traverse()