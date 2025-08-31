# Remove loop
# https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectAndRemoveLoop(head):
    """Detect and remove loop if present. Returns True if handled successfully."""
    if not head or not head.next:
        return True 

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return True 

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    ptr = slow
    while ptr.next != slow:
        ptr = ptr.next
    ptr.next = None

    return True


def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head


def createLoop(head, pos):
    if pos == 0:
        return
    loop_node = head
    for _ in range(1, pos):
        loop_node = loop_node.next
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = loop_node

head1 = createLinkedList([1, 3, 4])
createLoop(head1, 2)
print(detectAndRemoveLoop(head1))  
head2 = createLinkedList([1, 8, 3, 4])
createLoop(head2, 0)
print(detectAndRemoveLoop(head2))  

head3 = createLinkedList([1, 2, 3, 4])
createLoop(head3, 1)
print(detectAndRemoveLoop(head3))  
