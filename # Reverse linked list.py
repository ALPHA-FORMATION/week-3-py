# Reverse linked list
# https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedList(head):
    """Reverses the linked list and returns the new head."""
    prev = None
    current = head

    while current:
        next_node = current.next  
        current.next = prev       
        prev = current            
        current = next_node       

    return prev  

def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


head1 = createLinkedList([1, 2, 3, 4])
head1 = reverseLinkedList(head1)
printLinkedList(head1)  

head2 = createLinkedList([2, 7, 10, 9, 8])
head2 = reverseLinkedList(head2)
printLinkedList(head2)  

head3 = createLinkedList([2])
head3 = reverseLinkedList(head3)
printLinkedList(head3)  
