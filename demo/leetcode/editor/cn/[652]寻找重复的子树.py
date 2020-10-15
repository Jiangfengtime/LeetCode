# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。 
# 
#  两棵树重复是指它们具有相同的结构以及相同的结点值。 
# 
#  示例 1： 
# 
#          1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
#  
# 
#  下面是两个重复的子树： 
# 
#        2
#      /
#     4
#  
# 
#  和 
# 
#      4
#  
# 
#  因此，你需要以列表的形式返回上述重复子树的根结点。 
#  Related Topics 树 
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
# leetcode submit region end(Prohibit modification and deletion)
