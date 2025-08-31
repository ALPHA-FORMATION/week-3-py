# Insert in circular linked list
# https://www.geeksforgeeks.org/problems/sorted-insert-for-circular-linked-list/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertInSorted(head, data):
    new_node = Node(data)

    if head is None:
        new_node.next = new_node
        return new_node

    current = head

    if data <= head.data:
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        head = new_node
        return head

    while current.next != head and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

def printList(head):
    if head is None:
        print("List is empty")
        return
    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()

head = Node(1)
second = Node(2)
third = Node(4)

head.next = second
second.next = third
third.next = head   

print("Original list:")
printList(head)

head = insertInSorted(head, 2)
print("After inserting 2:")
printList(head)

head2 = Node(1)
node2 = Node(4)
node3 = Node(7)
node4 = Node(9)

head2.next = node2
node2.next = node3
node3.next = node4
node4.next = head2   

print("\nOriginal list:")
printList(head2)

head2 = insertInSorted(head2, 5)
print("After inserting 5:")
printList(head2)
