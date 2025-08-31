# Linked list insertion
# https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, x):
    new_node = Node(x)
    
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "\n")
        current = current.next

input_values = list(map(int, input("Enter linked list values (space separated): ").split()))
x = int(input("Enter the value to insert at the end: "))

head = build_linked_list(input_values)
head = insert_at_end(head, x)

print("Modified Linked List:")
print_linked_list(head)

