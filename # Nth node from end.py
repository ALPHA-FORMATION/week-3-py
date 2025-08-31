# Nth node from end
# https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kth_from_end(head, k):
    first = head
    second = head

    for _ in range(k):
        if not first:
            return -1  
        first = first.next

    while first:
        first = first.next
        second = second.next

    return second.data if second else -1


def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

head1 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(kth_from_end(head1, 2))  

head2 = create_linked_list([10, 5, 100, 5])
print(kth_from_end(head2, 5)) 
