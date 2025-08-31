# Delete a node
# https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, x):
    if x == 1:
        return head.next 

    prev = None
    curr = head
    count = 1

    while curr and count < x:
        prev = curr
        curr = curr.next
        count += 1

    if curr:
        prev.next = curr.next

    return head

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

if __name__ == "__main__":
    elements = list(map(int, input("Enter elements of the linked list (space-separated): ").split()))
    x = int(input("Enter the position (1-based index) to delete: "))

    head = create_linked_list(elements)
    print("Original Linked List:")
    print_linked_list(head)

    head = delete_node(head, x)

    print("Linked List after deletion:")
    print_linked_list(head)
