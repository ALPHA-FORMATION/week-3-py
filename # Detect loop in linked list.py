# Detect loop in linked list
# https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def hasLoop(head):
    """Detects if the linked list has a loop."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          
        fast = fast.next.next     

        if slow == fast:
            return True
    return False


def createLinkedList(arr):
    """Creates linked list from a Python list."""
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head


def createLoop(head, pos):
    """Creates a loop in the linked list at the given 1-based position."""
    if pos == 0:
        return

    loop_node = head
    for _ in range(1, pos):
        if loop_node:
            loop_node = loop_node.next

    tail = head
    while tail.next:
        tail = tail.next

    tail.next = loop_node  

head1 = createLinkedList([1, 3, 4])
createLoop(head1, 2)
print(hasLoop(head1)) 

head2 = createLinkedList([1, 8, 3, 4])
createLoop(head2, 0)
print(hasLoop(head2))  

head3 = createLinkedList([1, 2, 3, 4])
createLoop(head3, 1)
print(hasLoop(head3)) 
