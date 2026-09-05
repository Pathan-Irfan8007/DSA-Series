'''
Q. Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
# Ans :

def deleteDuplicate(self):
    node_val = set()

    prev = None
    current = self.head
    while current:
        if current.val in node_val:
            prev.next = current.next
        else:
            node_val.add(current.val)
            prev = current
        current = current.next

    return self.head


def deleteDuplicate2(self):
    current = self.head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return self.head