'''
Q. Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''
# Ans :

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

    def isPalindrome(self):
        normal_list = []

        current = self.head
        while current:
            normal_list.append(current.val)
            current = current.next
        print(normal_list)

        left = 0
        right = len(normal_list) - 1

        while left < right:
            if normal_list[left] != normal_list[right]:
                print(False)
                return
            left += 1
            right -= 1
        print(True)
        return

    def isPalindrome2(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)

        # Reversing second half
        prev = None
        current = slow
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        new_head = prev

        # Again Traversing
        first_half, second_half = self.head, new_head

        while second_half:
            if first_half.val != second_half.val:
                print(False)
                return
            first_half = first_half.next
            second_half = second_half.next
        print(True)


sll = SinglyLinkedList()

sll.insert(0)
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(1)
sll.insert(0)
sll.traverse()

sll.isPalindrome2()