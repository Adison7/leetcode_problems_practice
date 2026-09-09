class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    # Find middle using slow/fast pointers, keeping track of the node before slow
    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Disconnect left half from middle
    if prev:
        prev.next = None

    root = TreeNode(slow.val)
    root.left = sortedListToBST(head if prev else None)
    root.right = sortedListToBST(slow.next)

    return root

######


def sortedListToBST(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next

    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(values[mid])
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(values) - 1)


#####

def sortedListToBST(head):
    # Get length first
    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    self_head = [head]  # mutable reference to advance through the list

    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2

        left_child = build(left, mid - 1)  # build left subtree first

        root = TreeNode(self_head[0].val)   # current node is next in-order value
        root.left = left_child
        self_head[0] = self_head[0].next    # advance pointer

        root.right = build(mid + 1, right)  # then build right subtree

        return root

    return build(0, n - 1)