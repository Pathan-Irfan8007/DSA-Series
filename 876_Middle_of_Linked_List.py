'''
Q. Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

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

    def position(self, index):
        count = 0
        current = self.head
        while count < index:
            count += 1
            current = current.next
        print(current.val)

    def middle(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(count)
        mid = count // 2
        
        self.position(mid)

# ------ Floyd's Tortoise - Hare Algorithm ------
    def middle2(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)


sll = SinglyLinkedList()

# sll.insert(0)
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.insert(6)
sll.insert(7)
# sll.insert(8)
sll.traverse()

# sll.delete_index(1)
# sll.delete_val(0)
# sll.traverse()

sll.middle2()