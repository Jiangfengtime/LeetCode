# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表 
#  👍 502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        index = 1
        res = head
        t1 = head
        while index < m:
            t1 = t1.next
        t2 = t1.next
        t3 = t1.next
        cur = t3.next
        while index < n:
            temp = cur.next
            cur.next = t3
            t3 = cur
            cur = temp
        t4 = cur.next
        t1.next = t3
        t3.next = t4
        return res



# leetcode submit region end(Prohibit modification and deletion)
