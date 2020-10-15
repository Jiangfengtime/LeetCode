# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。 
# 
#  
# 
#  示例： 
# 
#  输入：[1,2,3,4,5,null,7,8]
# 
#         1
#        /  \ 
#       2    3
#      / \    \ 
#     4   5    7
#    /
#   8
# 
# 输出：[[1],[2,3],[4,5,7],[8]]
#  
#  Related Topics 树 广度优先搜索 
#  👍 24 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
# leetcode submit region end(Prohibit modification and deletion)
