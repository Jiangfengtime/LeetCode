# 删除链表中等于给定值 val 的所有节点。 
# 
#  示例: 
# 
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#  
#  Related Topics 链表 
#  👍 432 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode(0)
        result.next = head
        prev = result
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return result.next
# leetcode submit region end(Prohibit modification and deletion)
