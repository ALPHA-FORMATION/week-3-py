# Hackerrank: Print elements of linked list
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem



class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

if __name__ == "__main__":
    head = SinglyLinkedListNode(16)
    head.next = SinglyLinkedListNode(13)

    printLinkedList(head)
