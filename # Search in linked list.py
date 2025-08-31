# Search in linked list
# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def searchKey(head, key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False

def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

n = int(input("Enter number of nodes: "))
key = int(input("Enter key to search: "))
arr = list(map(int, input("Enter linked list elements: ").split()))

head = createLinkedList(arr)

if searchKey(head, key):
    print("true")
else:
    print("false")
