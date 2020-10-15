# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  示例: 
# 
#  输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 315 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
# leetcode submit region end(Prohibit modification and deletion)
