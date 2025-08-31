# Add two numbers represented by linked lists
# https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1



class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
def addTwoLists(first, second):
    first = reverse_list(first)
    second = reverse_list(second)

    carry = 0
    result_head = None
    result_tail = None

    while first or second or carry:
        val1 = first.data if first else 0
        val2 = second.data if second else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        new_node = Node(digit)
        if not result_head:
            result_head = new_node
            result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = result_tail.next

        if first:
            first = first.next
        if second:
            second = second.next

    result_head = reverse_list(result_head)

    while result_head and result_head.data == 0 and result_head.next:
        result_head = result_head.next

    return result_head

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

head1 = Node(4, Node(5))
head2 = Node(3, Node(4, Node(5)))

result = addTwoLists(head1, head2)  
print_list(result)
head3 = Node(0, Node(0, Node(6, Node(3))))
head4 = Node(0, Node(7))

result = addTwoLists(head3, head4)  
print_list(result)
