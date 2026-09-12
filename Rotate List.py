class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    k %= length
    if k == 0:
        return head
    
    # make circular
    tail.next = head
    
    # find new tail: (length - k - 1) steps from head
    steps_to_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head