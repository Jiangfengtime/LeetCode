# 给定一个非空二叉树，返回其最大路径和。 
# 
#  本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3]
# 
#        1
#       / \
#      2   3
# 
# 输出：6
#  
# 
#  示例 2： 
# 
#  输入：[-10,9,20,null,null,15,7]
# 
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# 
# 输出：42 
#  Related Topics 树 深度优先搜索 
#  👍 744 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
# leetcode submit region end(Prohibit modification and deletion)
