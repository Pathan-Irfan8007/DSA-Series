'''
Q. Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true

Example 2:
Input: head = [1,2], pos = 0
Output: true

Example 3:
Input: head = [1], pos = -1
Output: false
'''

def isCycle(self):
    add_set = set()

    current = self.head
    while current:
        if current in add_set:
            return True
        add_set.add(current)
        current = current.next
    return False

# ------ Floyd's Tortoise - Hare Algorithm ------
def isCycle2(self):
    slow, fast = self.head, self.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

    