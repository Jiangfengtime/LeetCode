# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1229 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        pointer1 = l1
        pointer2 = l2
        while pointer1 and pointer2:
            if pointer1 < pointer2:
                result.next = pointer1
                pointer1 = pointer1.next
            else:
                result.next = pointer2
                pointer2 = pointer2.next
        while pointer1:
            result.next = pointer1
            pointer1 = pointer1.next
        while pointer2:
            result.next = pointer2
            pointer2 = pointer2.next
        return result


# leetcode submit region end(Prohibit modification and deletion)
