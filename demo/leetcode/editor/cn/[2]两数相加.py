# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        current = res
        flag = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + flag
            flag = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if flag > 0:
            current.next = ListNode(flag)
        return res.next

    print(addTwoNumbers([2, 3, 5], [2, 5, 7]))